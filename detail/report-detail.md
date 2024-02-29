# Technical detail for report

### Introduction

可以分析我们如何想到这个项目的（literary review）即分析现有项目的缺陷，然后提出我们这个项目.(从目标群体，软硬件开销的角度)

### Materials and Methods
项目流程: 需求分析 -> 软件设计 -> 软件开发 -> 硬件部署 -> 项目测试

需求分析： 根据requirement.md 随便拉细节逻辑扯扯


#### 软件相关
##### 软件开发使用的工具
软件设计:  使用Markdown文档和mermaid（这是用来做流程图的语言）设计UML类图和状态机状态流程图，并使用git进行版本迭代的版本管理，github进行代码托管和多人合作。

代码架构： UML类图是software_structure.pdf 上半部分，下半部分是状态机流程图，可以截图选取用，也可以让我把他们分开拆成两个pdf。
类图解释： UML（统一建模语言（你可以查查定义掰扯一嘴））

git 不只是架构设计的版本管理，本项目所有代码都由git进行版本管理，并且使用github来远程托管代码实现多人协同开发。部分git log graph请看图片



#### 软件架构解释
本项目根据面向对象（OOP）的设计函数，以及状态机来实现业务逻辑切换（可以扯扯定义，比如面向对象的三原则封装，继承，多态，在本项目也有所实现。本身状态机也是由多态来实现的）。本项目有两个独立的application（或者程序），所以分开两个来讲述：

##### gate app部分
这是项目的主要程序，是项目主要的业务逻辑在这个程序里。根据类图GateApp类有一个公开的类函数run（）和exit（）用来执行程序和退出程序释放资源（关闭摄像头，结束与数据库的连接等）， 同时GateApp储存着从外部输入的Gate，VehicleIdReader，DataBaseManager对象，在GateApp类初始化的时候作为参数传入进该对象。这样做的好处是在GateApp之外初始化其聚合(aggregation)(aggregation describe a 'Has a' relationship) 的对象，因此可以自行决定传入哪一种对象，降低了程序的耦合性，方便了程序进行模块单元测试。

由上文可知，GateApp聚合了VehicleIdReader,Gate和DataBaseManager类。
其中，VehicleIdReader类是一个抽象接口，由 MockVehicleIdReader 和  WebcamVehicleIdReader 继承实现。MockVehicleIdReader是一个不依靠摄像头的模拟类，方便测试reader的业务逻辑和算法. WebcamVehicleIdReader 是实现了读取摄像头内容的类。他们都实现了 VehicleIdReader 接口里的get_vehicle_id() 函数，即通过算法读取图片中的数字并且返回一串字符串（string）

DataBaseManager类提供了连接，关闭连接的函数，以及操作数据库中数据的增加，删除，查询，更改函数

Gate类 Gate类聚合了一个GateIndicator泛型的list， composition了一个State类（继承，聚合，composition都是面向对象里的概念，composition describe a 'part of' relationship）并且有一个公开的register_indicator（GateIndicator）函数用来注册indicator进入到Gate里，这样可以降低Gate和GateIndicator的耦合，让Gate对象可以自由注册不同的实现了GateIndicator接口的对象。

State是一个接口(interface), 用来实现Gate的状态机，通过切换不同状态来实现不同的业务代码。State规定了一个run（）的函数存放业务逻辑，change_state()函数改变状态。然后实现了这个接口的OpenState和CloseState()类重写实现了这两个函数.

GateIndicator也是一个接口，实现了这个接口的indicator都会有on_gate_open()和on_gate_close()函数，都可以作为indicator传入到Gate对象使用。类图中，有Moter，RGBLightStateIndicator和Screen类实现了这个接口。

###### GateApp中的状态机

（查询状态机的定义）状态机动作，状态 啥的，动作在图中是箭头中的文字，方框中的是状态，简单描述一下


##### DataBaseUIApp部分
这部分是项目中管理数据库数据的部分，独立了一个软件来管理。该部分复用了之前的DataBaseManager的代码，提供了一个简单的终端UI来增加，删除，查询，更改和显示全部数据库数据

DataBaseUIApp类是UI的主要部分，同样会有run（）和exit（）函数来给程序主入口提供运行程序和释放资源. 同时该类聚合了一个Menu对象，用来显示当前菜单选项。

Menu是一个接口，规定了实现Menu的类需要有一个 DataBaseManager对象来管理数据库。实现了这个接口的有AddMenu,DeleteMenu,SearchMenu和ModifyMenu类，这些类会在DataBaseUIApp类中通过切换类型来显示不同的菜单，也就是面向对象中多态的实现，实现了状态机。

###### DataBaseUIApp部分的状态机
同上


