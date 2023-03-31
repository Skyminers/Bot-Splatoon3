# import nonebot
import random
import re
import time

from nonebot import get_driver
from nonebot import on_command, on_regex, on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Event
from nonebot.adapters.onebot.v11 import Bot
from nonebot.adapters.onebot.v11.message import MessageSegment
from nonebot import require
from .config import Config
from .data_source import *
from .utils import *
from .imageProcesser import *

global_config = get_driver().config
config = Config(**global_config.dict())
# Response

matcher_select_stage = on_regex('[0-9]+图')
matcher_select_stage_mode_rule = on_regex('[0-9]+(区域|推塔|蛤蜊|抢鱼)(挑战|开放|X段|x段)')
matcher_select_stage_mode = on_regex('[0-9]+(挑战|开放|涂地|X段|x段)')
matcher_select_all_mode_rule = on_regex('全部(区域|推塔|蛤蜊|抢鱼)(挑战|开放|X段|x段)')
matcher_select_all_mode = on_regex('全部(挑战|开放|涂地|X段|x段)')
matcher_coop = on_command('工')
matcher_all_coop = on_command('全部工')
matcher_stage_group = on_command('图')
matcher_stage_group2 = on_command('图图')
matcher_stage_next1 = on_command('下图')
matcher_stage_next12 = on_command('下图图')
matcher_random_weapon = on_command('随机武器')

@matcher_random_weapon.handle()
async def _(bot: Bot, event: Event):
    await matcher_random_weapon.send(
        MessageSegment.image(
            file=get_random_weapon(),
            cache=False
        )
    )

@matcher_select_all_mode.handle()
async def _(bot: Bot, event: Event):
    plain_text = event.get_message().extract_plain_text()
    msg = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    img = get_stage_info(msg, stage_mode=plain_text[-2:])
    await matcher_select_all_mode.send(
        MessageSegment.image(
            file=img,
            cache=False,
        )
    )


@matcher_select_all_mode_rule.handle()
async def _(bot: Bot, event: Event):
    plain_text = event.get_message().extract_plain_text()
    msg = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    img = get_stage_info(msg, stage_mode=plain_text[-4:])
    await matcher_select_all_mode_rule.send(
        MessageSegment.image(
            file=img,
            cache=False,
        )
    )


@matcher_select_stage_mode_rule.handle()
async def _(bot: Bot, event: Event):
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
    await matcher_select_stage_mode_rule.send(msg)


@matcher_select_stage_mode.handle()
async def _(bot: Bot, event: Event):
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
    await matcher_select_stage_mode.send(msg)


@matcher_select_stage.handle()
async def _(bot: Bot, event: Event):
    msg = list(set([int(x) for x in event.get_message().extract_plain_text()[:-1]]))
    msg.sort()
    img = get_stage_info(msg)
    await matcher_select_stage.send(
        MessageSegment.image(
            file=img,
            cache=False,
        )
    )


@matcher_coop.handle()
async def _(bot: Bot, event: Event):
    res = get_coop_info(all=False)
    await matcher_coop.send(
        MessageSegment.image(
            # file=draw_text_image(res, mode='coop'),
            file=res,
            cache=False
        )
    )

@matcher_all_coop.handle()
async def _(bot: Bot, event: Event):
    res = get_coop_info(all=True)
    await matcher_all_coop.send(
        MessageSegment.image(
            file=res,
            cache=False
        )
    )


@matcher_stage_group.handle()
async def _(bot: Bot, event: Event):
    img = get_stage_info()
    await matcher_stage_group.send(
        MessageSegment.image(
            file=img,
            cache=False,
        )
    )

@matcher_stage_group2.handle()
async def _(bot: Bot, event: Event):
    img = get_stage_info([0, 1])
    await matcher_stage_group2.send(
        MessageSegment.image(
            file=img,
            cache=False,
        )
    )


@matcher_stage_next1.handle()
async def _(bot: Bot, event: Event):
    args = str(event.get_message()).strip()
    img = get_stage_info([1])
    await matcher_stage_next1.send(
        MessageSegment.image(
            file=img,
            cache=False,
        )
    )


@matcher_stage_next12.handle()
async def _(bot: Bot, event: Event):
    args = str(event.get_message()).strip()
    img = get_stage_info([1, 2])
    await matcher_stage_next12.send(
        MessageSegment.image(
            file=img,
            cache=False,
        )
    )
