from django.shortcuts import render, redirect, get_object_or_404
from .models import Image
from .forms import ImageForm

def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album:showall')
    else:
        form = ImageForm()
        
        context = {'form':form}
    return render(request, 'album/upload.html', context)


def showall(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'album/showall.html', context)
    
def betails(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'album/betails.html', context)

def edit(request, id):
    image = get_object_or_404(Image, pk=id)
    if request.method == "POST":
        form = ImageForm(request.POST, instance = image)
        if form.is_valid():
            image=form.save(commit=False)
            image.picture=request.FILES['picture']
            image.save()
            return redirect('album:showall')
    imageform = ImageForm(instance = image)
    context = {
        'image':image,
        'imageform': imageform
    }
    return render(request, 'album/edit.html', context)

def delete(request, id):
    image = get_object_or_404(Image, pk=id)
    if request.method == "POST":
            image.delete()
            return redirect('album:showall')
    imageform = ImageForm(instance = image)
    context = {
        'image':image,
        'imageform': imageform
    }
    return render(request, 'album/delete.html', context)