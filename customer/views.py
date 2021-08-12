from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
from django.views.generic import TemplateView,ListView,DeleteView
from django.contrib.auth.models import User
from owner.models import Mobile
from customer.models import Cart
from django.contrib import messages
# Create your views here.
class RegistrationView(TemplateView):
    form_class=forms.RegistrationForm
    template_name = "registration.html"
    model=User
    context={}

    def get(self, request, *args, **kwargs):
        form=self.form_class
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
                form.save()
                return redirect("signin")

class SignInView(TemplateView):
    template_name = "login.html"
    form_class=forms.LoginForm
    cotext={}
    def get(self, request, *args, **kwargs):
        form=self.form_class
        self.cotext["form"]=form
        return render(request,self.template_name,self.cotext)

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("customerhome")



class CustomerHome(ListView):
    template_name = "customerhomepage.html"
    model = Mobile
    context_object_name = "mobiles"

class ProductDetail(DeleteView):
    template_name = "product_detail.html"
    model = Mobile
    context_object_name = "mobile"
    pk_url_kwarg = 'pk'



class AddCartView(TemplateView):
    model=Cart
    def get(self, request, *args, **kwargs):
        product_id=kwargs["id"]
        product=Mobile.objects.get(id=product_id)
        user=request.user
        cart=Cart(product=product,user=user)
        cart.save()
        messages.success(request,"Added to cart")
        return redirect("customerhome")

class ViewCart(ListView):
    model = Cart
    template_name = "cart_detail.html"
    context_object_name = "items"

class SignOutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("signin")

