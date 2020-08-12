from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .repo import MainSliderRepo


TEMPALTE_ROOT='dashboard/'

def getContext(request,*args, **kwargs):
    context={}
    context['title']="Insta-Market"
    context['message']="Hello! Welcome to my home page !!"
    return context
class IndexView(View):
    def home(self, request, *args, **kwargs):
        context=getContext(request=request)
        context['main_sliders']=MainSliderRepo().list()
        return render(request,TEMPALTE_ROOT+'index.html',context)
    def search(self, request, *args, **kwargs):
        context=getContext(request=request)
        context['main_sliders']=MainSliderRepo().list()
        return render(request,TEMPALTE_ROOT+'index.html',context)
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET request!')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
