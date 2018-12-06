from django.http import HttpResponse
from django.shortcuts import render, redirect

# One of the view Controlers
# Request parameter return a response object


def map(request):
    return render(request, 'index.html')


# currently redirect to the account log in page but in the future we might change it
# def login_redirect(request):
#     return redirect('/account')
