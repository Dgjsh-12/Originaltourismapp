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
    imageForm = ImageForm(instance=image)
    context = {
        'image':image,
        'imageform': imageForm
    }
    return render(request, 'album/edit.html', context)
    
def delete(request, id):
    image = get_object_or_404(Image, pk=id)
    image.delete()
    imageForm = ImageForm(instance=image)
    context = {'image':image}
    return render(request, 'album/betails.html', context)