from nonebot import on_command, on_regex
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.matcher import Matcher

from .data_source import *
from .utils import *
from .imageProcesser import *

matcher_select_stage = on_regex('[0-9]+图')
matcher_select_stage_mode_rule = on_regex('[0-9]+(区域|推塔|蛤蜊|抢鱼)(挑战|开放|X段|x段)')
matcher_select_stage_mode = on_regex('[0-9]+(挑战|开放|涂地|X段|x段)')
matcher_select_all_mode_rule = on_regex('全部(区域|推塔|蛤蜊|抢鱼)(挑战|开放|X段|x段)')
matcher_select_all_mode = on_regex('全部(挑战|开放|涂地|X段|x段)')

matcher_coop = on_command('工', priority=10, block=True)
matcher_all_coop = on_command('全部工', priority=10, block=True)

matcher_stage_group = on_command('图', priority=10, block=True)
matcher_stage_group2 = on_command('图图', priority=10, block=True)
matcher_stage_next1 = on_command('下图', priority=10, block=True)
matcher_stage_next12 = on_command('下图图', priority=10, block=True)
matcher_random_weapon = on_command('随机武器', priority=10, block=True)


# 随机武器
@matcher_random_weapon.handle()
async def _(matcher: Matcher, event: MessageEvent):
    await matcher.finish(
        MessageSegment.image(
            file=get_random_weapon(),
            cache=False
        )
    )


# 顺序 全部图 模式
@matcher_select_all_mode.handle()
async def _(matcher: Matcher, event: MessageEvent):
    plain_text = event.get_message().extract_plain_text()
    msg = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    img = get_stage_info(msg, stage_mode=plain_text[-2:])
    await matcher.finish(
        MessageSegment.image(
            file=img,
            cache=False,
        )
    )


# 顺序 全部图 模式 规则
@matcher_select_all_mode_rule.handle()
async def _(matcher: Matcher, event: MessageEvent):
    plain_text = event.get_message().extract_plain_text()
    msg = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    img = get_stage_info(msg, stage_mode=plain_text[-4:])
    await matcher.finish(
        MessageSegment.image(
            file=img,
            cache=False,
        )
    )


# 顺序  模式 规则
@matcher_select_stage_mode_rule.handle()
async def _(matcher: Matcher, event: MessageEvent):
    plain_text = event.get_message().extract_plain_text()
    msg = list(set([int(x) for x in plain_text[:-4]]))
    msg.sort()
    img = get_stage_info(msg, stage_mode=plain_text[-4:])
    if img is None:
        msg = '好像没有符合要求的地图模式>_<'
    else:
        msg = MessageSegment.image(
            file=img,
            cache=False,
        )
    await matcher.finish(msg)


# 顺序 图 模式
@matcher_select_stage_mode.handle()
async def _(matcher: Matcher, event: MessageEvent):
    plain_text = event.get_message().extract_plain_text()
    msg = list(set([int(x) for x in plain_text[:-2]]))
    msg.sort()
    img = get_stage_info(msg, stage_mode=plain_text[-2:])
    if img is None:
        msg = '好像没有符合要求的地图模式>_<'
    else:
        msg = MessageSegment.image(
            file=img,
            cache=False,
        )
    await matcher.finish(msg)


# 顺序 图
@matcher_select_stage.handle()
async def _(matcher: Matcher, event: MessageEvent):
    msg = list(set([int(x) for x in event.get_message().extract_plain_text()[:-1]]))
    msg.sort()
    img = get_stage_info(msg)
    await matcher.finish(
        MessageSegment.image(
            file=img,
            cache=False,
        )
    )


# 工
@matcher_coop.handle()
async def _(matcher: Matcher, event: MessageEvent):
    res = get_coop_info()
    await matcher.finish(
        MessageSegment.image(
            # file=draw_text_image(res, mode='coop'),
            file=res,
            cache=False
        )
    )


# 全部工
@matcher_all_coop.handle()
async def _(matcher: Matcher, event: MessageEvent):
    res = get_coop_info(all=True)
    await matcher.finish(
        MessageSegment.image(
            file=res,
            cache=False
        )
    )


# 图
@matcher_stage_group.handle()
async def _(matcher: Matcher, event: MessageEvent):
    img = get_stage_info()
    await matcher.finish(
        MessageSegment.image(
            file=img,
            cache=False,
        )
    )


# 图图
@matcher_stage_group2.handle()
async def _(matcher: Matcher, event: MessageEvent):
    img = get_stage_info([0, 1])
    await matcher.finish(
        MessageSegment.image(
            file=img,
            cache=False,
        )
    )


# 下图
@matcher_stage_next1.handle()
async def _(matcher: Matcher, event: MessageEvent):
    args = str(event.get_message()).strip()
    img = get_stage_info([1])
    await matcher.finish(
        MessageSegment.image(
            file=img,
            cache=False,
        )
    )


# 下下图
@matcher_stage_next12.handle()
async def _(matcher: Matcher, event: MessageEvent):
    args = str(event.get_message()).strip()
    img = get_stage_info([1, 2])
    await matcher.finish(
        MessageSegment.image(
            file=img,
            cache=False,
        )
    )
