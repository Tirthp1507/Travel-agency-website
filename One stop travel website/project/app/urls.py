from app import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('login', views.loginUser, name='login'),
    path('signup', views.signupUser, name='signup'),
    path('about', views.about, name='about'),
    path('chardham', views.chardham, name='chardham'),
    path('ad', views.ad, name='ad'),
    path('amritsar', views.amritsar, name='amritsar'),
    path('kerala', views.kerala, name='kerala'),
    path('ladakh', views.ladakh, name='ladakh'),
    path('lakshdweep', views.lakshdweep, name='lakshdweep'),
    path('manali', views.manali, name='manali'),
    path('hp', views.hp, name='hp'),
    path('goa', views.goa, name='goa'),
    path('uttarakhand', views.uttarakhand, name='uttarakhand'),
    path('udaipur', views.udaipur, name='udaipur'),    
    path('logout', views.logoutUser, name='logoutUser'),    
]