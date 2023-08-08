from django.http import HttpResponse
from django.urls import path
from category import views

urlpatterns = [
    path('<uuid:categoryId>/', views.categ, name="category"),
    path('allCategory/', views.allCategory, name="allCategory"),
    path('productPage/<uuid:productId>/', views.productPage, name="productPage"),
    path('buy/<uuid:productId>/', views.buy, name="buy"),
    path('paytmHandleRequest/',views.paytmHandleRequest,name='paytmHandleRequest')
]