from django.contrib import admin
from django.urls import path
from .views import Home, About, Upload, login_user, signup_user, logout_user, show_product, addtowish, show_wishlist, removewish, show_cart, addtocart, removeCart, show_data
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', Home, name="home"),
    path('about', About, name="about"),
    path('upload', Upload , name='upload'),
    path('login', login_user , name='login'),
    path('signup', signup_user , name='signup'),
    path('logout', logout_user , name='logout'),
    path('product/<int:id>', show_product , name='product'),
    path('addtowish/<int:id>', addtowish, name ='addtowish'),
    path('addtocart/<int:id>', addtocart, name ='addtocart'),
    path('wishlist', show_wishlist, name = "show_wishlist"),
    path('removewish/<int:id>', removewish, name = 'removewish'),
    path('show_cart', show_cart, name = 'show_cart'),
    path('removeCart/<int:id>', removeCart, name = 'removeCart'),
    path('dummy', show_data, name = 'dummy')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
