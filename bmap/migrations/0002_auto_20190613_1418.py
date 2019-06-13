# Generated by Django 2.1.7 on 2019-06-13 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelaccinfo',
            name='birth',
            field=models.DateField(verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='hotelaccinfo',
            name='checkintime',
            field=models.DateField(verbose_name='入住时间'),
        ),
        migrations.AlterField(
            model_name='hotelaccinfo',
            name='checkouttime',
            field=models.DateField(verbose_name='退房时间'),
        ),
        migrations.AlterField(
            model_name='hotelaccinfo',
            name='city',
            field=models.CharField(max_length=100, verbose_name='省市区(县)'),
        ),
        migrations.AlterField(
            model_name='hotelaccinfo',
            name='hotel',
            field=models.CharField(max_length=100, verbose_name='宾馆名称'),
        ),
        migrations.AlterField(
            model_name='hotelaccinfo',
            name='idcard',
            field=models.CharField(max_length=18, verbose_name='身份证号'),
        ),
        migrations.AlterField(
            model_name='hotelaccinfo',
            name='room',
            field=models.CharField(max_length=20, verbose_name='房间号'),
        ),
    ]
