from django.shortcuts import render

# Create your views here.


def getbootstrap_download(request):
    return render(request,'getbootstrap_download.html')