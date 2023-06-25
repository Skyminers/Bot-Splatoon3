import datetime

from .data_source import get_coop_info, get_stage_info
from .imageProcesser import get_coop_stages, imageManager, image_to_base64, get_stages

from PIL import Image
import io


# 从数据库新增或读取图片二进制  缓存图片
def get_save_temp_image(trigger_word, func, *args):
    res = imageManager.get_img_temp(trigger_word)
    time_now_str = datetime.datetime.now().strftime("%Y-%m-%dT%H").strip()
    image: bytes
    if not res:
        # 重新生成图片并写入
        image_data = func(*args)
        image = image_to_base64(image_data)
        if len(image) != 0:
            print('nonebot_plugin_splatoon3: [ImageManager] new temp image {}'.format(trigger_word))
            imageManager.add_or_modify_IMAGE_TEMP(trigger_word, image, time_now_str)
        return image
    else:
        # 判断时间是否过期
        time_str = res[1]
        if time_now_str != time_str:
            # 重新生成图片并写入
            image_data = func(*args)
            image = image_to_base64(image_data)
            if len(image) != 0:
                print('nonebot_plugin_splatoon3: [ImageManager] update temp image {}'.format(trigger_word))
                imageManager.add_or_modify_IMAGE_TEMP(trigger_word, image, time_now_str)
            return image
        print('nonebot_plugin_splatoon3: 数据库内存在时效范围内的缓存图片，将从数据库读取缓存图片')
        return image_to_base64(Image.open(io.BytesIO(res[0])))


# 取 打工图片
def get_coop_stages_image(*args):
    all = args[0]
    # 获取数据
    stage, weapon, time, boss, mode = get_coop_info(all)
    # 绘制图片
    image = get_coop_stages(stage, weapon, time, boss, mode)
    return image


# 取 对战图片
def get_stages_image(*args):
    num_list = args[0]
    stage_mode = args[1]
    # 获取数据
    schedule, new_num_list, contest_match, rule_match = get_stage_info(num_list, stage_mode)
    # 绘制图片
    image = get_stages(schedule, new_num_list, contest_match, rule_match)
    return image


# 取 随机武器图片
def get_random_weapon(*args):
    weapon1 = args[0]
    weapon2 = args[1]
    # 绘制图片
    image = get_random_weapon(weapon1, weapon2)
    return image
