import requests
from bs4 import BeautifulSoup
from nonebot.log import logger

from .imageProcesser import imageDB, get_file_url
from .utils import WeaponData, ImageInfo
from .translation import (
    dict_weapon_sub_trans,
    dict_weapon_special_trans,
    dict_weapon_trans,
)

weapon_url = "https://splatoonwiki.org/wiki/List_of_weapons_in_Splatoon_3"


# 爬取wiki数据 来重载武器数据，包括：武器图片，副武器图片，大招图片，武器配置信息
def reload_weapon_info():
    global weapon_url
    response = requests.get(weapon_url)
    soup = BeautifulSoup(response.text, "html.parser")
    # 通过 selector 找到 Weapon list
    weapon_list = iter(
        soup.select_one("#mw-content-text > div > div > table > tbody").find_all("tr")
    )
    # 跳过表头
    next(weapon_list)
    for weapon_info in weapon_list:
        # (image_td, name_td, id_td, sub_td, special_td, special_points_td, level_pd, price_td, class_pd)
        # 筛选掉用作分隔符的偶数下标元素
        weapon_info = [
            weapon_info.contents[i]
            for i in range(len(weapon_info.contents))
            if i % 2 == 1
        ]
        weapon_data = WeaponData(
            name=weapon_info[1].contents[0].text,
            sub_name=weapon_info[3].contents[2].text,
            special_name=weapon_info[4].contents[2].text,
            special_points=int(weapon_info[5].contents[0].text),
            level=int(weapon_info[6].text),
            weapon_class=weapon_info[8].contents[2].text,
            zh_name="None",
            zh_sub_name="None",
            zh_special_name="None",
        )
        if weapon_data.name in dict_weapon_trans:
            weapon_data.zh_name = dict_weapon_trans[weapon_data.name]
        if weapon_data.sub_name in dict_weapon_sub_trans:
            weapon_data.zh_sub_name = dict_weapon_sub_trans[weapon_data.sub_name]
        if weapon_data.special_name in dict_weapon_special_trans:
            weapon_data.zh_special_name = dict_weapon_special_trans[
                weapon_data.special_name
            ]
        # 数据库新增 装备信息
        imageDB.add_or_modify_weapon_info(weapon_data)
        # 数据库新增 装备图片
        names = [
            weapon_data.name,
            weapon_data.sub_name,
            weapon_data.special_name,
            weapon_data.weapon_class,
        ]
        type_names = ["main", "sub", "special", "class"]
        ids = [0, 3, 4, 8]
        for i in range(4):
            # 主武器图片、副武器图片、大招图片、类型图片
            push_weapon_images(
                ImageInfo(
                    name=names[i],
                    url="https:"
                    + weapon_info[ids[i]].contents[0].contents[0].attrs["src"],
                    source_type=type_names[i],
                    zh_name=None,  # 多余项忽略
                )
            )


# 向数据库新增 武器图片 二进制文件
def push_weapon_images(img: ImageInfo):
    res = imageDB.get_weapon_image(img.name, img.source_type)
    if not res:
        image_data = get_file_url(img.url)
        if len(image_data) != 0:
            logger.info("[ImageDB] new weapon image {}".format(img.name))
            imageDB.add_or_modify_weapon_images(
                img.name,
                img.source_type,
                image_data,
            )


if __name__ == "__main__":
    reload_weapon_info()
