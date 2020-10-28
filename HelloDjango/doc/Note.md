## Django
### SQLite3
+ 轻量嵌入式数据库与mysql相似
  + 常应用于 android ios wp
### 实现一个请求
+ 注册一个路由(url)
   + urls中
     + 参数1， 匹配规则， 正则表达式
     + 视图函数
       + 对应的 views 中的一个函数
         + **没有括号**，有括号是调用之意
+ 去 views 实现对应的视图函数
  + 第一个参数是 request
  + 必须返回一个 response
   
## html
+ ul*5 tab

#### 分散函数功能，不宜集中

## 模版配置（网页文件位置）
+ 两种
  + 在app中进行模版配置
    + 在app的目录 创建 templates 文件夹
    + 要添加 templates 文件夹为 mark as templatefolder
  + 在项目中进行模版配置
    + 在项目目录中创建 templates 并且标记
    + 在项目 setting.py 中进行注册
  + 在实际开发中常用第二种
    + 全局位置---模版可以继承

## 路由优化配置
  + 简化项目逻辑 进行拆分
  + 拆分为多个App（Two）
  + 继续拆分路由器 urls
    + 在App中创建自己的  urls.py
      + urlpatterns 路由规则列表
      + 在根 urls 中进行子路由包含 （include）
    + 子路由使用
      + 根路由规则（path('two', include('Two.urls')),） + 子路由规则（urlpatterns = [
    url('index', views.index),
]）
      