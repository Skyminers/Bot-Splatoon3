from nonebot_plugin_splatoon3.image import *
from nonebot_plugin_splatoon3.staticDataGetter import reload_weapon_info

# 测试打工图片
# res = get_coop_stages_image(True)
# res.show()

# 测试重载武器数据
# reload_weapon_info()

#
# # 测试 图
# res = get_stage_info(num_list=None, stage_mode=None)
# file = open('../output/stage.jpg', "wb")
# file.write(res)

# # 测试 随机武器
# res = get_random_weapon(weapon1=None, weapon2=None)
# file = open('../output/random_weapon.jpg', "wb")
# file.write(res)

# 测试nonebot 打工 命令文本触发
# plain_text = '工'
# # 传递函数指针
# func = get_coop_stages_image
# res = get_save_temp_image(plain_text, func, False)
# img = res


# 测试nonebot 对战 命令文本触发
# plain_text = '全部挑战'
# # 传递函数指针
# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# stage_mode = plain_text[-2:]
# func = get_stages_image
# res = get_save_temp_image(plain_text, func, num_list, stage_mode)
# file = open('../output/stage.jpg', "wb")
# file.write(res)


# 测试nonebot 对战 命令文本触发
# plain_text = "全部图"
#
# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# # num_list = list(set([int(x) for x in plain_text[:-2]]))
# num_list.sort()
#
# # stage_mode = plain_text[-2:]
# rule_match = None
# contest_match = None
# res = get_stages_image(num_list, contest_match, rule_match)
# res.show()


# 测试新版随机武器
plain_text = "随机武器 泡 泡 泡 泡"
res = get_random_weapon_image(plain_text)
