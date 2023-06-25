import csv
import os
import sqlite3
from pathlib import Path
from typing import Union

DATABASE = Path(os.path.join(os.path.dirname(__file__), "data", "image"))


class ImageManager:
    _has_init = False

    def __init__(self):
        if not ImageManager._has_init:
            if not DATABASE.exists():
                DATABASE.mkdir(parents=True)
                self.database_path = DATABASE / "image.db"
                self.conn = sqlite3.connect(self.database_path)
                self._create_table()
            else:
                self.database_path = DATABASE / "image.db"
                self.conn = sqlite3.connect(self.database_path)
            print("nonebot_plugin_splatoon3:图片数据库连接！")

    # 关闭数据库
    def close(self):
        self.conn.close()
        print("nonebot_plugin_splatoon3:图片数据库关闭")

    # 创建表
    def _create_table(self):
        c = self.conn.cursor()
        c.execute("""CREATE TABLE IMAGE_DATA(
                    id INTEGER PRIMARY KEY AUTOINCREMENT ,
                    image_name Char(30) UNIQUE,
                    image_data BLOB,
                    image_zh_name Char(30)
                );""")
        self.conn.commit()

    # 添加或修改
    def add_or_modify(self, image_name: str, image_data, image_zh_name: str):
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
    def get_info(self, image_name) -> []:
        sql = f"select image_data,image_zh_name from IMAGE_DATA where image_name=?"
        c = self.conn.cursor()
        c.execute(sql, (image_name,))
        data = c.fetchone()
        self.conn.commit()
        return data
