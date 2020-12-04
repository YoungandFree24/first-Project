# from django.shortcuts import render, HttpResponse

# # Create your views here.
# def index(request):
#     return HttpResponse("this is the equivalent of @app.route('/')!")

# def one_method(request): # no values passed via url
#     return HttpResponse("getting to the bag")

# def another_method(request, my_val): #my_val would be a number from the u  rl
#     pass                                 # given the example aboute, my_val would be 23

# def yet_another(request, name):	        # name would be a string from the URL
#     pass                                # given the example above, name would be 'pooh'
    
# def one_more(request, id, color): 	# id would be a number, and color a string from the URL
#     pass                                # given the example above, id would be 17 and color would be 'brown'

from django.shortcuts import HttpResponse, redirect
from django.http import JsonResponse
def root_method(request):
    return HttpResponse("String response from root_method")
def another_method(request):
    return redirect("/redirected_route")
def redirected_method(request):
    return JsonResponse({"response": " JSON response from redirected_method", "statis":True})