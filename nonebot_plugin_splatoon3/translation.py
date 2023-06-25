import json
import httpx

from .utils import get_time_ymd

trans_res = None
trans_res_save_ymd = None


# 取翻译数据
def get_trans():
    global trans_res
    global trans_res_save_ymd
    if trans_res is None or check_expire_trans(trans_res_save_ymd):
        print('重新请求:翻译文本')
        with httpx.Client() as client:
            result = client.get('https://splatoon3.ink/data/locale/zh-CN.json')
            trans_res = json.load(result)
            return trans_res
    else:
        # 刷新储存时 时间
        trans_res_save_ymd = get_time_ymd()
        return trans_res


# 校验过期翻译 记录每日ydm，不同则为false，使其每日刷新一次
def check_expire_trans(trans_res_save_ymd):
    now_ymd = get_time_ymd()
    if now_ymd != trans_res_save_ymd:
        return False
    return True


# 获取地图翻译名
def get_trans_stage(id: str):
    global trans_res
    zh_name = trans_res['stages'][id]['name']
    if zh_name == '':
        return '未取得翻译名称'
    return zh_name


# 获取武器翻译名
def get_trans_weapon(id: str):
    global trans_res
    zh_name = trans_res['weapons'][id]['name']
    if zh_name == '':
        return '未取得翻译名称'
    return zh_name
