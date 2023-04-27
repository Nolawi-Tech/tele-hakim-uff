from django.shortcuts import render
import requests

def home(request):
    return render(request, 'pay/home.html')

def payment_with_cart(request):
    obj = {
        "process": "Cart",
        "successUrl": "http://localhost:8000/success",
        "ipnUrl": "http://localhost:8000/ipn",
        "cancelUrl": "http://localhost:8000/cancel",
        "merchantId": "22429",
        "merchantOrderId": "l710.0",
        "expiresAfter": 24,
        "totalItemsDeliveryFee": 19,
        "totalItemsDiscount": 1,
        "totalItemsHandlingFee": 12,
        "totalItemsTax1": 250,
        "totalItemsTax2": 0
    }
    cart = {
        "cartitems": [

        {

            "itemId":"sku-01",

            "itemName":"sample item",

            "unitPrice":2300,

            "quantity":1

        },

        {

            "itemId":"sku-02",

            "itemName":"sample item 2",

            "unitPrice":2300,

            "quantity":2

        }

        ]
    }
    return render(request, 'pay/index-cart.html', {'obj': obj, 'cart': cart})

def payment_with_express(request):
    obj = {
        "process": "Express",
        "successUrl": "http://localhost:8000/success",
        "ipnUrl": "http://localhost:8000/ipn",
        "cancelUrl": "http://localhost:8000/cancel",
        "merchantId": "SB2261",
        "merchantOrderId": "l710.0",
        "expiresAfter": 24,
        "itemId": 60,
        "itemName": "Billing",
        "unitPrice": 11.0,
        "quantity": 1,
        "discount": 0.0,
        "handlingFee": 0.0,
        "deliveryFee": 0.0,
        "tax1": 0.0,
        "tax2": 0.0
    }
    return render(request, 'pay/index-express.html', {'obj': obj})

def success(request):
    ii= request.GET.get('itemId')
    total = request.GET.get('TotalAmount')
    moi = request.GET.get('MerchantOrderId')
    ti = request.GET.get('TransactionId')
    status = request.GET.get('Status')
    url = 'https://testapi.yenepay.com/api/verify/pdt/'
    datax = {
        "requestType": "PDT",
        "pdtToken": "Q1woj27RY1EBsm",
        "transactionId": ti,
        "merchantOrderId": moi
    }
    x = requests.post(url, datax)
    if x.status_code == 200:
        print("It's Paid")
    else:
        print('Invalid payment process')
    return render(request, 'pay/success.html', {'total': total, 'status': status,})

def cancel(request):
    return render(request, 'pay/cancel.html')

def ipn(request):
    return render(request, 'pay/ipn.html')


def login(request):
    name = ch

# from django.shortcuts import get_object_or_404, render, redirect
# from django.conf import settings
# from chapa import Chapa
# from .models import Order

# @login_required
# def order_confirm(request, order_id):
# """Handles initializing payment and redirecting to the payment gateway's page"""

#     order = Order.objects.get(id=order_id)

#     if request.method == 'POST':
#         data = {
#             'email': request.user.email,
#             'amount': order.total,
#             'first_name': request.user.first_name,
#             'last_name': request.user.last_name,
#             'tx_ref': order.id,
#             # optional
#             'callback_url': request.build_absolute_uri(
#                 reverse('billing:success', kwargs={'order_id': order.id})
#             ),
#             'customization': {
#                 'title': 'FidelBooks',
#                 'description': 'Payment for your services',
#             }
#         }

#         chapa = Chapa(settings.CHAPA_SECRET_KEY)
#         response = chapa.initialize(**data)

#         # after successfull response redirect to the chapa checkout_url
#         if response['status'] == 'success':
#             return redirect(response['data']['checkout_url'])
#         else:
#             messages.error(request, response['message'])

#     return render(request, 'billing/order_confirm.html', {
#         'payment_method': payment_method,
#     })

# @login_required
# def success(request, order_id):
# """Responsible for verifying payment and updating order status"""

#     order = get_object_or_404(Order, id=order_id)

#     # verify a transaction
#     chapa = Chapa(settings.CHAPA_SECRET_KEY)
#     response = chapa.verify(order_id)

#     context = {'order': order, 'msg': response['message']}

#     if response['status'] == 'success':
#         order.status = 'UN'
#         order.payment_status = 'PA'
#         order.save()
#         context['valid'] = True

#     return render(request, 'billing/order_complete.html', context)