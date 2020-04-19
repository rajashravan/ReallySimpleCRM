from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Contact


def index(request):
    contact_list = Contact.objects.order_by('-first_name')[:5]
    context = {'contact_list': contact_list}
    return render(request, 'contacts/index.html', context)

def detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'pages/profile.html', {'contact': contact})
