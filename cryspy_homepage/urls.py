"""cryspy_homepage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from register import views
from login import views as login_view  ##default login route
from django.contrib.auth import views as auth_views  ##django default login views
from home import views as home_view
from blog.views import product_create_view, product_detail_view, index
from createpdf import views as pdf_viewx

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register),
    path('about/', home_view.about, name='about'),
    path('home/', home_view.homepage, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path('blogentry/', product_create_view,name="blogentry"),
    path('detail/',index)
    # path('createpdf/',pdf_view.GeneratePdf)
]
