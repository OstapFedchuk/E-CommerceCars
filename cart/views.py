from django.shortcuts import render, redirect


def cart_summary(request):
    return render(request, 'car_summary.html', {})


def cart_add(request):
    pass


def cart_delete(request):
    pass


def cart_update(request):
    pass

