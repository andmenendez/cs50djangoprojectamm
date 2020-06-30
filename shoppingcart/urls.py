from django.urls import path

from . import views

urlpatterns = [
	path("", 			views.menu, 			name="menu"),
	path("user", 		views.user, 			name="user"),
	path("login", 		views.login_view, 		name="login"),
	path("logout", 		views.logout_view, 		name="logout"),
	path("cart", 		views.cart, 			name="cart")
]

urlpatterns += [
	path("add_to_cart/<int:item_id>/", views.add_to_cart, name="add_to_cart")
]