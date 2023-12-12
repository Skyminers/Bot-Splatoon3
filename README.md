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
<a href="https://github.com/Tian-que/nonebot-adapter-kaiheila">
<img src="https://img.shields.io/badge/kook-Adapter-lightgrey?style=social&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAARWSURBVHhe7ZtPSBRRHMdnibWk2IgKDCzbKLoERnkoFkwkCYLykBTYpT1EBBEGHcIOWSzusuC1U4QgHgQPCdZJ8JSXQOgqRijWQQMR8SS5zVt/D3bnfd+/GWfHne0LH1hn3vzm+/vOODuO8xxT5f84j4ZXnaX8mlPa5ywxr2Q7mEZ2nOb8qrMMdlIfuN5ZD9SOnQprzmdYtA5hvVBbZnKT+4sK1TVuT9SeWnDjGEFtYsXyyHuRnQnulTM2v/Na3F6p7V2Vr/ZoYIyp+nZwF9TvV51/lqn9+F/4ZJSbL7p3TWhlI8B6Z0e/Hm5vw2KpYU9/zp4EcPRU9HQNYG869iQA91KyL0DedAQOIPdLNBIVF7qwRxWBA7ibF41EyfAq9ikjcAAnz4smOGNjYyWVMplM1fjR0VFagzU1NVU1HnHsDPYpI3AAyARnZ2eHrGNVjs1ms7RUrp6enqptZCCfMkINQCc+rr29nZaoVVlbxoEk9ikjUACvvosGKlFpc3OzPCaVStESvbz1Edey2KuMQAHceC4a4PT19ZFtrGKxWEokEvSTXslkEu7Hy4uv2KuMQAEcPCIa4MzOzpJ1rLa2NvqkV2trK9wHAvlUESgAZICj08bGBn1Sy/TCx0E+VUQWgImGhoZgbRmpFuxThe8Ann4RDXCam5upBf+amZmBtVXceo29qvAdwOV7ogHOwMAAteFPKysrsK6ONz+wVxW+A0gkRAOcxcVFasVe29vbsKYJyKcO3wEgA5wgQvVMQT517KsAmpqaYD0TTl/FPnX4CqD/g2iAk06nqR07dXd3w3qm3H+PverwFcDZ66IBzsjICLVkL1TPlLzln8EcXwEgA5ytrS1qx169vb2wpgnIpwl7HkBQoZomIJ8mWAfwblnceSVBNTg4COuquHQHezXBOoDbb0UDnM7OTmoDa3Jykj6phWqrePwJezXBOgD2yAmZYExMTFALWB0dHaWFhQX6Sa7x8XFYXwbyaYp1AMgARyc2xvQZgLe2CuTTlJoHwJienqYlcs3Pz1fVlpE8hH2aYhXAy2+iAY7uyK6vr1eNN1HleBmZJ9irKVYBsJ0hE4z+/n6yjZXL5arGFwoFWoPF7icqx8tgBwV5NcUqAHa6IROMubk5so7V0tIibKMSu6P0jkcgnzZYBYAMRA3yaYNVAIdPiAaixPa/QAirAHK/RRNRwm7KkE8brAJgtF4WjUQFuy1HHm2wDoCBzEQB8maLrwCuPNh9JugH1IgXtB0CebPFVwBBGPopNuwFbRcWNQ+AcTwtNl0J2iYsIgmAPb5CjTPOZcD4EIkmAJeLN8XmGQ8/4vFhwV6Rj+xFSRQAGhcabu/lyVBwZQ3ofBZxAHxyFVxZI9hbZpWgMWFRbp7JPRUa73V5t2dq//+EibLchY0zZUY2jc49LRp30hQX3ChGUJtqxfJM0B15r9yN4nRNsJs6y1X+dmjUydNesbumepg+X/bI7/C0cpx/vPzmF35E+o0AAAAASUVORK5CYII=" alt="kook">
</a>
<a href="https://github.com/nonebot/adapter-qq">
<img src="https://img.shields.io/badge/QQ-Adapter-lightgrey?style=social&logo=data:image/png;base64,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" alt="qq">
</a>
</p>

</div>


## 📖 介绍

- 一个基于nonebot2框架的splatoon3游戏日程查询插件,支持onebot11,onebot12,[telegram](https://github.com/nonebot/adapter-telegram)协议,[kook](https://github.com/Tian-que/nonebot-adapter-kaiheila)协议,[QQ官方bot](https://github.com/nonebot/adapter-qq)协议
- onebot12协议下支持QQ、QQ频道、QQ官方bot、TG、微信消息、微信公众号、KOOK 等[平台](https://onebot.dev/ecosystem.html)
- 全部查询图片,全部采用pillow精心绘制,图片效果可查看下面的[效果图](#效果图)
> 也可以邀请我目前做好的bot直接加入频道，[kook频道bot](https://www.kookapp.cn/app/oauth2/authorize?id=22230&permissions=4096&client_id=4Kn4ukf1To48rax8&redirect_uri=&scope=bot),[qq频道bot](https://qun.qq.com/qunpro/robot/share?robot_appid=102081168)

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


## ⚙️ 配置
插件访问了`splatoon3.ink`和`splatoonwiki.org`这两个网站,如果机器人所处环境不支持直接访问这两个网站

可以在 nonebot2 项目的`.env.prod`文件中添加下表中的代理地址配置项

| 配置项 | 必填 | 值类型 | 默认值 | 说明 |
|:------:|:----:|:---:|:---:|:--:|
| splatoon3_proxy_address | 否 | str | ""  | 代理地址，格式为 127.0.0.1:20171 |
| splatoon3_reply_mode | 否 | bool | False  | 指定回复模式，开启后将通过触发词的消息进行回复，默认为False |
| splatoon3_permit_private | 否 | bool | False  | 是否允许频道私聊触发，默认为False |
| splatoon3_permit_c2c | 否 | bool | False  | 是否允许qq私聊(c2c)触发，默认为False |
| splatoon3_permit_channel | 否 | bool | True  | 是否允许频道触发，默认为True |
| splatoon3_permit_group | 否 | bool | True  | 是否允许群聊(如qq群，tg群)触发，默认为True |
| splatoon3_permit_unknown_src | 否 | bool | False  | 是否允许未知来源触发，默认为False |
| splatoon3_sole_prefix | 否 | bool | False  | 限制消息触发前缀为/ |
| splatoon3_guild_owner_switch_push | 否 | bool | False  | 频道服务器拥有者是否允许开关主动推送功能(为False时仅允许管理员开启关闭) |

<details>
<summary>示例配置</summary>
  
```env
# splatoon3示例配置
splatoon3_proxy_address = "" #代理地址
splatoon3_reply_mode = False #指定回复模式
splatoon3_permit_private = False #是否允许频道私聊触发
splatoon3_permit_c2c = False #是否允许qq私聊(c2c)触发
splatoon3_permit_channel = True #是否允许频道触发
splatoon3_permit_group = True # 是否允许群聊(如qq群，tg群)触发
splatoon3_permit_unkown_src = False #是否允许未知来源触发
splatoon3_sole_prefix = False # 限制消息触发前缀为/
splatoon3_guild_owner_switch_push = False # 频道服务器拥有者是否允许开关主动推送功能(为False时仅允许管理员开启关闭)
```

</details>

## 🎉 使用
### 指令表
<details>
<summary>指令帮助手册</summary>

![help.png](images/help1.png)

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

![random_weapon.png](images/random_weapon.png)

</details>

## ✨喜欢的话就点个star✨吧，球球了QAQ

## ⏳ Star 趋势

[![Stargazers over time](https://starchart.cc/Skyminers/Bot-Splatoon3.svg)](https://starchart.cc/Skyminers/nonebot-plugin-splatoon3)
