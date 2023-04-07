from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView
from classroom.models import Teacher
from classroom.forms import ContactForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thankyou.html'

class TeacherCreateView(CreateView):
    model = Teacher
    #model_form.html
    #.save() 
    fields = "__all__" #Para parametros específicos, usar ["par1", "par2"...]
    success_url  = reverse_lazy('classroom:thankyou')

class TeacherListView(ListView):
    #model_list.html
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')
    
    context_object_name = "teacher_list"

class TeacherDetailView(DetailView):
    # RETURN ONLY ONE MODEL ENTRY PK
    # model_detail.html
    model = Teacher
    # PK --> {{teacher}}



class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # success URL? URL, NOT A TEMPLATE.html
    success_url = reverse_lazy('classroom:thankyou')

    # what to do with form?
    def form_valid(self, form):
        print(form.cleaned_data) #aquí va la acción que se desea
        return super().form_valid(form) # esto raramente cambia