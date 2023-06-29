import json
import httpx

from .utils import get_time_ymd

# 翻译字典
dict_trans = {
    "LOFT": "真格塔楼",
    "CLAM": "真格蛤蜊",
    "GOAL": "真格鱼虎",
    "AREA": "真格区域",
    "TURF_WAR": "占地对战",
}

# 鲑鱼跑模式
list_salmonrun_mode = ["一般打工", "团队打工", "大型跑"]

trans_res = None
trans_res_save_ymd: str


# 取翻译数据
def get_trans_data():
    global trans_res
    global trans_res_save_ymd
    if trans_res is None or check_expire_trans(trans_res_save_ymd):
        print("nonebot_plugin_splatoon3: 重新请求:翻译文本")
        with httpx.Client() as client:
            result = client.get("https://splatoon3.ink/data/locale/zh-CN.json")
            trans_res = json.load(result)
            # 刷新储存时 时间
            trans_res_save_ymd = get_time_ymd()
            return trans_res
    else:
        return trans_res


# 校验过期翻译 记录每日ymd，不同则为false，使其每日刷新一次
def check_expire_trans(trans_res_save_ymd):
    now_ymd = get_time_ymd()
    if now_ymd != trans_res_save_ymd:
        return True
    return False


# 获取地图翻译名
def get_trans_stage(id: str):
    global trans_res
    zh_name = trans_res["stages"][id]["name"]
    if zh_name == "":
        return "未取得翻译名称"
    return zh_name


# 获取武器翻译名
def get_trans_weapon(id: str):
    global trans_res
    zh_name = trans_res["weapons"][id]["name"]
    if zh_name == "":
        return "未取得翻译名称"
    return zh_name


# 用现有翻译字典对游戏模式进行翻译
def get_trans_game_mode(text):
    if text in dict_trans:
        return dict_trans[text]
    return text
