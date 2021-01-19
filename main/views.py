from django.shortcuts import render , HttpResponse

def homepage(requests):
    return render(requests, "library.html")

def test(requests):
    return render(requests, "test.html") 

def third(requests):
    return HttpResponse("This is page test3")       
