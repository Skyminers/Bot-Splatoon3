from nonebot.log import logger

try:
    from .onebotv11_matcher import *
except ImportError as e:
    logger.error(
        "No OneBot adapter found, you can try 'nb adapter install nonebot-adapter-onebot' to install. \n"
        "If not, you can still use the plugin, but it will not respond to OneBot messages."
    )

try:
    from .telegram_matcher import *
except ImportError as e:
    logger.error(
        "No Telegram adapter found, you can try 'nb adapter install nonebot-adapter-telegram' to install. \n"
        "If not, you can still use the plugin, but it will not respond to Telegram messages."
    )
