# SSR/SS链接解码
基于python
使用库：base64,sys

运行方法：python ssr_link_decode.py （SSR或者SS链接）

即能输出各项参数

如：python ssr_link_decode.py ss://YWVzLTI1Ni1jZmI6Uk1PU2dGNDljYnFRQDE3Mi4xMDQuMTIyLjEwOTozOTMzMA==


其他python调用：

只需import ssr_link_decode

并调用ssr_link_decode或者ss_link_decode函数即可

参数均为SS或SSR链接字符串，返回值均为一个dict
