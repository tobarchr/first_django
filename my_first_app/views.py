from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def root(request):
    return redirect("/blogs")
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect("/")
def show(request,number):
    return HttpResponse("placeholder for display blog number: " + str(number))
def edit(request,number):
    return HttpResponse("placeholder to edit blog: "+ str(number))
def destroy(request,number):
    return redirect("/")
def json_text(request):
    return JsonResponse({"title":"My first blog","content":"loreIn enim incididunt excepteur Lorem eu magna ex magna ipsum ad dolor aliquip id."})
# Create your views here.
