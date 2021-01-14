from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    my_dict={'insert_me':"Hello, I am from views.py!"}      #This is basically a dictionary where the key is the same as the variable we created in index.html in the template folder
    return render(request,'index.html',context=my_dict)                      #1st parameter is the template we wish to use. 2nd parameter is the actual file, 3rd parameter is the context(This is basically going to link up what we're passing in here, to our index.html file)
# Create your views here.
