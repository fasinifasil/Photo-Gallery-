from django.shortcuts import render,redirect
from .models import Category,Photo

# Create your views here.
def GalleryFunction(request):
    category = request.GET.get('category')
    if category==None:
        photos = Photo.objects.all()

    else:
        photos = Photo.objects.filter(category__name=category)

    categories  =Category.objects.all()

    context={'key':categories,'key1':photos}
    return render(request,'Gallery.html',context)
def UploadFunction(request):

    categories = Category.objects.all()
    if request.method == 'POST':
        data=request.POST
        image=request.FILES.get('image')

        if data['category'] != 'none':
            category=Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category,created=Category.objects.get_or_create(name=data['category_new'])
        else:
            category=None
        photo =Photo.objects.create(category=category,description=data['description'],image=image)
        return redirect('Gallery')

    context = {'key': categories}
    return render(request,'Upload.html',context)





def PhotoFunction(request,pk):
    photos = Photo.objects.get(id=pk)


    return render(request,'Photo.html',{'key2':photos})
