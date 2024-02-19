from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
    
    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
    
    contact.save()
    
    send_mail(
        email,
        'Imóvel:  ' + listing + '                          Telefone:  ' + phone + '                                                                    Mensagem:  ' + message,
        name,
        ['cjimoveisbrasilia@gmail.com', ],
        fail_silently=False
    )
    
    messages.success(request, 'Mensagem enviada! Em breve entraremos em contato.' )
    
    return redirect('/listings/'+listing_id)

