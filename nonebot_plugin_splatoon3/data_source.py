import httpx
import json
import urllib3

from .translation import get_trans_stage, get_trans_weapon, get_trans
from .utils import *
from .imageProcesser import get_stages, get_all_coop_stages

schedule_res = None
http = urllib3.PoolManager()


# 校验过期日程
def check_expire_schedule(schedule):
    st = datetime.datetime.strptime(schedule['regularSchedules']['nodes'][0]['startTime'], '%Y-%m-%dT%H:%M:%SZ')
    ed = datetime.datetime.strptime(schedule['regularSchedules']['nodes'][0]['endTime'], '%Y-%m-%dT%H:%M:%SZ')
    nw = datetime.datetime.now() - datetime.timedelta(hours=8)
    if st < nw < ed:
        return False
    return True


# 取日程数据
def get_schedule():
    global schedule_res
    if schedule_res is None or check_expire_schedule(schedule_res):
        print('重新请求:日程数据')
        with httpx.Client() as client:
            result = client.get('https://splatoon3.ink/data/schedules.json')
            schedule_res = json.load(result)
            schedule_res = schedule_res['data']
            return schedule_res
    else:
        return schedule_res


# 取 打工
def get_coop_info(all=False):
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
    def get_str_info(sch):
        start_time = time_converter_day(sch['startTime'])
        end_time = time_converter_day(sch['endTime'])
        return '{} - {}'.format(start_time, end_time)

    # 取日程
    schedule = get_schedule()
    # 取翻译
    get_trans()
    schedule = schedule['coopGroupingSchedule']['regularSchedules']['nodes']
    if not all:
        # 只输出两排
        stage = [get_stage_image_info(schedule[0]), get_stage_image_info(schedule[1])]
        weapon = [get_weapon_image_info(schedule[0]), get_weapon_image_info(schedule[1])]
        info = [get_str_info(schedule[0]), get_str_info(schedule[1])]
    else:
        # 输出全部(五排)
        stage = [get_stage_image_info(sch) for sch in schedule]
        weapon = [get_weapon_image_info(sch) for sch in schedule]
        info = [get_str_info(sch) for sch in schedule]

    return get_all_coop_stages(stage, weapon, info)


# 取 图
def get_stage_info(num_list=None, stage_mode=None):
    if num_list is None:
        num_list = [0]
    schedule = get_schedule()
    get_trans()
    if stage_mode is not None:
        if len(stage_mode) == 2:
            return get_stages(schedule, num_list, map_contest[stage_mode[:2]])
        elif len(stage_mode) == 4:
            return get_stages(schedule, num_list, map_contest[stage_mode[2:]], map_rule[stage_mode[:2]])
        else:
            raise NameError()
    return get_stages(schedule, num_list)


if __name__ == '__main__':
    # get_stage_info().show()
    get_coop_info().show()
