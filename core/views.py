from django.shortcuts import render, redirect

from item.models import category, Item

from .forms import SignupForm

def index(request):
    #information about browser, IP  address, get/post request
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = category.objects.all()
    
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
        
    form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

# Create your views here.
