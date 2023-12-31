"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from products.views import HomePageView, ProductDetailView
from users.views import SignUpView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #homepage
    path('', HomePageView.as_view(), name='home'),
    # sign up
    path('signup/', SignUpView.as_view(), name='signup'),
    #login
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    #logout
    path('logout', auth_views.LogoutView.as_view(next_page="/"), name='logout'),
    #product detail views
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
