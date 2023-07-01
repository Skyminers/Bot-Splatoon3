import datetime

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
        zh_weapon_class="None",
        zh_father_class="None",
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
        self.zh_weapon_class = zh_weapon_class
        self.zh_father_class = zh_father_class


# 批量替换文本
def multiple_replace(text, _dict):
    for key in _dict:
        text = text.replace(key, _dict[key])
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
