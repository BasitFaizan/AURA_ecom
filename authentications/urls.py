from django.urls import include, path
from authentications import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.sign_up, name="signup"),
    path('login/', views.logIn, name="login"),
    path('logout/', views.logOut, name="logout"),
    path('profilePage/', views.profilePage, name='profilepage'),
    path('services/', views.service, name='services'),
    path('sell/', views.sell, name='sell'),
    path('category/', include('category.urls')),
]