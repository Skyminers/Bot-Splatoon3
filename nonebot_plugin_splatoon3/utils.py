import datetime
from multiprocessing import Lock

# map
map_contest = {'涂地': 'Turf War', '挑战': 'Ranked Challenge', '开放': 'Ranked Open', 'X段': 'X Schedule',
               'x段': 'X Schedule'}
map_rule = {'区域': 'AREA', '推塔': 'LOFT', '蛤蜊': 'CLAM', '抢鱼': 'GOAL'}

# 群白名单
white_list = ['458482582', '792711635', '835723997', '578031026', '1607044636']


# 类 图片信息 自身转化为对象
class ImageInfo:
    def __init__(self, name, url, zh_name):
        self.name = name
        self.url = url
        self.zh_name = zh_name


image_json_lock = Lock()





# 时间转换 时:分
def time_converter(time_str):
    # convert time to UTC+8
    dt = datetime.datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%SZ')
    dt += datetime.timedelta(hours=8)
    return datetime.datetime.strftime(dt, '%H:%M')


# 时间转换 月-天 时:分
def time_converter_day(time_str):
    # convert time to UTC+8
    dt = datetime.datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%SZ')
    dt += datetime.timedelta(hours=8)
    return datetime.datetime.strftime(dt, '%m-%d %H:%M')


# 获取年月日
def get_time_ymd():
    # convert time to UTC+8
    dt = datetime.datetime.now().strftime('%Y-%m-%d')
    return dt

# 校验群号
def check_group_id(group_id):
    # if group_id == '616533832':
    #     return False
    return True


