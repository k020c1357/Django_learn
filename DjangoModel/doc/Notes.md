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

