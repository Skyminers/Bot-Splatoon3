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
<img src="https://img.shields.io/badge/kook-Adapter-lightgrey?style=social&logo=data:image/x-icon;base64,AAABAAEAAAAAAAEAIABdHAAAFgAAAIlQTkcNChoKAAAADUlIRFIAAAEAAAABAAgGAAAAXHKoZgAAHCRJREFUeNrt3XmQldW57/Hv2j3RdNPQdCOTiAh9EQwIAUXuzYkJxyhYB9B4YiIKDic3yRUKGSKTw1WLElqwASNWkXgSpdSkFE0CKT3JydV4YiJC8GgMRAbBjsEw9AA0zYYe9rp/bBoa6GGP69nv+z6fqq5Cunu/v7XlffZa77vetQwe9hNLl4O1lBnLUCxDIzDUQB+gW8uXbfmzJVs6r/IQQxNQZ6COVl8WDoRgJ4ad1rCzdzG77zaclI6beDM9ZNkRLqOZCcbyVSzjrWEglpB0LhVghoiBvwF/tIa3yOLNxT3YKx0r9vgZrMKS31DDZCwTLUzAMlA6k1KdMlQaeDNk+HV2TzbOM4SlI7UfNcNYi1lxhC9Hmplh4V+xFElnUiphhmMGNoSyWH9/D/7LGKx0pHPjZYjVx+kdDjMTwwz9pFe+ZKjEsj4/n7VzCjkoHScaSdiT1QxotNyP5dsW8qXzKJVuBsIYns0xrJhfwmfCWWRUHGVIQwOLMMywlhzJN0EpCcbQiGV9bi7L53Vnj0gG1wdcayk8XsMjEct9emtOKcDQFDKsKezJIzMNx90e2qFl1XwDyyos/V0eVylPMOzHMHdxCa+4O6QDTxylLNLIWmv5mquGKeVVxvCfoRxmLujO7rQfK90HKK/iTmtZa6Eg3cdSyi8M1BvDzIWlPJ/m46THOkvX2mrWWstd6WyAUn5mDM8VlzDzu4YTaXn9dLzo8mqusJaXsQxP79ujVAAYdhjDrYtK2J7ql075PPryw0yxEbboya9UiliG2whbyg8zJdUvndICsKyae6zhNaCrszdHqWDoag2vlVfzb6l80ZQVgPIqFhPh360ly/17o5T/WUtWJMKz5VUsTtVrJn0NwFpMeTWrrOU+2bdHqQAxPLWohDnJPlyU9Ew8PfmVEmCZvbwaILlzL6khQHkVi/XkV0qIZXayw4GEhwDLqrmHCP8u/R4oFXShEN9eWJLYuZhQASg/zBRreE0v+CklzxiajeXrC3uxMe7fjfcXlldzhY2wBb3Vp1QmOWFCXB3vZKG4rgGss3S1lpfRk1+pTNPVWl5eZ+M7N+MqADXVPKMz/JTKUJbhNdU8E8+vxFwAyqu4E8ud0m1USnXAcmd5VeznaUzXAJ44SllzAx+gXX+lvOBEVi6jYllPIKYeQKSRtejJr5RXdD19znaq0wKwvJpbdSUfpbzFWr62vJpbO/u5DocAay2Fx6r5WNfwU8qDDPuLSri8o4VGO+wB1FXxqJ78SnmUpX9dFY929CPt9gAqjjLkVCN/1aW7lfIwQ1NeDsPa23eg3R5AQwOL9ORXyuMs2Q0NLGrv2232AE5v1/WJ7tijlPcZQ2OOYXBb25C12QNosCzQk18pf7CWnAbLgra+d0EPYPVxep8Ms0836lTKPwyEu+Qz6PxdiS/oAZw8ySw9+ZXyFwv5J08y6/y/P6cAWIuxMF06rFIq9SxMt/bcXv85BWB5FddiGSgdVCmVBpaBy6u4tvVfnVMAjNFPf6X87Pxz/Ex3oMKSf6qaA1iKpEMqpdLEcCyvhD7zDGFo1QNoqmGKnvxK+ZylqKnm7BZjZwpAxDJROptSKv1an+tnCoCFr0oHU0qlX+tzPQSw7AiX6dV/pQLCMnDZES6Dlh5AMxOkMymlHDp9zkcLQEQLgFKBEmlVAIxhvHQepZQ7Lee8+Ymly4Fq6rHJbRSqlPIQQ6RPCQWhg7WU6cmvVMBYQgdrKQsZy1DpLEop94xlaAgtAEoFk2VoKIIWAKWCKAJDQ0Bf6SBKKRF9s4Fu0ikyyT+2w8/nSadQmaSgFKavh1CWdJKU66YF4DyfbobP3pdOoTLNtp/CVXdIp0i5biEDhdIpMome/Kotvy2HxrB0itQyUBiy2gM4x9+1AKg2HDsA76yTTpFaFrqF0AJwxsk6OLwn+ddR/vT2U1BfI50ipbqFdPuvs/TTX3XkVB28VSGdIoUs2ToFuBUd/6vObP4x1P5NOkXqaAFoRQuA6kxzI/zmcekUqaMFoJW//7d0AuUFH7wKn/9ZOkVqaAE47ejnUHcw+ddRwfDGY9IJUkMLwGna/Vfx2PN29MvrtACcpncAVLxefxSslU6RHC0Ap2kPQMXrHx/Bh69Jp0iOFgCiVXz/h9IplBf95nFoapBOkTgtAMChXXDquHQK5UW1f4vODfAqnQWI+/G/MYbnnnuO7GyZt3/79u08/nhyN7N79erFihUryMnJEWnD5s2b+cEPfiBy7PO9VQFjp0EXD+6sqQUA9+P/YcOGMWPGDLH2rlmzJqnfz8/PZ9OmTYwbN06sDR9//LHYsc93ojb6nMAND0oniZ8OAXA/Aejqq68Wbe+WLVsS/t1QKMRLL70kevIn24Z0eGdd9IlBrwl8AWg6FV0FyCUvF4BVq1Zx0003ieZPtg3p0HQS/rNcOkX8Al8APv8IIk1ujylZAGpqatizJ7FnnufOncvs2bPFsrfYvXs3tbW10jEusO0lOF4lnSI+gS8Arsf/eXl5jBw5Uqy9W7duTej3brnlFlauXCmWu7VM+/RvkZ0HXYulU8RHC8A2t8cbPXq02JVzSOzkGT9+PC+88AKhUGb8c8nUAtD/Su8tHJoZ/0cFub4A6LWLZ2VlZWzcuJEuXbqI5k6mDa4M+KJ0gvgFugCEj0D1PrfH9NIFwNLSUl5//XVKS0tFM7fW2NjIBx98IB2jTVoAPEZi/r9kAaisrOTQoUMx/WzLvf4hQ4aI5W3Ln//8Z06ePCkdo00XawHwFtcFoLi4mMGDB4u1N9ZP/1AoxIsvvsg111wjljXZNrhWUALFA6RTxC/QBUBiApAxRqy9sZ48FRUV3HzzzWI5U9EG1waMkU6QGC0ADnlh/D9nzhzuu+8+0ZzJtkHCxaOlEyQmsAWg9jM4ftjtMSULQHNzM9u2dXzP8+tf/zpPPvmkWMbO1NXVZdQzAK158QIgBLgASKwAdNVVV4m1d/v27dTX17f7/WuuuSaj7vW3Ze3atUQiEekYbdIegMe4vgA4cOBAevfuLdbejrrOQ4YMYdOmTeTn54vl68wrr7zCkiVLpGO0qWSQ92YAtghuAdDxPxC91//GG29k1L3+8/3hD39gxowZ2AxdgM+rn/4Q0AIQibhf1z0TC0CXLl3YuHFjxt3rb23Xrl1MnTo1Y+/9g3fH/xDQAnDoY2ioT/514iFZAE6cOMH27ec+8xwKhXjhhRcYP368WK7OHD58mBtvvJHq6mrpKB3y4gSgFoEsAK7H/1lZWYwZI3ej+P3336ep6dxnnleuXMktt9wilqkz4XCYyZMn88knn0hH6VAoG/qNkE6RRH7pABJc3/8fPnw4BQUFYu09v/s/e/Zs5s6dK5anM5FIhGnTpvHee+9JR+lUn+GQkznPScUtkAXAdQ8gk8b/N910E6tWrRLN05m5c+fyi1/8QjpGTAZ4+AIgBLAANIbh4F/dHjNTCsC4ceN46aWXMvpef0VFBU899ZR0jJh5efwPASwA+z+ESLPbY0quAVBVVcW+ffsYPHhwxt/rf/XVV7n//vulY8TFq88AtAhcAXDd/c/Pz+eKK64Qa++WLVsoKSnhjTfeoFevXmI5OvPuu+9yxx13ZOxMv7bkFkCvMukUyQlcAXB9AXDMmDFiG4BA9Pn5jRs3UlaWuf9S9+zZw5QpUzL6Xn9bLh4FGTyaikngNgYJ2gXAGTNm0K9fP9EMHamqqmLixIlUVXlsOV28PQGohcfrV3zqq6N7ubkkXQAy+eQPh8NMmTIl4+/1t8frFwAhYAUgaEuAZbJIJMIdd9zBu+++Kx0lYdoD8BjX4//S0lIGDRok3eyMNH/+fF577TXpGAkrvAi6Z27nKmaBKgBBG/9nqtWrV7N69WrpGEnxw6c/BKwABG0JsEz085//nPnz50vHSJoWAI+p+RRO1Lg9phaAc23evJnbb7/dU/f626MFwGMkLgBKLgGWaT755BOmTJlCOByWjpIS/UdJJ0iN4BQAx93/yy67LKNX2XGpurqaSZMmcfiw41VY06R0MOR3l06RGoEpAK4XAdXuf9TJkyeZMmUKu3fvlo6SMn7p/kNACkBzE+wP2BJgmcBay/Tp0/njH/8oHSWl/DABqEUgCsDBv0KT42nmWgDg+9//Phs2bJCOkXLaA/AY1xcAs7Oz+eIXffSvJAFPP/00FRUV0jFSLisH+so93JlyWgDSYMSIERn93H26/fKXv8zo7cWS0fcLkJ0nnSJ1AlEA9AKgO1u2bGHatGm+uNffFj91/yEABaChHg7tcnvMoBaAvXv3MnnyZE6cOCEdJW38dAEQAlAA/v4BWMcfRkEsADU1NUyaNIlDhw5JR0kr7QF4jOv5/wUFBQwbNky62U6dOnWKqVOnsmuX466WY3ndopOA/MT3BcD1BcCxY8eSlZUl3WxnrLXMmDGDd955RzpK2g0YDcZIp0gtLQApFrTu/4IFC3j55ZelYzjht/E/+LwA1B2Co/vdHjNIBeCZZ55h5cqV0jGc8dv4H3xeAFyP/yE4BWDTpk3Mnj1bOoZTXt4GvD2+LgCuu/+9e/fmkksukW522m3dupVvfetbNDc73mFFUFFfKOojnSL1fF0AdAJQ6u3bt8/39/rb4sfuP/i9AOgSYClVW1vLjTfeyMGDB6WjOKcFwGOqPoHwUbfH9HMBaLnX//HHH0tHEeHHOwDg4wLgegUgY4xvlwCz1nLXXXfx+9//XjqKCGOi24D5kW8LgOvx/5AhQyguLpZudlo8/PDD/OxnP5OOIaZXGeQVSqdID98WgM+2uT2en7v/PXr0kI4gyq/df/BpAWhuhH9sd3vMcePGSTc7bWbNmhWI25vtGTBGOkH6+LIA/GM7NJ1ye0w/9wDy8vJYunSpdAwxA3w4AaiFLwuA6wlAOTk5jBo1SrrZaXX77bczcuRI6RjOZedBn+HSKdLHlwXA9QXAK6+8krw8H60T1YZQKER5ebl0DOf6jYiuA+hXviwA+gRgekycOJEJEyZIx3DKzxcAwYcF4GQdVO1xe8ygFACA8vJyjN8eiu+AX2cAtvBdAdj/AVjr9phBKgBjx47lm9/8pnQMZ/z4BGBrvisArrv/RUVFDB06VLrZTi1dupScHB8PjE/L7wGll0mnSC8tAEkaO3YsoZDv3sYODR48mO9973vSMdLO75/+4MMCoI8Au/HQQw/RrVs36Rhp5ffxP/isABw7EP1yKagFoFevXixYsEA6RlppD8BjXHf/IbgFAGDu3Ln07dtXOkbaaA/AY1x3//v160f//v2lmy2moKCARx55RDpGWvS4GAp7SadIP18VAJ0A5N4999zjy7sgQfj0Bx8VAGuj24C5pAUguhX6smXLpGOknN9nALbwTQE4vBtO1bk9phaAqJtvvpnx48dLx0gpPz8B2JpvCoDr7r+flwBLxBNPPCEdIWVMCPpfKZ3CDd8UANcXAC+//HKKiorE2mtdz3fuxJe+9CWmTp0qHSMlel8OuQXSKdzwTQEI2gXAioqKjCsCy5Yt88XGqEEZ/4NPCkDTKTiww+0xpQvAunXrePHFF0UznG/YsGHcfffd0jGSFpTxP/ikAHz+l+g6gC5JFoDa2lp2797NQw89RENDg1iOtjz66KN07dpVOkZSgnILEHxSAFyP//Py8kSXx9q6dSsAn376KU8//bRYjrb069ePOXPmSMdIWE4+XHS5dAp3fFEAXI//R40aRW5urlh7t2zZcubPjz/+OEePOt4CqRMLFy6kpKREOkZC+o2ErGzpFO74ogAEbQ/A995778yfq6urWb58uWie8xUVFfHggw9Kx0hIkLr/4IMCED4a3QfQJekC0DIEaLFmzRr2798vmul89957L4MGDZKOEbcgPAHYmucLgOtPf5AtAJWVlRfszhsOh3n44YfFMrUlNzfXk3sJaA/AY1yP/3v06EFZWZlYe1uP/1t7/vnn2bHD8b3QTtx2222MHu2dj9SuPaHnQOkUbnm+ALi+A3DVVVeJrorbXgFobm5m4cKFYrnaYozx1BThoH36gw8KgOttwKXH/+0VAIBf/epXGbeF93XXXcf1118vHSMmQRv/g8cLwJH9cPyQ22NKFoDm5ma2bet42+NMXKbLK3sJaA/AY1x3/0G2AOzYsYP6+voOf2bz5s28+uqrYhnbMmrUKKZNmyYdo1NBegaghacLwN+2Jf8a8RgwYAB9+vQRa29H3f/WlixZQlNTk1jOtixdulR08lRneg6Egp7SKdzzdAFwfQtw3Lhxou2NtQDs2rWLH/3oR6JZz3fppZcyc+ZM6RjtGjBGOoEMzxaASAT2f+j2mJl8AfB8jz32WKfDBdceeOABsrMzc55tEC8AgocLwKGd0OD437dkAQiHw/zlL3+J+ecPHDjAk08+KZa3LadOncq4oUmLIF4ABA8XANcXAEOhEGPGyPUT33///bhPnpUrV3LokOPbJB2IpwfjUigL+o2QTiHUdukAiXI9A3D48OEUFhaKtTeRk6euro7HHntMLHMq2uBC7+HRx4CDyLsFQCcAxeSHP/whe/bsEc2ebBvSLUgrAJ3PkwWgMQwHA7YEWKInT2NjI0uWLBHNDtFFTP/0pz9Jx2hTUMf/4NEC8PlHEGl2e0zJAlBVVcXevXsT/v0NGzZc8Aixazt37sy4hUtaBHECUAtPFgDX4//8/HxGjJC7SpRs19laKz5FOFO7/7kFcJH/djaLmScLgOsJQKNHjxa9f52Kk+d3v/sdr7/+uqfbkA79r4SQJ8+C1PBk04O2B0CqTp5FixYRiUQ83YZUC+oEoBaeKwD1NVDzqdtjSheAVI3fP/roI9avX+88f0NDAx9+6HjaZoyCfAEQIDPnZXZAYgmwt99+m127dom0t76+nqqqqpS93oMPPkhlZaXTNhw+fDjj9i9oEfQCYJYdJrP2l+rE/1sBv/XOIjMqgxX2ggcyaxU15zw3BHA9AUj5V9DH/+DBAiCxCIjyp6B3/8FjBeDYAaivlk6h/CKoawC05qkCUNQHLh0vnUL5xcWjpBPI81QBAJj0f6UTKD8oHQz5PaRTyPNcAbhkDHxhsnQK5XV6ATDKcwUA4IYHoos4KJUovQAY5ckCUDoYrpounUJ5WZCfAGzNkwUA4J/vjz7JpVS8QtnQ7wvSKTKDZwtAt4vgn+6VTqG8qO8VkJ0nnSIzeLYAQLQAFJRKp1Beo+P/szxdAPIKo0MBpeKh4/+zPF0AAK6eDiWDpFMoL9EewFmeLwBZOdHbgkrFIq8QepVJp8gcni8AACOm6sQOFZv+o8ADO5U744sCADpFWMVGu//n8k0BuOx/wdCvSadQmU4LwLl8UwAAJj6k3TvVMb0DcC5fFYA+w2D0N6VTqExV1Ae695VOkVl8VQAAvrZIZ3mptumn/4V8VwB69If/+b+lU6hMpOP/C3luWfBYfGUO/OlFCB+RTuKGzbB1nTP1OowWgAt5bllwdaGdv4XnbpNOEfU//hnu/pl0ChUr3w0BgmjoddHboJlAP2W9RQuAT0zMkIlQOiPTW7QA+MSA0TDyJukUWgC8RguAj1y/JLrajZTiS6BQ12fwFC0APlIyCMbdKXd8Hf97jxYAn5kwX26tRO3+e08IQ5N0CJU6hb3gy7Nkjq09AI8xNIWAOukcKrX+6f9A4UVuj2lC0G+kdMtVnOpCRguA7+QWwHUL3B6z9zDI7SrdchUPA3XaA/CpsbdHN1BxRbv/nqQFwK+ysuGGB90db4BeAPQiLQB+9oV/gQFj3BxLH7X1pLqQhQPSKVT6uFgrMacr9L5cuqUqXhYOhEKwUzqISp9B42HYDek9Rv+RuluzF4VgZwijBcDvbngoepsuXXQCkEcZdoasFgDf6z0UxqRxvQC9A+BN1rAz1LuY3Rgi0mFUel23ELK7pOe1tQB4kCHSu5jdobsNJ42lUjqPSq/ufeFL30396xaURJ8CVN5iLJV3G05GR4aGd6UDqfS7djZ0LU7ta+rtP486fc6HAKzhLek8Kv26FMFX56X2NXUCkDe1nPPRHkAWb0oHUm5ccw/0GJC619MegEedPudDAIt7sBej1wGCIDs3unJQqugFQA8yVC7uwV5otSCIQXsBQTHqFug7IvnX6Xlp6q8pqPRrfa6fKQAhw6+lgyk3jIFJDyf/Ovrp71GG/2j545kCkN2TjRiOSWdTbpR9BYZcm9xr6AxADzIcy+3Jppb/PLOG7DxDeHkVGyzcI51RuTHpYfjpdxL//UuvkW6BipeBDfMM4Vb/fdYTtVzb3MTvpEMqpdIjK5uvLCjm7Zb/PqcAWItZXs0+LAOlgyqlUsxQuaiEQcac3Q/0nGfEjMFiWS+dUymVBpb1rU9+aGNfgPx81hrOjhGUUt5nIJyfz9rz//6CAjCnkIMYnpUOrJRKIcOzcwo5eP5ft7lMRI5hhTE0SmdWSiXPGBpzDCva+l6bBWB+CZ/ptQClfMKyfn4Jn7X1rXYXisrNZbluG6aUxxmacnNZ3t632y0A87qzJ2RYI51fKZW4kGHNvO7saff7Hf1yYU8ewbBfuhFKqQQY9hf25JGOfqTDAjDTcBzDXOl2KKUSYJg703C84x+JwbIqfo3leun2KKViZPjN4lI63REiptXis3KYZaBeuk1Kqc4ZqM/KYVYsPxtTAVjQnd0Y7pVumFIqBoZ7F3Rndyw/GvN+MYtKWW8Mz0m3TSnVPmN4blFp7HN44towqriEmRh2SDdSKdUGw47iEmbG8ytxFYDvGk7kGL4BnJBuq1LqHCeM4dbvmvjOzbi3jPx+CTtCcJsxNEu3WCkFxtAcgtsWlbA93t9NaM/Yhb3YaA1JLCallEoVa/jOwl5sTOR3E940enEJPzaGxdKNVyrIQoYli0v4caK/H9NEoI4sr2K1tdwn/UYoFTTGsGZRKXOSeY2EewAtFpYw1+hDQ0o5ZQxrFpYkP00/6QJgDHZRKXN0OKCUGyHDktPnnE32tZIeArS2rJp7jOWH1pIl9/Yo5U/G0GwN30lmzH/Ba6Y6ZPlhpkTgp0BXp++OUv52IgS3JXq1vz0pLwAAK6sZ3mh5BctwN++NUj5m2GEMtyZyn7/zl06TdZautdWstZa70vrmKOVjxvBccQkz453hF/Prp7sBy6uYgeUZCwXpPpZSfmGgHsO98TzYk+Bx0q/iKENONbJWFxVRKgaG32TlMCvWR3qTO5RDy6r5BpZVWPq7PK5SnmDYj2Hu4hJecXdIx9ZaCo/X8EjEch/27PbkSgWWoSlkWFPYk0c6W8Mv9YcWUnGUIQ0NLLKG6VhypXIoJcUYGo3l+ZxcyjtaujutGaTfhCerGdBouR/Lty3kS+dRKt0MhDE8m2NY0d6OPQ6zZIbVx+kdDjMTwwwsA6XzKJVyhkos6/PzWdvWRp0ykTKMtZgVR/hypJkZFv4VS5F0JqUSZjhmYEMoi/X39+C/UjF/P7XxMliFJb+hhslYJlqYoD0D5QmGSgNvYviP3J5smmcIS0dqP6qHrDjCoEgzE6xlApbx1jAQm/wTjUolzBAxlkoM7xrDm5Es3lrcg73SsWKP72E/sXQ5WEuZsQzFMjQCQw30Abq1fNmWP+stRxWP6M7YdQbqaPVl4UAIdmLYaQ07exez+27DSem4ifr/B/yJ8tbd3IIAAAAASUVORK5CYII=" alt="telegram">
</a>
</p>

</div>


## 📖 介绍

- 一个基于nonebot2框架的splatoon3游戏日程查询插件,支持onebot11,onebot12,[telegram](https://github.com/nonebot/adapter-telegram)协议,[kook](https://github.com/Tian-que/nonebot-adapter-kaiheila)协议
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

![random_weapon.png](images/random_weapon.png)

</details>

## ✨喜欢的话就点个star✨吧，球球了QAQ

## ⏳ Star 趋势

[![Stargazers over time](https://starchart.cc/Skyminers/Bot-Splatoon3.svg)](https://starchart.cc/Skyminers/nonebot-plugin-splatoon3)
