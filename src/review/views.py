# -*- coding: utf-8 -*-
"""
views.py
@author wilton
@version 2018-10-30
"""
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm
# from django.forms import inlineformset_factory
from .models import Review
from order.models import Order
from django.contrib.auth.decorators import login_required


def index(request):
    context = {}
    return render(request, 'review/index.html', context=context)


@login_required
def review(request, order_id=None):
    order = get_object_or_404(Order, pk=order_id, user=request.user)
    review_sets = order.review_set.all()

    if not review_sets.exists():
        return redirect('index')

    title = '请对我们做出评价'
    product = f'Please review: {order.customer}'
    # CollectStarFormSet = inlineformset_factory(Order, Star, fields=('stars',))
    data = {
        ''
    }
    form = ReviewForm(request.POST or None)
    confirm_message = ''
    if form.is_valid():
        ft_star = form.cleaned_data['ft_star']
        ds_star = form.cleaned_data['ds_star']
        tf_star = form.cleaned_data['tf_star']
        # comment = form.cleaned_data['comment']
        review_sets = order.review_set.all()
        for review in review_sets:
            if review.stuff.position == 1:
                review.stars = ft_star
            elif review.stuff.position == 2:
                review.stars = ds_star
            elif review.stuff.position == 3:
                review.stars = tf_star
            review.save()
        print(review_sets)
        ft_review = Review()
        # save to our database
        # print(order, star, comment)
        title = 'Thanks!'
        confirm_message = 'You have a chance to get bouns.'
        form = None

        print(request.POST)
    context = {'title': title, 'product': product, 'review_sets': review_sets,
               'form': form, 'confirm_message': confirm_message, }
    # print(dir(request))
    return render(request, 'review/star.html', context=context)
