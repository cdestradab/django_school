from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView

from classroom.forms import ContactForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thankyou.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # success URL? URL, NOT A TEMPLATE.html
    success_url = reverse_lazy('classroom:thankyou')

    # what to do with form?
    def form_valid(self, form):
        print(form.cleaned_data) #aquí va la acción que se desea
        return super().form_valid(form) # esto raramente cambia