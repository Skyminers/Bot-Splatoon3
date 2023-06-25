import json
import httpx

from .utils import get_time_ymd

# 翻译字典
trans_dict = {
    'LOFT': '真格塔楼',
    'CLAM': '真格蛤蜊',
    'GOAL': '真格鱼虎',
    'AREA': '真格区域',
    'TURF_WAR': '占地对战'
}

# 鲑鱼跑模式
list_salmonrun_mode = ['一般打工', '团队打工', '大型跑']

trans_res = None
# trans_res = {'stages': {'VnNTdGFnZS0x': {'name': '温泉花大峡谷'}, 'VnNTdGFnZS0y': {'name': '鳗鲶区'}, 'VnNTdGFnZS0z': {'name': '烟管鱼市场'}, 'VnNTdGFnZS00': {'name': '竹蛏疏洪道'}, 'VnNTdGFnZS02': {'name': '鱼肉碎金属'}, 'VnNTdGFnZS0xMA==': {'name': '真鲭跨海大桥'}, 'VnNTdGFnZS0xMQ==': {'name': '金眼鲷美术馆'}, 'VnNTdGFnZS0xMg==': {'name': '鬼头刀SPA度假区'}, 'VnNTdGFnZS0xMw==': {'name': '海女美术大学'}, 'VnNTdGFnZS0xNA==': {'name': '鲟鱼造船厂'}, 'VnNTdGFnZS0xNQ==': {'name': '座头购物中心'}, 'VnNTdGFnZS0xNg==': {'name': '醋饭海洋世界'}, 'Q29vcFN0YWdlLTc=': {'name': '麦年海洋发电所'}, 'Q29vcFN0YWdlLTE=': {'name': '鲑坝'}, 'Q29vcFN0YWdlLTI=': {'name': '新卷堡'}, 'Q29vcFN0YWdlLTY=': {'name': '漂浮落难船'}, 'VnNTdGFnZS03': {'name': '臭鱼干温泉'}, 'VnNTdGFnZS05': {'name': '比目鱼住宅区'}, 'Q29vcFN0YWdlLTEwMA==': {'name': '醋饭海洋世界'}, 'Q29vcFN0YWdlLS05OTk=': {'name': ''}, 'VnNTdGFnZS01': {'name': '鱼露遗迹'}, 'VnNTdGFnZS0xOA==': {'name': '鬼蝠鲼玛利亚号'}, 'Q29vcFN0YWdlLTEwMg==': {'name': '海女美术大学'}, 'VnNTdGFnZS04': {'name': '塔拉波特购物公园'}, 'VnNTdGFnZS0xNw==': {'name': '昆布赛道'} }}
trans_res_save_ymd: str
# trans_res_save_ymd = "22222"

# 取翻译数据
def get_trans_data():
    global trans_res
    global trans_res_save_ymd
    if trans_res is None or check_expire_trans(trans_res_save_ymd):
        print('nonebot_plugin_splatoon3: 重新请求:翻译文本')
        with httpx.Client() as client:
            result = client.get('https://splatoon3.ink/data/locale/zh-CN.json')
            trans_res = json.load(result)
            # 刷新储存时 时间
            trans_res_save_ymd = get_time_ymd()
            return trans_res
    else:
        return trans_res


# 校验过期翻译 记录每日ydm，不同则为false，使其每日刷新一次
def check_expire_trans(trans_res_save_ymd):
    now_ymd = get_time_ymd()
    if now_ymd != trans_res_save_ymd:
        return True
    return False


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


# 用现有翻译字典对游戏模式进行翻译
def get_trans_game_mode(text):
    if text in trans_dict:
        return trans_dict[text]
    return text
