from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from . models import *
from .import auth_views
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='loginUser')
def home(request):
    user = request.user
    category = request.GET.get('category')
    
    if category:
        photos = Photo.objects.filter(user = user, category__name=category)
        selected_category = category
    else:
        photos = Photo.objects.filter(user=user)
        selected_category = None
        
    categories = Category.objects.all()
    context = {"photos": photos, 'categories': categories, 'selected_category': selected_category}
    
    return render(request, 'home.html', context)

@login_required(login_url='loginUser')
def addPhoto(request):
    user = request.user
    categories = Category.objects.all()
    # categories = user.category_set.all()
    
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image', '')
        
        if data['category'] != 'none':
            category = Category.objects.get(id = data['category'])
        elif data['new_category'] != '':
            category = Category.objects.get_or_create(name=data['new_category'])
        else:
            category = None
            
        if isinstance(category, tuple):
            category = category[0]
            
        photos = Photo.objects.create(
            category = category,
            image = image,
            description = data['description'],
            user=user
        )    
        
        return redirect('home')
    
    context = {'categories': categories}
    return render(request, 'addPhoto.html', context)


@login_required(login_url='loginUser')
def photo(request, pk):
    user = request.user
    photos = Photo.objects.get(id = pk, user=user)
    
    context = {'photos': photos}
    return render(request, 'photo.html', context)

def deletePhoto(request, pk):
    photo = get_object_or_404(Photo, id = pk, user=request.user)
    photo.delete()
    
    return redirect('home')