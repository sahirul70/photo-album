from django.shortcuts import render, redirect
from . models import Category, Photo

# Create your views here.
def index(request):
    category  = request.GET.get('data')
    if category == None:
        photo =  Photo.objects.all()
    else:
        photo =  Photo.objects.filter(category__name=category)

    category = Category.objects.all()
    context = {
        'category':category,
        'photo':photo,
    }
    return render(request,'index.html',context)

def viewPhoto(request, pk):
    photo =  Photo.objects.get(id=pk)
    context={
        'photo':photo,
    }
    return render(request,'photo.html',context)

def addPhoto(request):
    category = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category,created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        photo = Photo.objects.create(
            category = category,
            descriptions = data['descriptions'],
            image = image,
        )
        return redirect('myapp:index')
    context = {
        'category':category,
    }
    return render(request,'add.html',context)