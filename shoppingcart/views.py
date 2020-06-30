from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render

from .models import Item, Cart, CartItem


# Create your views here.
def menu(request):

	if request.user.is_authenticated:
		cart_n = Cart.objects.filter(user=request.user)
		if cart_n.count() < 1:
			Cart.objects.create(user=request.user)

		context = {
			'items': Item.objects.all(),
			'cart': Cart.objects.get(user=request.user),
			'user': request.user
		}
		return render(request, "menu.html", context)

	else:
		context = {
			'items': Item.objects.all(),
		}
		return render(request, "menu.html", context)

def user(request):
	return render(request, "user.html")

def login_view(request):
	username = request.POST.get("username")
	password = request.POST.get("password")
	user = authenticate(request, username=username, password=password)

	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse("user"))

	else:
		return render(request, "login.html", {"message": "Invalid Credentials"})

def logout_view(request):
	logout(request)
	return render(request, "login.html", {"message": "Logged out."})


def cart(request):
	if request.user.is_authenticated:

		cart = Cart.objects.filter(user=request.user)

		if cart.count() < 1:
			cart = Cart(user=request.user)
			cart.save()

		context = {
			'cart': Cart.objects.get(user=request.user)
		}
		return render(request, "cart.html", context)
	
	else: 
		return HttpResponseRedirect(reverse("login"), {"message": "Log in to access cart"})

def add_to_cart(request, item_id):
	item_pk = request.POST.get("item_pk")
	cart = Cart.objects.get(user=request.user)
	item = CartItem.objects.create(item_reference = Item.objects.get(pk=item_pk))
	cart.items.add(item)
	return HttpResponseRedirect(reverse("menu"))




