# Splatoon 3 地图查询插件

> QQ 机器人 SplatBot 已搭载该插件，可以[点击这里](https://flawless-dew-f3c.notion.site/SplatBot-e91a70e4f32a4fffb640ce8c3ba9c664)查看使用指南

## 说明
- 本插件为适配[nonebot2框架](https://github.com/nonebot/nonebot2)的机器人插件,nonebot2框架具体安装方式可自行搜索，推荐环境为gocq+nonebot2
- 本插件的命令都不需要触发前缀，同时也兼容`/`，`\ `,`.`,`。`这些触发前缀
- 除随机武器和祭典，活动等截图实现的功能外，其他功能的查询图片都会自动在对战规则的2h时段内缓存，缓存有效期内的图片无需重新生成，大大省去绘图时间

## 已实现功能
![help.png](images/help.png)

## 安装指南
### 手动安装

```shell
git clone https://github.com/Skyminers/Bot-Splatoon3.git

pip install -r requirements.txt
```

在 nonebot2 框架中，将本仓库代码内的`nonebot_plugin_splatoon3`文件夹置于插件目录(`src/plugins`)即可正常加载，
之后对机器人发送`更新武器数据`来更新数据库内的武器数据，不然`随机武器`功能无法使用

