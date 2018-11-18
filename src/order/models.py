from django.db import models
from django.conf import settings
from datetime import datetime


class Order(models.Model):
    '''
    Customer Order Model tabel
    This Model define how our customer order our product,
    every customer have a unique user account in our db
    we can use the foreign key relationship to connect this
    two table, once our user order a product from our store,
    we can immediatly give a record to ther user account.

    :field  user            each user can have many orders
    :field  customer        customer who issue a order
    :field  contact_phone   customer's phone
    :field  address         customer's recieve address
    :field  status          track the order's status for message parser
    :field  product         user's order type outline
    :field  description     user's personal description for product
    :field  create_time     order's created time
    :field  finish_time     order's finishe time
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customer = models.CharField(
        max_length=200,
        verbose_name="联系人",
        help_text='请务必仔细填写填，方便我们联系你。'
    )
    contact_phone = models.CharField(
        '联系电话',
        max_length=11,
        help_text='请务必填写正确！ 填写11位的电话号码。',
    )
    address = models.CharField(
        '送货地址',
        max_length=200,
        help_text='请务必填写正确！ 方便我们给你送货。',
        default=''
    )
    PRODUCT_CHOICES = (
        ('广告', (
            ('ad1', '喷绘'),
            ('ad2', '写真'),
        )),
        ('打印', (
            ('pt1', '论文修改'),
            ('pt2', '复习资料'),
        )),
        ('other', '其他'),
    )
    product = models.CharField(
        verbose_name='产品规格',
        max_length=10,
        choices=PRODUCT_CHOICES,
        default='ad1'
    )
    description = models.TextField(
        verbose_name='具体要求请备注',
        blank=True,
        null=True,
        help_text='请添加你对产品设计制作和安装过程中的详细要求。',
    )

    STATUS_CHOICE = (
        (0, '等待处理'),
        (1, '前台已经接单'),
        (2, '设计师设计中...'),
        (3, '等待定稿...'),
        (4, '等待安装...'),
        (5, '正在配送安装...'),
        (6, '订单完成'),
    )
    status = models.IntegerField(
        verbose_name='产品状态',
        default=0,
        choices=STATUS_CHOICE,
    )
    # price = models.FloatField(default=0.0)
    create_time = models.DateTimeField(
        verbose_name='订单生成时间',
        default=datetime.now(),
    )
    # finish_time = models.DateTimeField(
    #     verbose_name='订单完成时间',
    #     auto_now=True
    # )
    finish_time = models.DateTimeField(
        verbose_name='订单完成时间',
        auto_now=True
    )

    def contact_phone_format(self):
        return f'{self.contact_phone[:3]}-{self.contact_phone[3:7]}-{self.contact_phone[7:12]}'

    contact_phone_format.admin_order_field = 'finish_time'
    # contact_phone_format.boolean = True
    contact_phone_format.short_description = '联系方式'

    def finish_time_check(self):
        if self.status == 6:
            self.finish_time = datetime.now()
            return self.finish_time
        else:
            return '-'

    # def front_review(self):
    #     return self.review_set.filter(stuff__position=1).first().stars

    # def designer_review(self):
    #     return self.review_set.filter(stuff__position=2).first().stars

    # def installer_review(self):
    #     return self.review_set.filter(stuff__position=3).first().stars

    def __str__(self):
        return self.customer
