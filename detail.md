# Technical detail

## General form
- 6W1H


## Component
### Raspberry pi
- what: 一个功能齐全的微型电脑
- why: 与更轻量的arduino开发板和更重量的pc对比： 太轻量的arduino无法完成我们的需求，即没有足够的RAM来运行软件，无法进行图像处理，没有提供可操作的terminal;相比于pc，pc性能严重过剩，且有成本过高，可移动性过差的缺点，作为演示的原型机也不方便。
### LCD
- what: 我不记得了，组长补充
- why:可以调用更底层的方法实现需求，而不用额外开发驱动，节省开发成本

### Webcam:

### Servo motor

### Selfmade Car model

## System

### Hotspot
- what: 连接树莓派的主要方式是网线连接和智能设备连接树莓派开启的热点
- why: 相比于让树莓派连接热点的方式，树莓派开启热点能更加方便让智能设备连接。

## Further Improvement

### DBUI
#### 提升空间
- 拥有公有ip地址
拥有公有ipv4地址就可以做到真正的远程连接，控制DB而不是现在的wireless

- 安全性
1 DBUI app本身缺乏多账号系统和权限管理，目前只依靠树莓派的用户系统保证安全
2 当多用户同时访问数据库时，数据安全也无法保证，目前只是通过数据库本身的策略来运行



