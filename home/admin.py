from django.contrib import admin
from .models import Cooperation, Education, Kafedra, Science, VideoGallery, PhotoGallery, Enrolee, Contacts, AboutUs, Slide, News, Ad, Events, Director

@admin.register(Kafedra)
class KafedraAdmin(admin.ModelAdmin):
    list_display = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title',)

@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title',)
    list_filter = ('uploaded_at',)
    list_select_related = ()  # Удалите select_related

@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('text',)
    list_filter = ('uploaded_at',)

@admin.register(Enrolee)
class EnroleeAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ('title',)

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ["contact"]
    search_fields = ('contact',)

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ('title',)

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ('title',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "uploaded_at"]
    search_fields = ('title',)
    list_filter = ('uploaded_at',)

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ["title", "uploaded_at"]
    search_fields = ('title',)
    list_filter = ('uploaded_at',)

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ["title", "uploaded_at"]
    search_fields = ('title',)
    list_filter = ('uploaded_at',)

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ('title',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ('title',)


@admin.register(Cooperation)
class CooperationAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ('title',)


@admin.register(Science)
class ScienceAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ('title',)