from django.db import models

# Create your models here.
"""
1.我们的模型类需要继承来自 models.Model
2.系统会自动为我们添加一个主键--id
3.字段
   
    字段名=model.类型（选项）
    
    字段名其实就是数据表的字段名
    学段名不要使用python mysql等关键字
    
    char(M)
    varchar(M)
    M 就是选项
"""
class BookInfo(models.Model):
    #id
    name=models.CharField(max_length=10)

     #重写__str__方法以让admin来显示书籍名字
    def __str__(self):
        return self.name

#人物先复制过来，后期讲原理
# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
