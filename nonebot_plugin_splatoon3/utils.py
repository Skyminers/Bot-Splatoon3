import datetime

# dict
dict_contest = {
    "涂地": "Turf War",
    "挑战": "Ranked Challenge",
    "开放": "Ranked Open",
    "X段": "X Schedule",
}
dict_rule = {
    "区域": "AREA",
    "蛤蜊": "CLAM",
    "塔楼": "LOFT",
    "鱼虎": "GOAL",
}

# 触发关键词  同义文本替换
dict_keyword_replace = {
    "\\": "",
    "/": "",
    ".": "",
    "。": "",
    "涂涂": "涂地",
    "组排": "开放",
    "排排": "开放",
    "pp": "开放",
    "PP": "开放",
    "真格": "挑战",
    "x段": "X段",
    "X赛": "X段",
    "x赛": "X段",
    "推塔": "塔楼",
    "抢塔": "塔楼",
    "抢鱼": "鱼虎",
    "鲑鱼跑": "工",
    "团队打工": "工",
    "打工": "工",
    "big run": "工",
    "bigrun": "工",
    "help": "帮助",
    "衣服": "装备",
}

# 语义化字典 装备 副武器
dict_weapon_sub = {
    "斯普拉炸弹": "斯普拉炸弹",
    "三角雷": "斯普拉炸弹",
    "吸盘炸弹": "吸盘炸弹",
    "粘弹": "吸盘炸弹",
    "黏弹": "吸盘炸弹",
    "快速炸弹": "快速炸弹",
    "水球": "快速炸弹",
    "洒墨器": "洒墨器",
    "花洒": "洒墨器",
    "斯普拉防护墙": "斯普拉防护墙",
    "水帘": "斯普拉防护墙",
    "帘子": "斯普拉防护墙",
    "雨帘": "斯普拉防护墙",
    "碳酸炸弹": "碳酸炸弹",
    "碳酸": "碳酸炸弹",
    "摇摇乐": "碳酸炸弹",
    "冰壶炸弹": "冰壶炸弹",
    "冰壶": "冰壶炸弹",
    "机器人炸弹": "机器人炸弹",
    "小鸡雷": "机器人炸弹",
    "跳跃信标": "跳跃信标",
    "跳点": "跳跃信标",
    "信标": "跳跃信标",
    "定点侦测器": "定点侦测器",
    "狗链": "定点侦测器",
    "狗环": "定点侦测器",
    "墨汁陷阱": "墨汁陷阱",
    "陷阱": "墨汁陷阱",
    "地雷": "墨汁陷阱",
    "毒雾": "毒雾",
    "毒瓶": "毒雾",
    "标线器": "标线器",
    "马克笔": "标线器",
    "鱼雷": "鱼雷",
}

# 语义化字典 装备 大招
dict_weapon_special = {
    "终极发射": "终极发射",
    "rpg": "终极发射",
    "RPG": "终极发射",
    "巨大防护罩": "巨大防护罩",
    "防护罩": "巨大防护罩",
    "触手喷射": "触手喷射",
    "触手": "触手喷射",
    "蜘蛛侠": "触手喷射",
    "多重导弹": "多重导弹",
    "导弹": "多重导弹",
    "墨雨云": "墨雨云",
    "下雨": "墨雨云",
    "赞气弹": "赞气弹",
    "nice弹": "赞气弹",
    "弹跳声呐": "弹跳声呐",
    "跳蛋": "弹跳声呐",
    "声呐": "弹跳声呐",
    "吸墨机": "吸墨机",
    "吸尘器": "吸墨机",
    "喇叭辐射5.1ch": "喇叭辐射5.1ch",
    "镭射": "喇叭辐射5.1ch",
    "激光": "喇叭辐射5.1ch",
    "喷射背包": "喷射背包",
    "喷气背包": "喷射背包",
    "飞机": "喷射背包",
    "jet": "喷射背包",
    "JET": "喷射背包",
    "终极印章": "终极印章",
    "印章": "终极印章",
    "锤子": "终极印章",
    "大锤": "终极印章",
    "螃蟹坦克": "螃蟹坦克",
    "螃蟹": "螃蟹坦克",
    "鲨鱼坐骑": "鲨鱼坐骑",
    "鲨鱼": "鲨鱼坐骑",
    "三重龙卷风": "三重龙卷风",
    "龙卷风": "三重龙卷风",
    "能量站": "能量站",
    "饮料站": "能量站",
    "饮料": "能量站",
    "诱饵烟花": "诱饵烟花",
    "反击狼烟": "诱饵烟花",
    "烟花": "诱饵烟花",
    "诱饵": "诱饵烟花",
    "帝王鱿鱼": "帝王鱿鱼",
    "鱿鱼": "帝王鱿鱼",
    "帝王乌贼": "帝王鱿鱼",
    "大王乌贼": "帝王鱿鱼",
}

# 语义化字典 装备类别
dict_weapon_class = {
    "射击枪": "射击枪",
    "小枪": "射击枪",
    "爆破枪": "爆破枪",
    "泡": "爆破枪",
    "炮": "爆破枪",
    "伞": "伞",
    "笔刷": "笔刷",
    "画笔": "笔刷",
    "刷子": "笔刷",
    "笔": "笔刷",
    "狙击枪": "狙击枪",
    "狙": "狙击枪",
    "双枪": "双枪",
    "滚筒": "滚筒",
    "筒": "滚筒",
    "刷": "滚筒",
    "泼桶": "泼桶",
    "桶": "泼桶",
    "刮水刀": "刮水刀",
    "电锯": "刮水刀",
    "锯": "刮水刀",
    "水刀": "刮水刀",
    "刀": "刮水刀",
    "旋转枪": "旋转枪",
    "加特林": "旋转枪",
    "加": "旋转枪",
    "弓": "弓",
}

# 背景 rgb颜色
dict_bg_rgb = {
    "Turf War": (24, 200, 26),
    "Ranked Challenge": (227, 68, 17),
    "Ranked Open": (24, 200, 26),
    "X Schedule": (14, 205, 147),
    "打工": (14, 203, 146),
    "活动": (223, 42, 119),
}


# 类 图片信息 自身转化为对象
class ImageInfo:
    def __init__(self, name, url, zh_name, source_type):
        self.name = name
        self.url = url
        self.zh_name = zh_name
        self.source_type = source_type


# 类 数据库 Weapon_Data
class WeaponData:
    # zh 字段暂且预留，方便后续翻译的进行
    # 为了便于先进行 INFO 信息的查询，image 字段默认留空
    def __init__(
        self,
        name,
        sub_name,
        special_name,
        special_points,
        level,
        weapon_class,
        image=None,
        sub_image=None,
        special_image=None,
        weapon_class_image=None,
        zh_name="None",
        zh_sub_name="None",
        zh_special_name="None",
    ):
        self.name = name
        self.image = image
        self.sub_name = sub_name
        self.sub_image = sub_image
        self.special_name = special_name
        self.special_image = special_image
        self.special_points = special_points
        self.level = level
        self.weapon_class = weapon_class
        self.weapon_class_image = weapon_class_image
        self.zh_name = zh_name
        self.zh_sub_name = zh_sub_name
        self.zh_special_name = zh_special_name


# 批量替换文本
def multiple_replace(text):
    for key in dict_keyword_replace:
        text = text.replace(key, dict_keyword_replace[key])
    return text


# 时间转换 月-日
def time_converter_yd(time_str):
    # convert time to UTC+8
    dt = datetime.datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%SZ")
    dt += datetime.timedelta(hours=8)
    return datetime.datetime.strftime(dt, "%m.%d")


# 时间转换 时:分
def time_converter(time_str):
    # convert time to UTC+8
    dt = datetime.datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%SZ")
    dt += datetime.timedelta(hours=8)
    return datetime.datetime.strftime(dt, "%H:%M")


# 时间转换 月-日 时:分
def time_converter_day(time_str):
    # convert time to UTC+8
    dt = datetime.datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%SZ")
    dt += datetime.timedelta(hours=8)
    return datetime.datetime.strftime(dt, "%m-%d %H:%M")


# 获取年月日
def get_time_ymd():
    # convert time to UTC+8
    dt = datetime.datetime.now().strftime("%Y-%m-%d")
    return dt
