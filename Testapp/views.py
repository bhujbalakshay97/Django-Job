from django.shortcuts import render

# Create your views here.
def Index_views(request):
    return render(request,'html/Index.html') 
