from django.shortcuts import render , HttpResponse
from .models  import ToDo

def homepage(requests):
    return render(requests, "library.html")

def test(request):
    todo_list =ToDo.objects.all()
    return render(request, "test.html", {"todo_list":todo_list}) 

#def third(requests):
#    return HttpResponse("This is page test3")

def test1(requests):
    return render( requests,"new_test1.html") 

def test2(requests):
    return render(requests, "new_test2.html")

def test3(requests):
    return render(requests, "new_test3.html")                
