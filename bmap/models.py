from django.db import models


#性别
gender_choice = (
    ('男', '男'),
    ('女', '女'),
)

# Create your models here.
class HotelAccInfo(models.Model):
    name = models.CharField(max_length=30, verbose_name="姓名", null=False)
    gender = models.CharField(max_length=30, choices=gender_choice, default='男', verbose_name="性别")
    birth = models.DateField(verbose_name="出生日期")
    idcard = models.CharField(max_length=18, null=False, verbose_name="身份证号")
    city = models.CharField(max_length=100, verbose_name="省市区(县)")
    hotel = models.CharField(max_length=100, verbose_name="宾馆名称")
    room = models.CharField(max_length=20, verbose_name="房间号")
    checkintime = models.DateField(verbose_name="入住时间")
    checkouttime = models.DateField(verbose_name="退房时间")