from django.urls import path
from . import views

'''
    In questa sezione vanno creati i percorsi 
    alle nostre pagine web(views.py) all'interno del sito
'''
urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('login/', views.login_user, name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('register/', views.register_user, name='register'),
   path('product/<int:pk>', views.product, name='product'),
   path('category/<str:foo>', views.category, name='category'),
]
