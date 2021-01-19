from django.shortcuts import render , HttpResponse

def homepage(requests):
    return HttpResponse("Hi Zag!")

def test(requests):
    return render(requests, "test.html")    
