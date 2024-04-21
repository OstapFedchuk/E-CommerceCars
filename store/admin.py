from django.contrib import admin
from .models import Category, Customer, Product, Order, Profile
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Profile)

#Facciamo un MIX tra info del profile e info del user
class ProfileInLine(admin.StackedInline):
    model = Profile


#Estensione del User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name", "email"]
    inlines = [ProfileInLine]

#Deimplemento la registrazione old-style
admin.site.unregister(User)

#Implemento la registrazione nuova (new-style)
admin.site.register(User, UserAdmin)
