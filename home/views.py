from django.views.generic import ListView, DetailView, TemplateView
from .models import AboutUs, Ad, Director, Events, Kafedra, Enrolee, Contacts, Slide, News, PhotoGallery, VideoGallery, Education, Cooperation, Science


class KafedraView(ListView):
    model = Kafedra
    template_name = "index.html"  # Путь к вашему шаблону

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kafedras'] = Kafedra.objects.all()
        context['slides'] = Slide.objects.all()
        context['news_info'] = News.objects.all()
        context['ads_info'] = Ad.objects.all()
        context['events_info'] = Events.objects.all()
        context['director_info'] = Director.objects.all()
        context['photo_info'] = PhotoGallery.objects.all()
        context['video_info'] = VideoGallery.objects.all()
        return context


class KafedraDetailView(DetailView):
    model = Kafedra
    template_name = 'kafedra_detail.html'  # Create this template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kafedra'] = Kafedra.objects.all()
        return context
    

class EnroleeListView(ListView):
    model = Enrolee
    context_object_name = 'enrolees'
    template_name = 'abiturient.html'


class ContactsView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_info'] = Contacts.objects.first()  # Получаем первый объект из модели Contacts
        return context
    


class AboutUsView(TemplateView): 
    template_name = 'o_nas.html'  # Указываем шаблон
   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_info'] = AboutUs.objects.all()  # Получаем все объекты из модели AboutUs
        return context

class PhotoGalleryView(ListView):
    model = PhotoGallery
    template_name = 'fotogallery.html'
    context_object_name = 'photos'



class VideoGalleryView(ListView):
    model = VideoGallery
    template_name = 'videogallery.html'
    context_object_name = 'videos'


    
class EducationListView(ListView):
    model = Education
    context_object_name = 'educations'
    template_name = 'obrazovanie.html'


class CooperationListView(ListView):
    model = Cooperation
    context_object_name = 'cooperations'
    template_name = 'sotrudnich.html'


class ScienceListView(ListView):
    model = Science
    context_object_name = 'sciences'
    template_name = 'nauka.html'