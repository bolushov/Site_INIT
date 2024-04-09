from django.urls import path
from .views import AboutUsView, CooperationListView, KafedraView, KafedraView, KafedraDetailView, EnroleeListView, ContactsView, PhotoGalleryView, ScienceListView, VideoGalleryView, EducationListView

urlpatterns = [
    path('home', KafedraView.as_view(), name='index'),
    path('', KafedraView.as_view(), name='kafedra_list'), 
    path('kafedra/<slug:slug>/', KafedraDetailView.as_view(), name='kafedra_detail'),
    path('enrolees/', EnroleeListView.as_view(), name='enrolee_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
    path('photo-gallery/', PhotoGalleryView.as_view(), name='photo_gallery'),
    path('video-gallery/', VideoGalleryView.as_view(), name='video_gallery'),
    path('education/', EducationListView.as_view(), name='education_list'),
    path('cooperation/', CooperationListView.as_view(), name='cooperation_list'),
    path('science/', ScienceListView.as_view(), name='science_list')
]

