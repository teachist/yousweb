from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Order
from .forms import NewOrder
from wxservice import clients


@login_required
def new_order(request):
    title = '创建订单'
    form = NewOrder(request.POST or None)
    confirm_message = ''

    if form.is_valid():
        customer = form.cleaned_data['customer']
        contact_phone = form.cleaned_data['contact_phone']
        product = form.cleaned_data['product']
        # user = request.user
        order = Order(customer=customer, contact_phone=contact_phone, product=product, user=request.user)
        order.save()
        title = 'Thanks!'
        confirm_message = 'You have a chance to get bouns.'
        if request.user.is_authenticated and clients:
            template_id = clients.client.template.get('TM00015')
            data = {
                "first": {
                    "value": "你订购的商品我们已经知晓，稍后会有人联系你！",
                    "color": "#173177"
                },
                "orderMoneySum": {
                    "value": "39.8元",
                    "color": "#173177"
                },
                "orderProductName": {
                    "value": product,
                    "color": "#173177"
                },
                "Remark": {
                    "value": f'你的姓名: {customer}',
                    "color": "#173177"
                }
            }
            clients.client.message.send_template(request.user.openid, template_id, data, 'https://baidu.com')
        form = None

    context = {'title': title, 'form': form, 'confirm_message': confirm_message, }
    return render(request, 'order/new.html', context=context)
