from nonebot_plugin_splatoon3.data_source import *
from nonebot_plugin_splatoon3.utils import *
from nonebot_plugin_splatoon3.imageProcesser import *


# 测试打工图片
res_coop = get_coop_info(all=True)
file = open('../output/coop.jpg', "wb")
file.write(res_coop)
