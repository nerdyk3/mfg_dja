from django.shortcuts import render
from .models import blog

def index(request):
	blog_var = blog.objects.all()
	return render(request,'myfirstapp/index.html',{'blog_kun':blog_var})
