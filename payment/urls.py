from django.urls import path
from . import views

'''
    In questa sezione vanno creati i percorsi 
    alle nostre pagine web(views.py) all'interno del sito
'''
urlpatterns = [
   path('payment_success/', views.payment_success, name='payment_success'),
   path('checkout/', views.checkout, name='checkout'),
   path('billing_info/', views.billing_info, name='billing_info'),
]
