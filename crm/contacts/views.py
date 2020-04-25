from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.db.models.functions import Lower

import os

from .models import Contact
from .forms import ContactForm
from .postcards import send_postcard
from .xls import import_contacts, export_contacts


@login_required(login_url="/login/")
def index(request):
    if request.method == 'POST' and 'document' in request.FILES:
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        import_contacts(fs.url(name)[1:], request.user)
    contact_list = Contact.objects.filter(user=request.user).order_by(
        Lower('first_name'), Lower('last_name'))
    context = {'contact_list': contact_list}
    export = request.GET.get('export', False)
    if export:
        return export_contacts(request.user)
    return render(request, 'index.html', context)


@login_required(login_url="/login/")
def detail(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        try:
            send_postcard(contact, request.POST['postcard_text'])
        except Exception as e:
            return render(request, 'pages/profile.html', {'contact': contact, 'postcard_error': str(e)})
        return render(request, 'pages/profile.html', {'contact': contact, 'postcard_success': True})
    return render(request, 'pages/profile.html', {'contact': contact})


@login_required(login_url="/login/")
def contact_create_view(request):
    form = ContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = form.save(commit=False)
        contact.user = request.user
        contact.save()
        return HttpResponseRedirect(reverse('contacts:detail', args=(contact.id,)))

    return render(request, 'pages/contact_create.html', {'form': form})


def contact_edit_view(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return HttpResponseRedirect(reverse('contacts:detail', args=(contact.id,)))
    else:
        form = ContactForm(instance=contact)
    return render(request, 'pages/contact_create.html', {'form': form, 'contact': contact})


@login_required(login_url="/login/")
def postcard_view(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    send_postcard(contact)
    return HttpResponseRedirect(reverse('contacts:detail', args=(contact.id,)))
