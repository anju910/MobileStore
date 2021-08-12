from django.urls import path
from customer import views


urlpatterns=[
    path("accounts/signin",views.SignInView.as_view(),name="signin"),
    path("accounts/signup",views.RegistrationView.as_view(),name="signup"),
    path("home",views.CustomerHome.as_view(),name="customerhome"),
    path("products/<int:pk>", views.ProductDetail.as_view(), name="productdetail"),
    path("products/addtocart/<int:id>",views.AddCartView.as_view(),name="addtocart"),
    path("products/carts", views.ViewCart.as_view(), name="cartdetails"),
    path("accounts/signout",views.SignOutView.as_view(),name="signout"),
]