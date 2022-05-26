from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from eshop_products.models import Product
from .forms import order_form
from .models import order
from .models import order_detail
from django.http import HttpResponse
from django.shortcuts import redirect
import requests
import json
from e_shop.utils import price_show


@login_required(login_url='/login')
def new_order_creat(request):
    order_Form = order_form(request.POST or None)

    if order_Form.is_valid():
        Order = order.objects.filter(owner_id=request.user.id, is_paid=False).first()

        product = Product.objects.filter(id=order_Form.cleaned_data.get('product_id')).first()

        if Order is None:
            Order = order.objects.create(owner_id=request.user.id, is_paid=False)

        count = order_Form.cleaned_data.get('count')

        if count <= 0:
            count = 1

        Order.order_detail_set.create(count=count, product_id=product.id,
                                      price=product.price)

        return redirect('/')


@login_required(login_url='/login')
def order_page(request):
    context = {
        'order_details': None,
        'user_error': None
    }
    Order = order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if Order is None:
        context['user_error'] = True
        return render(request, 'order_page.html', context)
    total_order_price = 0
    context['order_details'] = Order.order_detail_set.all()
    for item in context['order_details']:
        total_order_price += item.price * item.count
    context['total_p'] = price_show(total_order_price)

    context['Taxation'] = price_show(int(total_order_price * 1 / 100))
    for item in context['order_details']:
        item.product.price = price_show(item.product.price)
    context['full_total'] = price_show(total_order_price + int(total_order_price * 1 / 100))
    return render(request, 'order_page.html', context)


def order_delete(request, *args, **kwargs):
    order_detail_id = kwargs.get('detail_id')
    order_detail_del = order_detail.objects.filter(id=order_detail_id).first().delete()
    return redirect('/user-order')


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
amount = 11000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://localhost:8000/verify/'


def send_request(request):
    req_data = {
        "merchant_id": MERCHANT,
        "amount": amount,
        "callback_url": CallbackURL,
        "description": description,
        "metadata": {"mobile": mobile, "email": email}
    }
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
        req_data), headers=req_header)
    authority = req.json()['data']['authority']
    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


def verify(request):
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                return HttpResponse('Transaction success.\nRefID: ' + str(
                    req.json()['data']['ref_id']
                ))
            elif t_status == 101:
                return HttpResponse('Transaction submitted : ' + str(
                    req.json()['data']['message']
                ))
            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(
                    req.json()['data']['message']
                ))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return HttpResponse('Transaction failed or canceled by user')
