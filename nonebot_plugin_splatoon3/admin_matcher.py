import re

from nonebot import on_regex
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.matcher import Matcher
from nonebot.permission import SUPERUSER

from .static_data_getter import reload_weapon_info
from .image_db import imageDB

matcher_admin = on_regex("^[\\\/\.。]?(重载武器数据|更新武器数据|清空图片缓存)$", priority=10, block=True, permission=SUPERUSER)


# 重载武器数据，包括：武器图片，副武器图片，大招图片，武器配置信息
@matcher_admin.handle()
async def _(matcher: Matcher, event: MessageEvent):
    plain_text = event.get_message().extract_plain_text().strip()
    err_msg = "执行失败，错误日志为: "
    # 清空图片缓存
    if re.search("^清空图片缓存$", plain_text):
        msg = "数据库合成图片缓存数据已清空！"
        try:
            imageDB.clean_image_temp()
        except Exception as e:
            msg = err_msg + str(e)
        # 发送消息
        await matcher.finish(MessageSegment.text(msg))
    elif re.search("^(重载武器数据|更新武器数据)$", plain_text):
        msg_start = "将开始重新爬取武器数据，此过程可能需要10min左右,请稍等..."
        msg = "武器数据更新完成"
        await matcher.send(MessageSegment.text(msg_start))
        try:
            reload_weapon_info()
        except Exception as e:
            msg = err_msg + str(e) + "\n如果错误信息是timed out，不妨可以等会儿重新发送指令"
        await matcher.finish(MessageSegment.text(msg))
