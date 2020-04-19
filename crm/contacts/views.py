from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Contact
from .forms import ContactForm

@login_required(login_url="/login/")
def index(request):
    contact_list = Contact.objects.order_by('first_name')
    context = {'contact_list': contact_list}
    return render(request, 'index.html', context)

@login_required(login_url="/login/")
def detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'pages/profile.html', {'contact': contact})


def contact_create_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        contact = form.save(commit=False)
        contact.user = request.user
        contact.save()
        return HttpResponseRedirect(reverse('contacts:detail', args=(contact.id,)))

    return render(request, 'pages/contact_create.html', {'form': form})

def contact_edit_view(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return HttpResponseRedirect(reverse('contacts:detail', args=(contact.id,)))
    else:
        form = ContactForm(instance=contact)
    return render(request, 'pages/contact_create.html', {'form': form})
