import httpx
import json
import urllib3

from .translation import get_trans_stage, get_trans_weapon, get_trans_data, list_salmonrun_mode
from .utils import *
from .imageProcesser import get_stages

schedule_res = None
http = urllib3.PoolManager()


# 取日程数据
def get_schedule_data():
    # 校验过期日程
    def check_expire_schedule(schedule):
        st = datetime.datetime.strptime(schedule['regularSchedules']['nodes'][0]['startTime'], '%Y-%m-%dT%H:%M:%SZ')
        ed = datetime.datetime.strptime(schedule['regularSchedules']['nodes'][0]['endTime'], '%Y-%m-%dT%H:%M:%SZ')
        nw = datetime.datetime.now() - datetime.timedelta(hours=8)
        if st < nw < ed:
            return False
        return True

    global schedule_res
    if schedule_res is None or check_expire_schedule(schedule_res):
        print('nonebot_plugin_splatoon3: 重新请求:日程数据')
        with httpx.Client() as client:
            result = client.get('https://splatoon3.ink/data/schedules.json')
            schedule_res = json.load(result)
            schedule_res = schedule_res['data']
            return schedule_res
    else:
        return schedule_res


# 取 打工
def get_coop_info(all=None):
    # 取地图信息
    def get_stage_image_info(sch):  # sch为schedule[idx]
        return ImageInfo(sch['setting']['coopStage']['name'],
                         sch['setting']['coopStage']['image']['url'],
                         get_trans_stage(sch['setting']['coopStage']['id']))

    # 取装备信息
    def get_weapon_image_info(sch):  # sch为schedule[idx]
        return [ImageInfo(sch['setting']['weapons'][i]['name'],
                          sch['setting']['weapons'][i]['image']['url'],
                          get_trans_weapon(sch['setting']['weapons'][i]['__splatoon3ink_id']))
                for i in range(4)]

    # 取时间信息
    def get_str_time(sch):
        start_time = time_converter_day(sch['startTime'])
        end_time = time_converter_day(sch['endTime'])
        return '{} - {}'.format(start_time, end_time)

    # 取boss名称
    def get_str_boss(sch):
        return sch['__splatoon3ink_king_salmonid_guess']

    # 校验普通打工时间，是否在特殊打工模式之后
    def check_salmonrun_time(start_time, special_mode_start_time):
        st = datetime.datetime.strptime(start_time, '%m-%d %H:%M')
        su_st = datetime.datetime.strptime(special_mode_start_time, '%m-%d %H:%M')
        if st > su_st:
            return True
        return False

    # 取日程
    schedule = get_schedule_data()
    # 取翻译
    get_trans_data()
    # 一般打工数据
    regular_schedule = schedule['coopGroupingSchedule']['regularSchedules']['nodes']
    # 团队打工竞赛
    team_schedule = schedule['coopGroupingSchedule']['teamContestSchedules']['nodes']
    # big run 数据
    bigrun_schedule = schedule['coopGroupingSchedule']['bigRunSchedules']['nodes']
    stage = []
    weapon = []
    time = []
    boss = []
    mode = []
    schedule = regular_schedule
    if not all:
        # 只输出两排
        for i in range(2):
            stage.append(get_stage_image_info(schedule[i]))
            weapon.append(get_weapon_image_info(schedule[i]))
            time.append(get_str_time(schedule[i]))
            boss.append(get_str_boss(schedule[i]))
            mode.append(list_salmonrun_mode[0])
    else:
        # 输出全部(五排)
        stage = [get_stage_image_info(sch) for sch in schedule]
        weapon = [get_weapon_image_info(sch) for sch in schedule]
        time = [get_str_time(sch) for sch in schedule]
        boss = [get_str_boss(sch) for sch in schedule]
        mode = [list_salmonrun_mode[0] for sch in schedule]

    # 如果存在 团队打工
    if len(team_schedule) != 0:
        schedule = team_schedule
        # 计算插入索引
        insert_idx = 0
        need_offset = False
        special_mode_start_time = get_str_time(schedule[0]).split(" - ")[0]
        for k, v in enumerate(time):
            start_time = v.split(" - ")[0]
            if check_salmonrun_time(start_time, special_mode_start_time):
                insert_idx = k
        if not need_offset:
            insert_idx = len(time)

        # 插入数据
        stage.insert(insert_idx, get_stage_image_info(schedule[0]))
        weapon.insert(insert_idx, get_weapon_image_info(schedule[0]))
        time.insert(insert_idx, get_str_time(schedule[0]))
        # 团队打工取不到boss信息
        boss.insert(insert_idx, "")
        mode.insert(insert_idx, list_salmonrun_mode[1])

    # 如果存在 bigrun
    if len(bigrun_schedule) != 0:
        schedule = bigrun_schedule
        # 计算插入索引
        insert_idx = 0
        need_offset = False
        special_mode_start_time = get_str_time(schedule[0]).split(" - ")[0]
        for k, v in enumerate(time):
            start_time = v.split(" - ")[0]
            if check_salmonrun_time(start_time, special_mode_start_time):
                insert_idx = k
                need_offset = True

        if not need_offset:
            insert_idx = len(time)
        # 插入数据
        stage.insert(insert_idx, get_stage_image_info(schedule[0]))
        weapon.insert(insert_idx, get_weapon_image_info(schedule[0]))
        time.insert(insert_idx, get_str_time(schedule[0]))
        # 团队打工取不到boss信息
        boss.insert(insert_idx, "")
        mode.insert(insert_idx, list_salmonrun_mode[2])

    return stage, weapon, time, boss, mode


# 取 图
def get_stage_info(num_list=None, stage_mode=None):
    if num_list is None:
        num_list = [0]
    schedule = get_schedule_data()
    get_trans_data()
    contest_match = None
    rule_match = None
    if stage_mode is not None:
        if len(stage_mode) == 2:
            contest_match = map_contest[stage_mode[:2]]
        elif len(stage_mode) == 4:
            contest_match = map_contest[stage_mode[2:]]
            rule_match = map_rule[stage_mode[:2]]

    return schedule, num_list, contest_match, rule_match


if __name__ == '__main__':
    # get_stage_info().show()
    get_coop_info().show()
