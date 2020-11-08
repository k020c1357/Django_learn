## HttpResponse 
### 服务器返回给客户端的数据
+ 由自己创建
  + 不使用模版，直接`HttpResponse()`
  + 调用模版，进行渲染
    + 先 load，再渲染
    + 直接使用 `render（）`
 ```python
    render(request, template_name[,context])
    request
    context #  字典参数
 ```
<h5>MIME</h5>
 + 作用： 指定传输数据，用哪种形式打开
 + 格式： 大类型/小类型
   + image/png
   + image/jpg

### HttpResponse 子类
+ HttpResponseRedirect
  + 响应重定向，可以实现服务器内部跳转
    + `return HttpResponseRedirect('/grade/2020')`
  + 使用时推荐 用 反向解析

+ JsonResponse
  + 返回Json 数据的请求，通常用于 异步请求
    JsonResponse(dict)
  + 也可以用 `__init__(self, data)`设置数据
  + content-type : application/json

#### Json
* JsonObject
  * {}
  * key-value
* JsonArray
  * `[ ]`
  + 列表中可以是普通数据类型，也可以是 JsonObject
+ `` JsonObject JsonArray`` 可以互相嵌套
+ 移动端常用
+ 给Ajax

+ chrome plugins
   + jsonformatter
 
+ 会话
  + cookies
    + 客户端会话技术
      + 数据存储在客户端
    + 键值对 形式
    + 支持过期时间
    + 默认cookies 自动携带，本网站所有cookies
    + Cookies 跨域名，跨网站
    + 通过 HttpResponse 控制（服务器控制客户端）
    + 加盐：加密
        
  + Session
    + 服务端会话技术
    + 数据存储在服务器中
    + 默认 Session存储在内存中
    + django 默认 把session持久化到数据库中
    + session 默认过期时间是 14天
    + 主键是 string
    + 数据有安全保护
    + session 依赖于 cookie
     
  + Token 
    + 服务端会话技术
    + 自定义的session
    + 不依赖 cookie
    