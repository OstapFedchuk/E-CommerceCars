from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm

from payment.forms import ShippingForm

from payment.models import ShippingAddress

from django import forms
import json
from cart.cart import Cart

def search(request):
    #Controllo se il form è stato compilato
    if request.method == "POST":
        searched = request.POST['searched']
        #Un passaggio che permetterà di recuperare dal DB il prodotto adatto in base al testo scritto all'interno del form
        searched = Product.objects.filter(name__icontains=searched)
        #
        if not searched:
            messages.success(request, "That Product Don't Exist!!!")
            return render(request, "search.html", {})    
        else:
            return render(request, "search.html", {'searched':searched})    
    else:
        return render(request, "search.html", {})

    

def update_info(request):
    if request.user.is_authenticated:
        #Ottenimento del'User corrente
        current_user = Profile.objects.get(user__id=request.user.id)
        #Ottenimento dei dati di Shipping dell'User corrente
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)

        #Ottengo il form classico dell'User
        form = UserInfoForm(request.POST or None, instance=current_user)
        #Ottengo il form di Shipping dell'User
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)

        if form.is_valid() or shipping_form.is_valid():
            #Salvo il form originale
            form.save()
            #Salvo il shipping form 
            shipping_form.save()
            messages.success(request, "Your Info has been Updated!!!")
            return redirect('home')
        return render(request, "update_info.html", {'form': form, 'shipping_form':shipping_form })
    else:
        messages.success(request, "You must be logged in to access that page!!!")
        return redirect('home') 

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        #Controllo se il form è stato compilato
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            #Controllo se il form è valido
            if form.is_valid():
                form.save()
                messages.success(request, "Your Password Has Been Updated!!!")
                login(request, current_user)
                return redirect('update_user')
            #Altrimenti ritrona un errore
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, "update_password.html", {'form':form})
    else:
        messages.success(request, "You must be Logged In!!!")
        return redirect('home')

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, "User has been Updated!!!")
            return redirect('home')
        return render(request, "update_user.html", {'user_form': user_form})
    else:
        messages.success(request, "You must be logged in to access that page!!!")
        return redirect('home')


def category_summary(request):
     categories = Category.objects.all()
     return render(request, 'category_summary.html', {"categories":categories})

def category(request, foo):
    foo = foo.replace('-', ' ') #Sostituisce lo spazio con il trattino
    #Prendiamo la categoria dall'url
    try:
        #recupero nome categoria
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category':category})
    except:
        messages.success(request, ("That Category Doesn't Exist..."))
        return redirect('home')
        
    
def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user  = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            #Delle 'cose' per il carrello
            current_user = Profile.objects.get(user__id=request.user.id)
            #Ottenimento carrello dell'utente
            saved_cart = current_user.old_cart
            #COnverto la string del DB in dictionary di python usando JSON
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                #Aggiungo il carrello convertito alla sessione corrente
                cart = Cart(request)
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)

            messages.success(request, ("You have been logged in!"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error, please try again!"))
            return redirect('login')

    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out!"))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Username Created - Add Some Your Information!!!"))
            return redirect('update_info')
        else:
            messages.success(request, ("There was an error during the Registration, please try again...!"))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})