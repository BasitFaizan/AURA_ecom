from django.shortcuts import render
from category.models import category,product
from authentications.models import address
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from paytmchecksum import PaytmChecksum
# Create your views here.

def categ(request,categoryId):
    allProduct = {}
    allProductList = set()
    categ = category.objects.get(pk=categoryId)
    products = product.objects.filter(categoryName=categ)
    for products in products:
        subCategoryName = products.subCategory
        allProductList.add(subCategoryName)
    for getProduct in allProductList:
        subCategoryProduct = product.objects.filter(subCategory=getProduct)
        allProduct[getProduct] = subCategoryProduct
    print(allProduct)
    return render(request,'category.html',{'categories':categ,'product':allProduct})

def allCategory(request):
    return render(request,'allCategoryPages.html')

def productPage(request,productId):
    productDetails = product.objects.get(pk=productId)
    return render(request,'productPage.html',{'productDetails':productDetails})


def buy(request,productId):
    user = request.user
    userAddress = address.objects.filter(userAdd=user)
    productDetails = product.objects.get(pk=productId)
    #Request paytm to transfer the amount to your account after payment by user
    return render(request,'buy.html',{'productDetails':productDetails,'user':user,'userAddress':userAddress})

@csrf_exempt
def paytmHandleRequest(request):
    # More Details: https://developer.paytm.com/docs/checksum/#python


# Generate Checksum via Hash/Array
# initialize an Hash/Array
    paytmParams = {"MID": "YOUR_MID_HERE", "ORDERID": "YOUR_ORDER_ID_HERE"}

    # Generate checksum by parameters we have
    # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
    paytmChecksum = PaytmChecksum.generateSignature(paytmParams, "YOUR_MERCHANT_KEY")
    verifyChecksum = PaytmChecksum.verifySignature(paytmParams, "YOUR_MERCHANT_KEY",paytmChecksum)

    print(f"generateSignature Returns:{str(paytmChecksum)}")
    print(f"verifySignature Returns:{str(verifyChecksum)}")

    # Generate Checksum via String
    # initialize JSON String
    body = "{\"mid\":\"YOUR_MID_HERE\",\"orderId\":\"YOUR_ORDER_ID_HERE\"}"

    # Generate checksum by parameters we have
    # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
    paytmChecksum = PaytmChecksum.generateSignature(body, "YOUR_MERCHANT_KEY")
    verifyChecksum = PaytmChecksum.verifySignature(body, "YOUR_MERCHANT_KEY", paytmChecksum)

    print(f"generateSignature Returns:{str(paytmChecksum)}")
    print(f"verifySignature Returns:{str(verifyChecksum)}")