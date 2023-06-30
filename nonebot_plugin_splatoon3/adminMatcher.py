import re

from nonebot import on_command, on_regex
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.matcher import Matcher
from nonebot.log import logger
from nonebot.permission import SUPERUSER

from .staticDataGetter import reload_weapon_info
from .imageProcesser import imageDB

matcher_admin = on_regex(
    "^[\\\/\.。]?(重载武器数据|清空图片缓存)$", priority=10, block=True, permission=SUPERUSER
)


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
    elif re.search("^重载武器数据$", plain_text):
        msg = "武器数据重载成功"
        try:
            reload_weapon_info()
        except Exception as e:
            msg = err_msg + str(e)
        await matcher.finish(MessageSegment.text(msg))
