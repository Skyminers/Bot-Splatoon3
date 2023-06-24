from nonebot_plugin_splatoon3.data_source import *
from nonebot_plugin_splatoon3.utils import *
from nonebot_plugin_splatoon3.imageProcesser import *

# 测试打工图片
# res = get_coop_info(all=True)
# file = open('../output/coop.jpg', "wb")
# file.write(res)

# 测试 图
# res = get_stage_info(num_list=None, stage_mode=None)
# file = open('../output/stage.jpg', "wb")
# file.write(res)

# 测试 随机武器
res = get_random_weapon(weapon1=None, weapon2=None)
file = open('../output/random_weapon.jpg', "wb")
file.write(res)
