## 模版标签
+ 结构标签
  + block
    + 用来规划布局
    + 首次出现 代表规划
    + 第二次，代表填充以前的规则
    + 第三次，代表填充以前的规则， 默认是覆盖
      * 不想覆盖：添加{{block.super}}
      * 这样可实现增量式操作
  * extent
    + 继承
    + 可以获取父模版所有结构
  + block + extends
    + 化整为零
  + include
    + 可以将页面作为其他页面的一部分 进行嵌入
  + include + block
  + 三个标签 可混合使用
  + 尽量用 block+extends，因为 include 效率不高  
  + 如果，继承自父模版，则子模版重写的页面结构是不生效的
  
  
+ 标签语法
+ 常用标签

### 静态资源
+ 动静分离
+ 创建静态文件夹
+ 在SETTING中注册 STATICFILE_DIR=[]
+ 在模版中使用
  + 先加载静态资源  ``{% load static %}``
  + 使用 `{% static 'xxx' %}` xxx相对路径
+ 注意点：
  + 仅能在 debug 模式中使用
  + 以后需要单独处理
  
# python 内存分配
+ 垃圾回收使用引用计数器
+ id[([1,2,3])==id([4,5,6])
  + 存在赋值符号 =  ， 才会进行内存分配
  + 没有赋值符号，直接调用的话，会在临时缓冲区，id获取临时缓冲区的内容
  
  

# 视图
### 概述
+ Django 中视图主要用来接收 web请求，并响应
  + 本质上是一个 函数
  + 分类
    + 以Json数据形式返回
    + 以网页形式返回
      + 重定向到另一个网页
      + 错误视图（40x，50x）错误
  + 过程：
    + 浏览器 -> Django 获取信息并去掉IP 路径，剩下路径 -> urls路由匹配 -> 视图响应 -> 返回到浏览器
    
### 配置URL
+ 流程 
  + setting 中指定 根级 url配置文件， 对应属性 ROOT_URLCONF
  + urlpatterns: 一个 URL实例 的列表，全在根配置搞定，内部 url组成（正则匹配路径）
    + url('Learn/', views.learn),
  + 导入其他URL配置：
    + 在应用中创建 urls.py 文件，编写匹配规则，在 project的 urls.py 中进行导入
      + ```python
        from django.conf.urls import include
        urlpatterns = [
                url('xxx/',include('App.urls'))
        ]
      ```
  + url 正则匹配注意事项： **（没有最有匹配）**
    + 正则匹配时 从上到下遍历， 匹配到之后不再继续向后查找。
    + 匹配的正则前方不需要加反斜线
  + url路由编写规则：
  + url路由路径中的参数，使用  （） 进行获取
    + 一对 圆括号，对应视图函数中的一个参数
    
    
+ url 反向解析
  + 动态获取路径
  
  
  
# 双R （request ，response）
### HttpResponse
+ 视图中的第一个参数就是 HttpResponse 对象

    