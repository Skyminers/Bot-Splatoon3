import re
from nonebot import on_regex
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.matcher import Matcher
from nonebot.log import logger
from nonebot.plugin import PluginMetadata

from .image import *
from .image_processer_tools import image_to_base64
from .translation import dict_keyword_replace
from .image_db import imageDB
from .utils import multiple_replace
from .data_source import get_screenshot
from .admin_matcher import matcher_admin

__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-splatoon3",
    description="一个基于nonebot2框架的splatoon3游戏日程查询插件",
    usage="发送 帮助 help 可查看详细指令\n",
    type="application",
    # 发布必填，当前有效类型有：`library`（为其他插件编写提供功能），`application`（向机器人用户提供功能）。
    homepage="https://github.com/Skyminers/Bot-Splatoon3",
    # 发布必填。
    supported_adapters={"~onebot.v11"},
)

# 初始化插件时清空合成图片缓存表
imageDB.clean_image_temp()

# 图 触发器  正则内需要涵盖所有的同义词
matcher_stage_group = on_regex("^[\\\/\.。]?[0-9]*(全部)?下*图+$", priority=10, block=True)

# 对战 触发器
matcher_stage = on_regex(
    "^[\\\/\.。]?[0-9]*(全部)?下*(区域|推塔|抢塔|塔楼|蛤蜊|抢鱼|鱼虎|涂地|涂涂|挑战|真格|开放|组排|排排|pp|PP|X段|x段|X赛|x赛){1,2}$",
    priority=10,
    block=True,
)

# 打工 触发器
matcher_coop = on_regex(
    "^[\\\/\.。]?(全部)?(工|打工|鲑鱼跑|bigrun|big run|团队打工)$",
    priority=10,
    block=True,
)

# 其他命令 触发器
matcher_else = on_regex("^[\\\/\.。]?(帮助|help|(随机武器).*|装备|衣服|祭典|活动)$", priority=10, block=True)


# 图 触发器处理 二次判断正则前，已经进行了同义词替换，二次正则只需要判断最终词
@matcher_stage_group.handle()
async def _(matcher: Matcher, event: MessageEvent):
    plain_text = event.get_message().extract_plain_text().strip()
    # 触发关键词  同义文本替换
    plain_text = multiple_replace(plain_text, dict_keyword_replace)
    logger.info("同义文本替换后触发词为:" + plain_text + "\n")
    # 判断是否满足进一步正则
    num_list = []
    contest_match = None
    rule_match = None
    flag_match = False
    # 顺序 单图
    if re.search("^[0-9]+图$", plain_text):
        num_list = list(set([int(x) for x in plain_text[:-1]]))
        num_list.sort()
        flag_match = True
    elif re.search("^下{1,11}图$", plain_text):
        re_list = re.findall("下", plain_text)
        num_list = list(set([len(re_list)]))
        num_list.sort()
        flag_match = True
    # 多图
    elif re.search("^下?图{1,11}$", plain_text):
        re_list = re.findall("图", plain_text)
        lens = len(re_list)
        # 渲染太慢了，限制查询数量
        if lens > 5:
            lens = 5
        num_list = list(set([x for x in range(lens)]))
        num_list.sort()
        if "下" in plain_text:
            num_list.pop(0)
        flag_match = True
    elif re.search("^全部图*$", plain_text):
        # 渲染太慢了，限制查询数量
        num_list = [0, 1, 2, 3, 4, 5]
        flag_match = True
    # 如果有匹配
    if flag_match:
        # 传递函数指针
        func = get_stages_image
        # 获取图片
        img = get_save_temp_image(plain_text, func, num_list, contest_match, rule_match)
        # 发送消息
        await matcher.finish(
            MessageSegment.image(
                file=img,
                cache=False,
            )
        )


# 对战 触发器处理
@matcher_stage.handle()
async def _(matcher: Matcher, event: MessageEvent):
    plain_text = event.get_message().extract_plain_text().strip()
    # 触发关键词  同义文本替换  同时替换.。\/ 等前缀触发词
    plain_text = multiple_replace(plain_text, dict_keyword_replace)
    logger.info("同义文本替换后触发词为:" + plain_text)
    # 判断是否满足进一步正则
    num_list = []
    contest_match = None
    rule_match = None
    flag_match = False
    # 双筛选  规则  竞赛
    if re.search("^[0-9]*(全部)?(区域|蛤蜊|塔楼|鱼虎)(挑战|开放|X段)$", plain_text):
        if "全部" in plain_text:
            num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        else:
            if len(plain_text) == 2:
                num_list = [0]
            else:
                num_list = list(set([int(x) for x in plain_text[:-4]]))
                num_list.sort()
        stage_mode = plain_text[-4:]
        contest_match = stage_mode[2:]
        rule_match = stage_mode[:2]
        flag_match = True
    # 双筛选  竞赛  规则
    elif re.search("^[0-9]*(全部)?(挑战|开放|X段)(区域|蛤蜊|塔楼|鱼虎)$", plain_text):
        if "全部" in plain_text:
            num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        else:
            if len(plain_text) == 2:
                num_list = [0]
            else:
                num_list = list(set([int(x) for x in plain_text[:-4]]))
                num_list.sort()
        stage_mode = plain_text[-4:]
        contest_match = stage_mode[:2]
        rule_match = stage_mode[2:]
        flag_match = True
    # 单筛选  竞赛
    elif re.search("^[0-9]*(全部)?(挑战|开放|X段|涂地)$", plain_text):
        if "全部" in plain_text:
            num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        else:
            if len(plain_text) == 2:
                num_list = [0]
            else:
                num_list = list(set([int(x) for x in plain_text[:-2]]))
                num_list.sort()

        stage_mode = plain_text[-2:]
        contest_match = stage_mode
        rule_match = None
        flag_match = True
    # 单筛选 下 竞赛
    elif re.search("^下{1,11}(挑战|开放|X段|涂地)$", plain_text):
        re_list = re.findall("下", plain_text)
        lens = len(re_list)
        num_list = list(set([lens]))
        num_list.sort()
        stage_mode = plain_text[-2:]
        contest_match = stage_mode
        rule_match = None
        flag_match = True
    # 单筛选  模式
    elif re.search("^[0-9]*(全部)?(区域|蛤蜊|塔楼|鱼虎)$", plain_text):
        if "全部" in plain_text:
            num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        else:
            if len(plain_text) == 2:
                num_list = [0]
            else:
                num_list = list(set([int(x) for x in plain_text[:-2]]))
                num_list.sort()
        stage_mode = plain_text[-2:]
        rule_match = stage_mode
        contest_match = None
        flag_match = True
    # 单筛选 下 模式
    elif re.search("^下{1,11}(区域|蛤蜊|塔楼|鱼虎)$", plain_text):
        re_list = re.findall("下", plain_text)
        lens = len(re_list)
        num_list = list(set([lens]))
        stage_mode = plain_text[-2:]
        contest_match = None
        rule_match = stage_mode
        flag_match = True

    # 如果有匹配
    if flag_match:
        # 传递函数指针
        func = get_stages_image
        # 获取图片
        img = get_save_temp_image(plain_text, func, num_list, contest_match, rule_match)
        # 发送消息
        await matcher.finish(
            MessageSegment.image(
                file=img,
                cache=False,
            )
        )


# 打工 触发器处理
@matcher_coop.handle()
async def _(matcher: Matcher, event: MessageEvent):
    plain_text = event.get_message().extract_plain_text().strip()
    # 触发关键词  同义文本替换
    plain_text = multiple_replace(plain_text, dict_keyword_replace)
    logger.info("同义文本替换后触发词为:" + plain_text + "\n")
    # 判断是否满足进一步正则
    _all = False
    if "全部" in plain_text:
        _all = True
    # 传递函数指针
    func = get_coop_stages_image
    # 获取图片
    img = get_save_temp_image(plain_text, func, _all)
    # 发送消息
    await matcher.finish(
        MessageSegment.image(
            file=img,
            cache=False,
        )
    )


# 其他命令 触发器处理
@matcher_else.handle()
async def _(matcher: Matcher, event: MessageEvent):
    plain_text = event.get_message().extract_plain_text().strip()
    # 触发关键词  同义文本替换
    plain_text = multiple_replace(plain_text, dict_keyword_replace)
    logger.info("同义文本替换后触发词为:" + plain_text + "\n")
    # 判断是否满足进一步正则
    # 随机武器
    if re.search("^随机武器.*$", plain_text):
        # 这个功能不能进行缓存，必须实时生成图
        # 测试数据库能否取到武器数据
        if not get_weapon_info_test():
            msg = "请机器人管理员先发送 更新武器数据 更新本地武器数据库后，才能使用随机武器功能"
            await matcher.finish(MessageSegment.text(msg))
        else:
            img = image_to_base64(get_random_weapon_image(plain_text))
            # 发送消息
            await matcher.finish(MessageSegment.image(file=img, cache=False))
    elif re.search("^祭典$", plain_text):
        # 传递函数指针
        func = get_festival_image
        # 获取图片
        img = get_save_temp_image(plain_text, func)
        if img is None:
            msg = "近期没有任何祭典"
            msgm = MessageSegment.text(msg)
        else:
            # 发送图片
            msgm = MessageSegment.image(file=img, cache=False)
        await matcher.finish(msgm)
    elif re.search("^活动$", plain_text):
        # 传递函数指针
        func = get_events_image
        # 获取图片
        img = get_save_temp_image(plain_text, func)
        if img is None:
            msg = "近期没有任何活动比赛"
            msgm = MessageSegment.text(msg)
        else:
            # 发送图片
            msgm = MessageSegment.image(file=img, cache=False)
        await matcher.finish(msgm)
    elif re.search("^帮助$", plain_text):
        # 传递函数指针
        func = get_help_image
        # 获取图片
        img = get_save_temp_image(plain_text, func)
        # 发送图片
        msgm = MessageSegment.image(file=img, cache=False)
        await matcher.finish(msgm)
    elif re.search("^装备$", plain_text):
        img = await get_screenshot(shot_url="https://splatoon3.ink/gear")
        await matcher.finish(MessageSegment.image(file=img, cache=False))
