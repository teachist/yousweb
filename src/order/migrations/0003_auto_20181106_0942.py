# Generated by Django 2.1.2 on 2018-11-06 01:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20181104_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', help_text='请务必填写正确！ 方便我们给你送货。', max_length=200, verbose_name='送货地址'),
        ),
        migrations.AlterField(
            model_name='order',
            name='contact_phone',
            field=models.CharField(help_text='请务必填写正确！ 填写11位的电话号码。', max_length=11, verbose_name='联系电话'),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 6, 9, 42, 14, 722403), verbose_name='订单生成时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='finish_time',
            field=models.DateTimeField(auto_now=True, verbose_name='订单完成时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.CharField(choices=[('广告', (('ad1', '喷绘'), ('ad2', '写真'))), ('打印', (('pt1', '论文修改'), ('pt2', '复习资料'))), ('other', '其他')], default='ad1', max_length=10, verbose_name='产品规格'),
        ),
    ]