from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from authentications.models import profile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from category.models import category, product

# Create your views here.

def home(request):
    return render(request, 'index.html')
def service(request):
    return render(request,'service.html')

def sign_up(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        if password!=confirmPassword:
            messages.warning(request,'Password not match,try again')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'email address already exists,try again')
        else:
            user =User.objects.create_user(email,email,password)
            user.save()
            profileManager = profile.objects.create(mainUser=user)
            profileManager.save()
            messages.success(request,'You have successfully created your accounts')
            return redirect('/login')
    return render(request,'signup.html')

def logIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = authenticate(request,username=email, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else :
                messages.warning(request,'Incorrect credentials')
        except Exception:
            messages.warning(request,"something went wrong")

    return render(request,'login.html')

def logOut(request):
    logout(request)
    return redirect('/')

@login_required
def profilePage(request):
    if request.method == 'POST':
        user = request.user
        profileManage = profile.objects.get(mainUser = user)
        username = request.POST.get('username')
        proileImg = request.FILES.get('proileImg')
        fName = request.POST.get('fName')
        lName = request.POST.get('lName')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phoneNumber')
        profileManage.Phonenumber = phoneNumber
        profileManage.profilePic = proileImg
        profileManage.first_name = fName
        profileManage.last_name = lName
        try:
            profileManage.save()
            print('hogaya')
        except Exception as e:
            print(e)


    user = request.user
    profileManage = profile.objects.filter(mainUser = user)
    context = {
        'user':user,
        'profile':profileManage
    }
    return render(request,'profilePage.html',context)
@login_required
def sell(request):
    if request.method == 'POST':
        prod_img_1 = request.FILES.get('prod_img_1')
        prod_img_2 = request.FILES.get('prod_img_2')
        prod_img_3 = request.FILES.get('prod_img_3')
        productName = request.POST.get('productName')
        productPrice = request.POST.get('productPrice')
        categoryName = request.POST.get('categoryName')
        subCategory = request.POST.get('subCategory')
        productDescription = request.POST.get('productDescription')
        user = request.user
        categoryFilter = category.objects.get(categoryName=categoryName)
        categories = product.objects.create(userProduct=user,categoryName=categoryFilter,subCategory=subCategory,productName=productName,productDescription=productDescription,productPrice=productPrice,prod_img_1=prod_img_1,prod_img_2=prod_img_2,prod_img_3=prod_img_3)
        categories.save()
    return render(request,'sell.html')
    


