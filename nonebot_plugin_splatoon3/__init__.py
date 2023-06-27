# from nonebot import on_command, on_regex
# from nonebot.adapters.onebot.v11 import MessageEvent
# from nonebot.adapters.onebot.v11 import MessageSegment
# from nonebot.matcher import Matcher
#
# from .image import get_save_temp_image, get_coop_stages_image, get_random_weapon, \
#     get_stages_image
#
# matcher_select_stage = on_regex('[0-9]+图', priority=10, block=True)
# matcher_select_stage_mode_rule = on_regex('[0-9]+(区域|推塔|蛤蜊|抢鱼|塔楼|鱼虎)(挑战|真格|开放|组排|排排|X段|x段)',
#                                           priority=10,
#                                           block=True)
# matcher_select_stage_mode = on_regex('[0-9]+(挑战|真格|开放|组排|排排|涂地|涂涂|X段|x段)', priority=10, block=True)
# matcher_select_all_mode_rule = on_regex('全部(区域|推塔|蛤蜊|抢鱼|塔楼|鱼虎)(挑战|真格|开放|组排|排排|X段|x段)',
#                                         priority=10,
#                                         block=True)
# matcher_select_all_mode = on_regex('全部(挑战|真格|开放|组排|排排|涂地|涂涂|X段|x段)', priority=10, block=True)
#
# matcher_coop = on_command('工', aliases={'打工', '鲑鱼跑', 'bigrun', "big run", '团队打工'}, priority=10, block=True)
# matcher_all_coop = on_command('全部工', aliases={'全部打工', '全部鲑鱼跑', '全部bigrun', "全部big run", '全部团队打工'},
#                               priority=10, block=True)
#
# matcher_stage_group = on_command('图', priority=10, block=True)
# matcher_stage_group2 = on_command('图图', priority=10, block=True)
# matcher_stage_next1 = on_command('下图', priority=10, block=True)
# matcher_stage_next12 = on_command('下图图', aliases={'下下图'}, priority=10, block=True)
# matcher_random_weapon = on_command('随机武器', priority=10, block=True)
#
# matcher_help = on_command('帮助', aliases={"help"}, priority=10, block=True)
#
#
# # 随机武器
# @matcher_random_weapon.handle()
# async def _(matcher: Matcher, event: MessageEvent):
#     plain_text = event.get_message().extract_plain_text().strip()
#     # 传递函数指针
#     func = get_random_weapon
#     # 获取图片
#     weapon1 = None
#     weapon2 = None
#     img = get_save_temp_image(plain_text, func, weapon1, weapon2)
#     # 发送消息
#     await matcher.finish(
#         MessageSegment.image(
#             file=img,
#             cache=False
#         )
#     )
#
#
# # 顺序 全部图 模式
# @matcher_select_all_mode.handle()
# async def _(matcher: Matcher, event: MessageEvent):
#     plain_text = event.get_message().extract_plain_text().strip()
#     # 传递函数指针
#     func = get_stages_image
#     # 获取图片
#     num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#     stage_mode = plain_text[-2:]
#     img = get_save_temp_image(plain_text, func, num_list, stage_mode)
#     # 发送消息
#     await matcher.finish(
#         MessageSegment.image(
#             file=img,
#             cache=False,
#         )
#     )
#
#
# # 顺序 全部图 模式 规则
# @matcher_select_all_mode_rule.handle()
# async def _(matcher: Matcher, event: MessageEvent):
#     plain_text = event.get_message().extract_plain_text().strip()
#     # 传递函数指针
#     func = get_stages_image
#     # 获取图片
#     num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#     stage_mode = plain_text[-4:]
#     img = get_save_temp_image(plain_text, func, num_list, stage_mode)
#     # 发送消息
#     await matcher.finish(
#         MessageSegment.image(
#             file=img,
#             cache=False,
#         )
#     )
#
#
# # 顺序  模式 规则
# @matcher_select_stage_mode_rule.handle()
# async def _(matcher: Matcher, event: MessageEvent):
#     plain_text = event.get_message().extract_plain_text().strip()
#     # 传递函数指针
#     func = get_stages_image
#     # 获取图片
#     num_list = list(set([int(x) for x in plain_text[:-4]]))
#     num_list.sort()
#     stage_mode = plain_text[-4:]
#     img = get_save_temp_image(plain_text, func, num_list, stage_mode)
#     # 发送消息
#     if img is None:
#         msg = '好像没有符合要求的地图模式>_<'
#         # else:
#         msg = MessageSegment.image(
#             file=img,
#             cache=False,
#         )
#     await matcher.finish(msg)
#
#
# # 顺序 图 模式
# @matcher_select_stage_mode.handle()
# async def _(matcher: Matcher, event: MessageEvent):
#     plain_text = event.get_message().extract_plain_text().strip()
#     # 传递函数指针
#     func = get_stages_image
#     # 获取图片
#     num_list = list(set([int(x) for x in plain_text[:-2]]))
#     num_list.sort()
#     stage_mode = plain_text[-2:]
#     img = get_save_temp_image(plain_text, func, num_list, stage_mode)
#     # 发送消息
#     if img is None:
#         msg = '好像没有符合要求的地图模式>_<'
#     else:
#         msg = MessageSegment.image(
#             file=img,
#             cache=False,
#         )
#     await matcher.finish(msg)
#
#
# # 顺序 图
# @matcher_select_stage.handle()
# async def _(matcher: Matcher, event: MessageEvent):
#     plain_text = event.get_message().extract_plain_text().strip()
#     # 传递函数指针
#     func = get_stages_image
#     # 获取图片
#     num_list = list(set([int(x) for x in event.get_message().extract_plain_text()[:-1]]))
#     num_list.sort()
#     stage_mode = None
#     img = get_save_temp_image(plain_text, func, num_list, stage_mode)
#     # 发送消息
#     await matcher.finish(
#         MessageSegment.image(
#             file=img,
#             cache=False,
#         )
#     )
#
#
# # 工
# @matcher_coop.handle()
# async def _(matcher: Matcher, event: MessageEvent):
#     plain_text = event.get_message().extract_plain_text().strip()
#     # 传递函数指针
#     func = get_coop_stages_image
#     # 获取图片
#     all = False
#     img = get_save_temp_image(plain_text, func, all)
#     # 发送消息
#     await matcher.finish(
#         MessageSegment.image(
#             file=img,
#             cache=False
#         )
#     )
#
#
# # 全部工
# @matcher_all_coop.handle()
# async def _(matcher: Matcher, event: MessageEvent):
#     plain_text = event.get_message().extract_plain_text().strip()
#     # 传递函数指针
#     func = get_coop_stages_image
#     # 获取图片
#     all = True
#     img = get_save_temp_image(plain_text, func, all)
#     # 发送消息
#     await matcher.finish(
#         MessageSegment.image(
#             file=img,
#             cache=False
#         )
#     )
#
#
# # 图
# @matcher_stage_group.handle()
# async def _(matcher: Matcher, event: MessageEvent):
#     plain_text = event.get_message().extract_plain_text().strip()
#     # 传递函数指针
#     func = get_stages_image
#     # 获取图片
#     num_list = [0]
#     num_list.sort()
#     stage_mode = None
#     img = get_save_temp_image(plain_text, func, num_list, stage_mode)
#     # 发送消息
#     await matcher.finish(
#         MessageSegment.image(
#             file=img,
#             cache=False,
#         )
#     )
#
#
# # 图图
# @matcher_stage_group2.handle()
# async def _(matcher: Matcher, event: MessageEvent):
#     plain_text = event.get_message().extract_plain_text().strip()
#     # 传递函数指针
#     func = get_stages_image
#     # 获取图片
#     num_list = [0, 1]
#     num_list.sort()
#     stage_mode = None
#     img = get_save_temp_image(plain_text, func, num_list, stage_mode)
#     # 发送消息
#     await matcher.finish(
#         MessageSegment.image(
#             file=img,
#             cache=False,
#         )
#     )
#
#
# # 下图
# @matcher_stage_next1.handle()
# async def _(matcher: Matcher, event: MessageEvent):
#     plain_text = event.get_message().extract_plain_text().strip()
#     # 传递函数指针
#     func = get_stages_image
#     # 获取图片
#     num_list = [1]
#     num_list.sort()
#     stage_mode = None
#     img = get_save_temp_image(plain_text, func, num_list, stage_mode)
#     # 发送消息
#     await matcher.finish(
#         MessageSegment.image(
#             file=img,
#             cache=False,
#         )
#     )
#
#
# # 下下图
# @matcher_stage_next12.handle()
# async def _(matcher: Matcher, event: MessageEvent):
#     plain_text = event.get_message().extract_plain_text().strip()
#     # 传递函数指针
#     func = get_stages_image
#     # 获取图片
#     num_list = [1, 2]
#     num_list.sort()
#     stage_mode = None
#     img = get_save_temp_image(plain_text, func, num_list, stage_mode)
#     # 发送消息
#     await matcher.finish(
#         MessageSegment.image(
#             file=img,
#             cache=False,
#         )
#     )
#
#
# # 帮助菜单
# @matcher_help.handle()
# async def _(matcher: Matcher, event: MessageEvent):
#     plain_text = event.get_message().extract_plain_text().strip()
#     # 传递函数指针
#     func = get_random_weapon
#     # 获取图片
#     weapon1 = None
#     weapon2 = None
#     img = get_save_temp_image(plain_text, func, weapon1, weapon2)
#     # 发送消息
#     await matcher.finish(
#         MessageSegment.image(
#             file=img,
#             cache=False
#         )
#     )
