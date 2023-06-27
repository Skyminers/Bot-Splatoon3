import csv
import os
import sqlite3
from pathlib import Path
from typing import Union

DATABASE_path = Path(os.path.join(os.path.dirname(__file__), "data", "image"))
DATABASE=Path(DATABASE_path,"image.db")

class ImageManager:
    _has_init = False

    def __init__(self):
        if not ImageManager._has_init:
            if not DATABASE_path.exists():
                DATABASE.mkdir(parents=True)
            if not DATABASE.exists():
                self.database_path = DATABASE
                self.conn = sqlite3.connect(self.database_path)
                self._create_table()
            else:
                self.database_path = DATABASE
                self.conn = sqlite3.connect(self.database_path)
            print("nonebot_plugin_splatoon3: 图片数据库连接！")

    # 关闭数据库
    def close(self):
        self.conn.close()
        print("nonebot_plugin_splatoon3: 图片数据库关闭")

    # 创建表
    def _create_table(self):
        c = self.conn.cursor()
        c.execute("""CREATE TABLE IMAGE_DATA(
                    id INTEGER PRIMARY KEY AUTOINCREMENT ,
                    image_name Char(30) UNIQUE,
                    image_data BLOB,
                    image_zh_name Char(30)
                );""")
        # 一次只能执行一条sql语句
        c.execute("""CREATE TABLE IMAGE_TEMP(
                    id INTEGER PRIMARY KEY AUTOINCREMENT ,
                    trigger_word Char(30) UNIQUE,
                    image_data BLOB,
                    image_expire_time TEXT
                );""")
        self.conn.commit()

    # 添加或修改 图片数据表
    def add_or_modify_IMAGE_DATA(self, image_name: str, image_data, image_zh_name: str):
        sql = f"select * from IMAGE_DATA where image_name=?"
        c = self.conn.cursor()
        c.execute(sql, (image_name,))
        data = c.fetchone()
        if not data:  # create user
            sql = f"INSERT INTO IMAGE_DATA (image_data, image_zh_name,image_name) VALUES (?, ?, ?);"
        else:
            sql = f"UPDATE IMAGE_DATA set image_data=?,image_zh_name=? where image_name=?"
            image_name = data[0]

        c.execute(sql, (image_data,image_zh_name, image_name))
        self.conn.commit()

    # 取图片信息(图片二进制数据)
    # return value: visible_fc, visible_card, fc_code, card
    def get_img_data(self, image_name) -> []:
        sql = f"select image_data,image_zh_name from IMAGE_DATA where image_name=?"
        c = self.conn.cursor()
        c.execute(sql, (image_name,))
        data = c.fetchone()
        self.conn.commit()
        return data

    # 添加或修改 图片缓存表
    def add_or_modify_IMAGE_TEMP(self, trigger_word: str, image_data, image_expire_time: str):
        sql = f"select * from IMAGE_TEMP where trigger_word=?"
        c = self.conn.cursor()
        c.execute(sql, (trigger_word,))
        data = c.fetchone()
        if not data:  # create user
            sql = f"INSERT INTO IMAGE_TEMP ( image_data,image_expire_time,trigger_word) VALUES (?, ?, ?);"
        else:
            sql = f"UPDATE IMAGE_TEMP set image_data=?,image_expire_time=? where trigger_word=?"
            image_name = data[0]

        c.execute(sql, (image_data,image_expire_time, trigger_word))
        self.conn.commit()

    # 取图片缓存(图片二进制数据)
    # return value: visible_fc, visible_card, fc_code, card
    def get_img_temp(self, trigger_word) -> []:
        sql = f"select image_data,image_expire_time from IMAGE_TEMP where trigger_word=?"
        c = self.conn.cursor()
        c.execute(sql, (trigger_word,))
        data = c.fetchone()
        self.conn.commit()
        return data