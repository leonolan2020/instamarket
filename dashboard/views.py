from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
def getContext(request,*args, **kwargs):
    context={}
    context['title']="Insta-Market"
    context['message']="Hello to my home page !!"
    return context
class IndexView(View):
    def home(self, request, *args, **kwargs):
        context=getContext(request=request)
        return render(request,'index.html',context)
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET request!')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
