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
  