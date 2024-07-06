from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def upload_addimage(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
    else:
        form = UploadForm()
    context={'form':form}
    return render(request,'image.html',context)

    