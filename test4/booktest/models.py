#coding:utf8
from django.db import models

# Create your models here.
class BookInfo(models.Model):
	btitle=models.CharField(max_length=20)
	bpub_date=models.DateTimeField(db_column='pub_date')#加这个参数是因为名字不对应 
	class Meta():
		db_table='bookinfo'#默认名字(数据库中)


class HeroInfo(models.Model)		:
	hname = models.CharField(max_length=10)
	hgender = models.BooleanField()
	hcontent = models.CharField(max_length=1000)
	isDelete = models.BooleanField()
	book = models.ForeignKey('BookInfo')
	def showname(self):
		return self.hname