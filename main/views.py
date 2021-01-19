from django.shortcuts import render , HttpResponse

def homepage(requests):
    return HttpResponse("Hi Zag!")

def test(requests):
    return render(requests, "test.html") 

def third(requests):
    return HttpResponse("This is page test3")       
