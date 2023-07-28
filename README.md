<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-splatoon3

_✨ splatoon3游戏日程查询插件 ✨_

<p align="center">
<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/Skyminers/Bot-Splatoon3.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-splatoon3">
  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/nonebot-plugin-splatoon3">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-splatoon3">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-splatoon3.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">
<br />
<a href="https://onebot.dev/">
  <img src="https://img.shields.io/badge/OneBot-v11-black?style=social&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABABAMAAABYR2ztAAAAIVBMVEUAAAAAAAADAwMHBwceHh4UFBQNDQ0ZGRkoKCgvLy8iIiLWSdWYAAAAAXRSTlMAQObYZgAAAQVJREFUSMftlM0RgjAQhV+0ATYK6i1Xb+iMd0qgBEqgBEuwBOxU2QDKsjvojQPvkJ/ZL5sXkgWrFirK4MibYUdE3OR2nEpuKz1/q8CdNxNQgthZCXYVLjyoDQftaKuniHHWRnPh2GCUetR2/9HsMAXyUT4/3UHwtQT2AggSCGKeSAsFnxBIOuAggdh3AKTL7pDuCyABcMb0aQP7aM4AnAbc/wHwA5D2wDHTTe56gIIOUA/4YYV2e1sg713PXdZJAuncdZMAGkAukU9OAn40O849+0ornPwT93rphWF0mgAbauUrEOthlX8Zu7P5A6kZyKCJy75hhw1Mgr9RAUvX7A3csGqZegEdniCx30c3agAAAABJRU5ErkJggg==" alt="onebot">
</a>
<a href="https://onebot.dev/">
  <img src="https://img.shields.io/badge/OneBot-v12-black?style=social&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABABAMAAABYR2ztAAAAIVBMVEUAAAAAAAADAwMHBwceHh4UFBQNDQ0ZGRkoKCgvLy8iIiLWSdWYAAAAAXRSTlMAQObYZgAAAQVJREFUSMftlM0RgjAQhV+0ATYK6i1Xb+iMd0qgBEqgBEuwBOxU2QDKsjvojQPvkJ/ZL5sXkgWrFirK4MibYUdE3OR2nEpuKz1/q8CdNxNQgthZCXYVLjyoDQftaKuniHHWRnPh2GCUetR2/9HsMAXyUT4/3UHwtQT2AggSCGKeSAsFnxBIOuAggdh3AKTL7pDuCyABcMb0aQP7aM4AnAbc/wHwA5D2wDHTTe56gIIOUA/4YYV2e1sg713PXdZJAuncdZMAGkAukU9OAn40O849+0ornPwT93rphWF0mgAbauUrEOthlX8Zu7P5A6kZyKCJy75hhw1Mgr9RAUvX7A3csGqZegEdniCx30c3agAAAABJRU5ErkJggg==" alt="onebot">
</a>
<a href="https://github.com/nonebot/adapter-telegram">
<img src="https://img.shields.io/badge/telegram-Adapter-lightgrey?style=social&logo=telegram" alt="telegram">
</a>
</p>

</div>


## 📖 介绍

- 一个基于nonebot2框架的splatoon3游戏日程查询插件,支持onebot11,onebot12,[telegram](https://github.com/nonebot/adapter-telegram)协议
- onebot12协议下支持QQ、QQ频道、TG、微信消息、微信公众号、KOOK 等[平台](https://onebot.dev/ecosystem.html)
- 全部查询图片(除nso衣服查询外),全部采用pillow精心绘制,图片效果可查看下面的[效果图](#效果图)
> QQ 机器人 SplatBot 已搭载该插件，可以[点击这里](https://flawless-dew-f3c.notion.site/SplatBot-e91a70e4f32a4fffb640ce8c3ba9c664)查看qq机器人使用指南

## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-splatoon3

</details>


<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-splatoon3
</details>

<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-splatoon3
</details>

</details>



安装完成后，需要以超级管理员用户对机器人发送`更新武器数据`来更新数据库内的武器数据，不然`随机武器`功能无法使用

## ⚙️ 配置
插件访问了`splatoon3.ink`和`splatoonwiki.org`这两个网站,如果机器人所处环境不支持直接访问这两个网站

可以在 nonebot2 项目的`.env.prod`文件中添加下表中的代理地址配置项

| 配置项 | 必填 | 值类型 | 默认值 | 说明 |
|:------:|:----:|:---:|:---:|:--:|
| splatoon3_proxy_address | 否 | str | ""  | 代理地址，格式为 127.0.0.1:20171 |
| splatoon3_reply_mode | 否 | bool | False  | 指定回复模式，开启后将通过触发词的消息进行回复，默认为False |
| splatoon3_permit_private | 否 | bool | False  | 是否允许私聊触发，默认为False |
| splatoon3_permit_channel | 否 | bool | False  | 是否允许频道触发，默认为False |
| splatoon3_permit_unkown_src | 否 | bool | False  | 是否允许未知来源触发，默认为False |
| splatoon3_whitelist | 否 | List[str] | []  | 白名单列表，填写后黑名单无效，里面可以填写用户id，群id，频道id，如 ["10000","123456"]|
| splatoon3_blacklist | 否 | List[str] | []  | 黑名单列表，里面可以填写用户id，群id，频道id，如 ["10000","123456"]|

<details>
<summary>示例配置</summary>
  
```env
# splatoon3示例配置
splatoon3_proxy_address = "" #代理地址
splatoon3_reply_mode = False #指定回复模式
splatoon3_permit_private = False #是否允许私聊触发
splatoon3_permit_channel = False #是否允许频道触发
splatoon3_permit_unkown_src = False #是否允许未知来源触发
splatoon3_whitelist = [] #白名单列表，填写后黑名单无效，里面可以填写用户id，群id，频道id
splatoon3_blacklist = ["10000","123456"] #黑名单列表，填写后黑名单无效，里面可以填写用户id，群id，频道id
```

</details>

## 🎉 使用
### 指令表
<details>
<summary>指令帮助手册</summary>

![help.png](images/help.png)

</details>


### 效果图
<details>
<summary>对战查询</summary>

![stages.png](images/stages.png)

</details>
<details>
<summary>打工查询</summary>

![coop.png](images/coop.jpg)

</details>
<details>
<summary>活动</summary>

![events.png](images/events.png)

</details>
<details>
<summary>祭典</summary>

![festival.png](images/festival.png)

</details>
<details>
<summary>随机武器</summary>

![random_weapon.png](images/random_weapon.jpg)

</details>

## ✨喜欢的话就点个star✨吧，球球了QAQ
