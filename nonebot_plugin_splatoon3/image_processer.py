import os
import urllib3
from PIL import Image, ImageDraw, ImageFont

from ._class import WeaponData, ImageInfo
from .image_processer_tools import (
    get_file,
    tiled_fill,
    paste_with_a,
    get_stage_card,
    get_time_head_bg,
    circle_corner,
    get_save_file,
    get_stage_name_bg,
    get_weapon_card,
    have_festival,
    get_event_card,
    change_image_alpha,
    get_event_desc_card,
)
from .translation import get_trans_stage, get_trans_cht_data, dict_rule_reverse_trans
from .utils import *

# 根路径
cur_path = os.path.dirname(__file__)

# 图片文件夹
image_folder = os.path.join(cur_path, "staticData", "ImageData")
# 武器文件夹
weapon_folder = os.path.join(cur_path, "staticData", "weapon")
# 字体
ttf_path = os.path.join(cur_path, "staticData", "SplatoonFontFix.otf")
ttf_path_chinese = os.path.join(cur_path, "staticData", "Text.ttf")

http = urllib3.PoolManager()


# 绘制 祭典地图
def get_festival(festivals):
    background_size = (1000, 700)
    # 取背景rgb颜色
    bg_rgb = dict_bg_rgb["祭典"]
    # 创建纯色背景
    image_background = Image.new("RGBA", background_size, bg_rgb)
    bg_mask = get_file("祭典蒙版").resize((600, 400))
    # 填充小图蒙版
    image_background = tiled_fill(image_background, bg_mask)
    return image_background


# 绘制 活动地图
def get_events(events):
    background_size = (1084, 2200)
    event_card_bg_size = (background_size[0] - 40, 640)
    # 取背景rgb颜色
    bg_rgb = dict_bg_rgb["活动"]
    # 创建纯色背景
    image_background = Image.new("RGBA", background_size, bg_rgb)
    bg_mask = get_file("猫爪蒙版").resize((400, 250))
    # 填充小图蒙版
    image_background = tiled_fill(image_background, bg_mask)
    # 圆角
    _, image_background = circle_corner(image_background, radii=20)
    # 遍历每个活动
    pos_h = 0
    for index, event in enumerate(events):
        # 获取翻译
        cht_event_data = event["leagueMatchSetting"]["leagueMatchEvent"]
        _id = cht_event_data["id"]
        trans_cht_event_data = get_trans_cht_data()["events"][_id]
        # 替换为翻译文本
        cht_event_data["name"] = trans_cht_event_data["name"]
        cht_event_data["desc"] = trans_cht_event_data["desc"]
        cht_event_data["regulation"] = trans_cht_event_data["regulation"]
        event["leagueMatchSetting"]["vsRule"]["rule"] = dict_rule_reverse_trans.get(
            event["leagueMatchSetting"]["vsRule"]["rule"]
        )
        # 顶部活动标志(大号)
        pos_h += 20
        game_mode_img_size = (80, 80)
        game_mode_img = get_file("活动比赛").resize(game_mode_img_size, Image.ANTIALIAS)
        game_mode_img_pos = (20, pos_h)
        paste_with_a(image_background, game_mode_img, game_mode_img_pos)
        pos_h += game_mode_img_size[1] + 20
        # 绘制主标题
        main_title = cht_event_data["name"]
        drawer = ImageDraw.Draw(image_background)
        ttf = ImageFont.truetype(ttf_path_chinese, 40)
        main_title_pos = (game_mode_img_pos[0] + game_mode_img_size[0] + 20, game_mode_img_pos[1])
        main_title_size = ttf.getsize(main_title)
        drawer.text(main_title_pos, main_title, font=ttf, fill=(255, 255, 255))
        # 绘制描述
        desc = cht_event_data["desc"]
        ttf = ImageFont.truetype(ttf_path_chinese, 30)
        desc_pos = (main_title_pos[0], main_title_pos[1] + main_title_size[1] + 10)
        drawer.text(desc_pos, desc, font=ttf, fill=(255, 255, 255))
        # 绘制对战卡片
        event_card = get_event_card(event, event_card_bg_size)
        event_card_pos = (20, pos_h)
        paste_with_a(image_background, event_card, event_card_pos)
        pos_h += event_card_bg_size[1] + 10
        # 绘制祭典说明卡片
        event_desc_card_bg_size = (event_card_bg_size[0], 300)
        event_desc_card = get_event_desc_card(cht_event_data, event_desc_card_bg_size)
        event_card_pos = (20, pos_h)
        paste_with_a(image_background, event_desc_card, event_card_pos)
        pos_h += event_desc_card_bg_size[1]
        # 计算下一行高度
        pos_h += 20
    return image_background


# 绘制 竞赛地图
def get_stages(schedule, num_list, contest_match=None, rule_match=None):
    # 涂地
    regular = schedule["regularSchedules"]["nodes"]
    # 真格
    ranked = schedule["bankaraSchedules"]["nodes"]
    # X段
    xschedule = schedule["xSchedules"]["nodes"]
    # 祭典
    festivals = schedule["festSchedules"]["nodes"]

    # 如果存在祭典时，转变为输出祭典地图，后续不再进行处理
    if have_festival(festivals):
        image = get_festival(festivals)
        return image

    cnt = 0
    time_head_count = 0
    # 计算满足条件的有效数据有多少排
    for i in num_list:
        # 筛选到数据的个数
        count_match_data = 0
        if contest_match is None or contest_match == "Turf War":
            if rule_match is None:
                cnt += 1
                count_match_data += 1
        if contest_match is None or contest_match == "Ranked Challenge":
            if rule_match is None or rule_match == ranked[i]["bankaraMatchSettings"][0]["vsRule"]["rule"]:
                cnt += 1
                count_match_data += 1
        if contest_match is None or contest_match == "Ranked Open":
            if rule_match is None or rule_match == ranked[i]["bankaraMatchSettings"][1]["vsRule"]["rule"]:
                cnt += 1
                count_match_data += 1

        if contest_match is None or contest_match == "X Schedule":
            if rule_match is None or rule_match == xschedule[i]["xMatchSetting"]["vsRule"]["rule"]:
                cnt += 1
                count_match_data += 1

        # 如果有筛选结果,需要加上一个时间卡片
        if count_match_data:
            time_head_count += 1

    if cnt == 0:
        # 没有搜索结果情况下，用全部list再次调用自身
        num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        return get_stages(schedule, num_list, contest_match, rule_match)

    time_head_bg_size = (540, 60)
    # 一张对战卡片高度为340 时间卡片高度为time_head_bg_size[1] 加上间隔为10
    background_size = (1044, 340 * cnt + (time_head_bg_size[1] + 10) * time_head_count)
    # 取背景rgb颜色
    default_bg_rgb = dict_bg_rgb["X Schedule"]
    if contest_match is not None:
        bg_rgb = dict_bg_rgb[contest_match]
    else:
        bg_rgb = default_bg_rgb
    # 创建纯色背景
    image_background = Image.new("RGBA", background_size, bg_rgb)
    bg_mask = get_file("对战蒙版").resize((600, 399))
    # 填充小图蒙版
    image_background = tiled_fill(image_background, bg_mask)

    total_pos = 0
    for i in num_list:
        pos = 0
        # 创建一张纯透明图片 用来存放一个时间周期内的多张地图卡片
        background = Image.new("RGBA", background_size, (0, 0, 0, 0))
        # 筛选到数据的个数
        count_match_data = 0

        # 第一排绘制 默认为涂地模式
        if contest_match is None or contest_match == "Turf War":
            if rule_match is None:
                count_match_data += 1

                stage = regular[i]["regularMatchSetting"]["vsStages"]
                regular_card = get_stage_card(
                    ImageInfo(
                        stage[0]["name"],
                        stage[0]["image"]["url"],
                        get_trans_stage(stage[0]["id"]),
                        "对战地图",
                    ),
                    ImageInfo(
                        stage[1]["name"],
                        stage[1]["image"]["url"],
                        get_trans_stage(stage[1]["id"]),
                        "对战地图",
                    ),
                    "一般比赛",
                    "Regular",
                    regular[i]["regularMatchSetting"]["vsRule"]["rule"],
                    time_converter_hm(regular[i]["startTime"]),
                    time_converter_hm(regular[i]["endTime"]),
                )
                paste_with_a(background, regular_card, (10, pos))
                pos += 340
                total_pos += 340

        # 第二排绘制 默认为真格区域
        if contest_match is None or contest_match == "Ranked Challenge":
            if rule_match is None or rule_match == ranked[i]["bankaraMatchSettings"][0]["vsRule"]["rule"]:
                count_match_data += 1
                stage = ranked[i]["bankaraMatchSettings"][0]["vsStages"]
                ranked_challenge_card = get_stage_card(
                    ImageInfo(
                        stage[0]["name"],
                        stage[0]["image"]["url"],
                        get_trans_stage(stage[0]["id"]),
                        "对战地图",
                    ),
                    ImageInfo(
                        stage[1]["name"],
                        stage[1]["image"]["url"],
                        get_trans_stage(stage[1]["id"]),
                        "对战地图",
                    ),
                    "蛮颓比赛-挑战",
                    "Ranked-Challenge",
                    ranked[i]["bankaraMatchSettings"][0]["vsRule"]["rule"],
                    time_converter_hm(ranked[i]["startTime"]),
                    time_converter_hm(ranked[i]["endTime"]),
                )
                paste_with_a(background, ranked_challenge_card, (10, pos))
                pos += 340
                total_pos += 340

        # 第三排绘制 默认为真格开放
        if contest_match is None or contest_match == "Ranked Open":
            if rule_match is None or rule_match == ranked[i]["bankaraMatchSettings"][1]["vsRule"]["rule"]:
                count_match_data += 1
                stage = ranked[i]["bankaraMatchSettings"][1]["vsStages"]
                ranked_challenge_card = get_stage_card(
                    ImageInfo(
                        stage[0]["name"],
                        stage[0]["image"]["url"],
                        get_trans_stage(stage[0]["id"]),
                        "对战地图",
                    ),
                    ImageInfo(
                        stage[1]["name"],
                        stage[1]["image"]["url"],
                        get_trans_stage(stage[1]["id"]),
                        "对战地图",
                    ),
                    "蛮颓比赛-开放",
                    "Ranked-Open",
                    ranked[i]["bankaraMatchSettings"][1]["vsRule"]["rule"],
                    time_converter_hm(ranked[i]["startTime"]),
                    time_converter_hm(ranked[i]["endTime"]),
                )
                paste_with_a(background, ranked_challenge_card, (10, pos))
                pos += 340
                total_pos += 340

        # 第四排绘制 默认为X赛
        if contest_match is None or contest_match == "X Schedule":
            if rule_match is None or rule_match == xschedule[i]["xMatchSetting"]["vsRule"]["rule"]:
                count_match_data += 1
                stage = xschedule[i]["xMatchSetting"]["vsStages"]
                ranked_challenge_card = get_stage_card(
                    ImageInfo(
                        stage[0]["name"],
                        stage[0]["image"]["url"],
                        get_trans_stage(stage[0]["id"]),
                        "对战地图",
                    ),
                    ImageInfo(
                        stage[1]["name"],
                        stage[1]["image"]["url"],
                        get_trans_stage(stage[1]["id"]),
                        "对战地图",
                    ),
                    "X比赛",
                    "X",
                    xschedule[i]["xMatchSetting"]["vsRule"]["rule"],
                    time_converter_hm(xschedule[i]["startTime"]),
                    time_converter_hm(xschedule[i]["endTime"]),
                )
                paste_with_a(background, ranked_challenge_card, (10, pos))
                pos += 340
                total_pos += 340
        # 如果有筛选结果，将时间表头贴到底图上
        if count_match_data:
            # 取涂地模式的时间，除举办祭典外，都可用
            date_time = time_converter_yd(regular[i]["startTime"])
            start_time = time_converter_hm(regular[i]["startTime"])
            end_time = time_converter_hm(regular[i]["endTime"])
            # 绘制时间表头
            time_head_bg = get_time_head_bg(time_head_bg_size, date_time, start_time, end_time)
            # 贴到大图上
            time_head_bg_pos = (
                (background_size[0] - time_head_bg_size[0]) // 2,
                total_pos - 340 * count_match_data + 10,
            )
            paste_with_a(image_background, time_head_bg, time_head_bg_pos)
            total_pos += time_head_bg_size[1] + 10

            # 将一组图片贴到底图上
            paste_with_a(
                image_background,
                background,
                (0, time_head_bg_pos[1] + time_head_bg_size[1]),
            )

    # 圆角化
    _, image_background = circle_corner(image_background, radii=16)
    return image_background


# 绘制 打工地图
def get_coop_stages(stage, weapon, time, boss, mode):
    # 校验是否需要绘制小鲑鱼(现在时间处于该打工时间段内)
    def check_coop_fish(_time):
        start_time = _time.split(" - ")[0]
        # 输入时间都缺少年份，需要手动补充一个年份后还原为date对象
        year = datetime.datetime.now().year
        start_time = str(year) + "-" + start_time
        now_time = datetime.datetime.now()
        st = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M")
        if st < now_time:
            return True
        return False

    top_size_pos = (0, -2)
    bg_size = (800, len(stage) * 162 + top_size_pos[1])
    stage_bg_size = (300, 160)
    weapon_size = (90, 90)
    boss_size = (40, 40)
    mode_size = (40, 40)
    coop_fish_size = (36, 48)

    # 创建纯色背景
    image_background_rgb = dict_bg_rgb["打工"]
    image_background = Image.new("RGBA", bg_size, image_background_rgb)
    bg_mask_size = (300, 200)
    bg_mask = get_file("打工蒙版").resize(bg_mask_size)
    # 填充小图蒙版
    image_background = tiled_fill(image_background, bg_mask)

    # 绘制地图信息
    coop_stage_bg = Image.new("RGBA", (bg_size[0], bg_size[1] + 2), (0, 0, 0, 0))
    dr = ImageDraw.Draw(coop_stage_bg)
    font = ImageFont.truetype(ttf_path, 30)
    for pos, val in enumerate(time):
        # 绘制时间文字
        time_text_pos = (40, 5 + pos * 160)
        time_text_size = font.getsize(val)
        dr.text(time_text_pos, val, font=font, fill="#FFFFFF")
        if check_coop_fish(val):
            # 现在时间处于打工时间段内，绘制小鲑鱼
            coop_fish_img = get_file("小鲑鱼").resize(coop_fish_size)
            coop_fish_img_pos = (6, 8 + pos * 160)
            paste_with_a(coop_stage_bg, coop_fish_img, coop_fish_img_pos)
    for pos, val in enumerate(stage):
        # 绘制打工地图
        stage_bg = get_save_file(val).resize(stage_bg_size, Image.ANTIALIAS)
        stage_bg_pos = (500, 2 + 162 * pos)
        coop_stage_bg.paste(stage_bg, stage_bg_pos)

        # 绘制 地图名
        stage_name_bg = get_stage_name_bg(val.zh_name, 25)
        stage_name_bg_size = stage_name_bg.size
        # X:地图x点位+一半的地图宽度-文字背景的一半宽度   Y:地图Y点位+一半地图高度-文字背景高度
        stage_name_bg_pos = (
            stage_bg_pos[0] + +stage_bg_size[0] // 2 - stage_name_bg_size[0] // 2,
            stage_bg_pos[1] + stage_bg_size[1] - stage_name_bg_size[1],
        )
        paste_with_a(coop_stage_bg, stage_name_bg, stage_name_bg_pos)

        for pos_weapon, val_weapon in enumerate(weapon[pos]):
            # 绘制武器底图
            weapon_bg_img = Image.new("RGBA", weapon_size, (30, 30, 30))
            # 绘制武器图片
            weapon_image = get_save_file(val_weapon).resize(weapon_size, Image.ANTIALIAS)
            paste_with_a(weapon_bg_img, weapon_image, (0, 0))
            coop_stage_bg.paste(weapon_bg_img, (120 * pos_weapon + 20, 60 + 160 * pos))
    for pos, val in enumerate(boss):
        if val != "":
            # 绘制boss图标
            boss_img = get_file(val).resize(boss_size)
            boss_img_pos = (500, 160 * pos + stage_bg_size[1] - 40)
            paste_with_a(coop_stage_bg, boss_img, boss_img_pos)
    for pos, val in enumerate(mode):
        # 绘制打工模式图标
        mode_img = get_file(val).resize(mode_size)
        mode_img_pos = (500 - 70, 160 * pos + 15)
        paste_with_a(coop_stage_bg, mode_img, mode_img_pos)

    paste_with_a(image_background, coop_stage_bg, top_size_pos)
    # 圆角
    _, image_background = circle_corner(image_background, radii=20)

    return image_background


# 绘制 随机武器
def get_random_weapon(weapon1: [WeaponData], weapon2: [WeaponData]):
    # 底图
    image_background_size = (660, 500)
    _, image_background = circle_corner(get_file("背景2").resize(image_background_size), radii=20)
    # 绘制上下两块武器区域
    weapon_card_bg_size = (image_background_size[0] - 10, (image_background_size[1] - 10) // 2)
    top_weapon_card = get_weapon_card(weapon1, weapon_card_bg_size, dict_bg_rgb["上-武器卡片-黄"])
    down_weapon_card = get_weapon_card(weapon2, weapon_card_bg_size, dict_bg_rgb["下-武器卡片-蓝"])
    # 将武器区域贴到最下层背景
    paste_with_a(image_background, top_weapon_card, (5, 5))
    paste_with_a(image_background, down_weapon_card, (5, (image_background_size[1]) // 2))
    # 绘制私房图标
    private_img_size = (35, 35)
    private_img_pos = (
        (image_background_size[0] - private_img_size[0]) // 2,
        (image_background_size[1] - private_img_size[1]) // 2,
    )
    private_img = get_file("private").resize(private_img_size)
    paste_with_a(image_background, private_img, private_img_pos)

    return image_background
