## 数据表删除bug
+ 重建数据表时，提示 no changes detected
  +  应当将 该 应用，以及主项目目录中的 缓存文件全部手动删除
     + migrations & ____pycache__ 
  + 然后
    + python3 manage.py makemigrations --empty 应用名
    + python3 manage.py makemigrations 
    + python3 manage.py migrate
    + okです
    