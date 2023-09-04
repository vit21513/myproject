from django.shortcuts import render

# Create your views here.


def index(request):
    content = {"index": 'Hello people its template rendered'}
    return render(request, "myapp/index.html", content)
