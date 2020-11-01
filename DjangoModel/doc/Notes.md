## 数据表删除bug
+ 重建数据表时，提示 no changes detected
  +  应当将 该 应用，以及主项目目录中的 缓存文件全部手动删除
     + migrations & ____pycache__ 
  + 然后
    + python3 manage.py makemigrations --empty 应用名
    + python3 manage.py makemigrations 
    + python3 manage.py migrate
    + okです
***
    + 尽量通过 ORM 修改数据表

## 向数据库添加数据
+ 在 model.py 中创建类
  + 之后 视图函数 views.py 中编写 函数，创建对象
    + 必须调用 .save() 才能存储进数据库
      + 注意： __init__ 已在 models.Model 中使用，在自定义时不能用
      + 是 查询集（可迭代对象） 
      + 查询集  可以有多个 过滤器 ***filter*** ***exclude***
        + 过滤器 是  函数 （查看源代码 可知）
        + 从 sql 角度来看 过滤器 和 select语句 等价 相当于 where 查询条件
        
+ model.py 中 一个类方法 代表 表中的 一个字段
  + 添加后 须 重新  ***迁移***
  + 注意： model.py 增加 函数后 不需要重新 迁移
***
+ 创建对象方案
  + 在模型类中增加 类方法， 创建对象
    + @classmethod
    + def create(cls,name,age):
  + 在自定义的 管理器 中添加方法 来创建对象
    
### 注（接上）：方法
+ 对象方法
  + 可以调用对象属性， 也可以调用 类的属性
+ 类方法
  + 只能 调用类属性
+ 静态方法
  + 啥都不能调用， 不能获取对象属性， 也不获取 类属性 
## 快捷键
* .re 快速生成 return

### 查询集 和 过滤器
+ 在 管理器上 调用方法 返回 查询集 
* 查询集 经 过滤器 筛选返回新的 查询（clone），因此 可以 链式调用
  + all() 返回所有数据
  + filter() 符合条件数据
  + exclude() 条件以外数据
  + order_by() 排序
  + value() 一条数据为 一个 字典 ， 返回一个 列表 类似 json
  + 以上返回值 均为 ***<class 'django.db.models.query.QuerySet'>***

## 状态码
+ 2**
  + 请求成功
+ 3**
  + 转发 重定向
+ 4**
  + 客户端错误
+ 5**
  + 服务器错误 ！！！

### 获取单个对象
+ get() 返回 一个 满足条件的对象
  + 查询条件没有匹配对象，doesNotExist
      + get使用に注意
  + 查询条件 存在多个对象也不行  MultipleObjectsReturned
+ first() 返回 查询集 第一个对象
+ last() 最后一个
+ count（） 对象个数
+ exist（） 判断是否 有数据 有--True；无--False

#### first last
+ 默认情况下 正常获取 从 QuerySet
+ 隐藏bug
  + 可能会出现 获取相同对象
    + 显示 写出 ***排序规则***
    
    
 ## 限制查询集 切片
 + 不同于python切片
 + QuerySet[5:15] 获取 5-15 条数据
   * 相当于 sql 中 limit offset
   
 + 每个查询集 都有一个缓存，为了最小化 数据库访问
   + filter。。。时 并不会查询数据库
   + 只有在 迭代 查询结果，或获取单个对象属性，才会去查询数据库
     + 所谓 ***懒查询*** 
       + 为 优化结构和查询

## 查询条件
+ 属性__运算符=值
+ gt
+ lt
+ gte
+ lte
+ in 在某一个集合当中
+ contains 包含 类似于 sql 的 **like**  大小写敏感 加 ```i```（ignore）则不区分大小写

+ startswith 相当于 like
+ endswith  也 相当于 like
+ 时间的比较运算符

***
```	on_delete=None,               # 删除关联表中的数据时,当前表与其关联的field的行为
	on_delete=models.CASCADE,     # 删除关联数据,与之关联也删除
	on_delete=models.DO_NOTHING,  # 删除关联数据,什么也不做
	on_delete=models.PROTECT,     # 删除关联数据,引发错误ProtectedError
	# models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)
	on_delete=models.SET_NULL,    # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）
	# models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
	on_delete=models.SET_DEFAULT, # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）
	on_delete=models.SET,         # 删除关联数据,
	 a. 与之关联的值设置为指定值,设置：models.SET(值)
	 b. 与之关联的值设置为可执行对象的返回值,设置：models.SET(可执行对象）
```
### 聚合函数
+ aggregate()
  + Avg()
  + Max()
  + Count()
  + Min()
  + Sum()
  
### F对象
+ 可 使用 模型的 A属性与B属性 比较
  + 可 获取属性值
  + 实现同一个模型 不同属性之间的比较 查询等操作
  + 还支持算数运算符
  
### Q对象
+ 可以对 条件 进行封装
+ 封装之后，可以支持 逻辑运算
  + 与（&） 或（|） 非（～） 等

  
  