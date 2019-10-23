from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'basic_app'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('register/',views.register,name='register'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('menu/',views.menu,name='menu'),
    path('menu/food_details',views.food_details,name='food_details'),
    path('menu/payment/',views.payment,name='payment'),
    path('user_login/',views.user_login,name='user_login'),
]
