#coding:utf8
from django.contrib import admin

# Register your models here.
from models import *

# class HeroInfoInline(admin.StackedInline):
class HeroInfoInline(admin.TabularInline):
	model = HeroInfo
	extra = 3

class BookInfoAdmin(admin.ModelAdmin):

	list_display = ['id','btitle','bpub_date']
	# list_display = ['id','btitle', 'gender','bpub_date']
	list_filter = ['btitle']
	search_fields = ['btitle']
	list_per_page = 10
	# fields = ['bpub_date', 'btitle']
	fieldsets = [
	('basic',{'fields':['btitle']}),
	('super',{'fields':['bpub_date']}),
	]
	inlines = [HeroInfoInline]
	# list_display = ['id', 'hname', 'gender', 'hcontent']

# def gender(self):
# 	if self.hgender:
# 		return '男'
# 	else:
# 		return '女'
# gender.short_description = '性别'

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)