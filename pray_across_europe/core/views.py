from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import FormView, TemplateView, ListView
from django.urls import reverse_lazy
from .models import Downloads


# Create your views here.


def home(request):
    return render(request, "core/home.html", {'title':'Home'})


def about(request):

    return render(request, "core/about.html", {'title': 'Historia'})


class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.send()
        return super().form_valid(form)


class ContactSuccessView(TemplateView):
    template_name = 'core/success.html'


class DownloadView(ListView):
    model = Downloads
    template_name = 'core/downloads.html'