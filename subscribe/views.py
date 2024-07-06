from django.shortcuts import render,redirect
from django.urls import reverse
from subscribe.models import *
from subscribe.forms import *

# Create your views here.
def subscribe(request):
    subscribeform = SubscribeForm()  # Instantiate the form correctly
    email_error = ""
    
    if request.method == 'POST':  # Check if the request method is POST
        subscribeform = SubscribeForm(request.POST)
        
        if subscribeform.is_valid():  # Call is_valid() with parentheses
            
            subscribeform.save()
            return redirect(reverse('thankyou'))
    context = {'form': subscribeform, 'email_error': email_error}
    return render(request, 'subscribe.html', context)

def thankyou(request):
    context={}
    return render(request,'thankyou.html',context)