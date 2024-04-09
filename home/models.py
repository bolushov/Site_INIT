from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Kafedra(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название кафедры", null=True)
    slug = models.SlugField(unique=True, blank=True)
    text = RichTextField(null=True, blank=True, verbose_name="Текст")


    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('kafedra_detail', kwargs={'slug': self.slug})
    
class Enrolee(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True, verbose_name="Абитуриент")
    text = RichTextField(null=True, blank=True, verbose_name="Текст")

    class Meta:
        verbose_name = "Абитуриент"
        verbose_name_plural = "Абитуриенты"

    def __str__(self):
        return self.title
    


class Contacts(models.Model):
    contact = RichTextField(null=True, blank=True, verbose_name="Текст")

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.contact
    

class AboutUs(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True, verbose_name="О нас")
    text = RichTextField(null=True, blank=True, verbose_name="Текст")

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

    def __str__(self):
        return self.title if self.title else ""  # Возвращаем title, если он не пустой, иначе возвращаем пустую строку
    

class Slide(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название", null=True, blank=True)
    slide = models.ImageField(upload_to='slide_image/', verbose_name="фотки для слайдера", blank=True, null=True)
 
    
    class Meta: 
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"

    def __str__(self):  
        return self.title
    



class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название", null=True, blank=True)  
    news_image = models.ImageField(upload_to='news_image/', verbose_name="фотки для новости", blank=True, null=True)  
    text = models.TextField(null=True, blank=True, verbose_name="Текст")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title if self.title else 'No title provided'
    



class Ad(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название", null=True, blank=True)
    ads_image = models.ImageField(upload_to='ads_image/', verbose_name="фотки для объявления", blank=True, null=True)
    text = models.TextField(null=True, blank=True, verbose_name="Текст")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")


    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


        def __str__(self):
            return self.title if self.title else 'No title provided'
        

class Events(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название", null=True, blank=True)
    events_image = models.ImageField(upload_to='events_image/', verbose_name="фотки для события", blank=True, null=True)
    text = models.TextField(null=True, blank=True, verbose_name="Текст")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")


    class Meta:
        verbose_name = "События"
        verbose_name_plural = "События"

    def __str__(self):
        return self.title if self.title else 'No title provided'
    


class Director(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название", null=True, blank=True)
    director_image = models.ImageField(upload_to='director_image/', verbose_name="фотки для директора", blank=True, null=True)
    text = RichTextField(null=True, blank=True, verbose_name="Текст")

    class Meta:
        verbose_name = "Директор"
        verbose_name_plural = "Директоры"

        def __str__(self):
            return self.title if self.title else 'No title provided'


class PhotoGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название", null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    photo = models.ImageField(upload_to='photos/', verbose_name="Изображение")
    text = models.TextField(blank=True, verbose_name="Текст для фото")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return self.title if self.title else 'No title provided'



class VideoGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название", blank=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    video_file = models.FileField(upload_to='videos/', verbose_name="Видеофайл", blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', verbose_name="Обложка", blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True, verbose_name="Образование")
    text = RichTextField(null=True, blank=True, verbose_name="Текст")

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образование"

    def __str__(self):
        return self.title
    


class Cooperation(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True, verbose_name="Cотрудничество")
    text = RichTextField(null=True, blank=True, verbose_name="Текст")

    class Meta:
        verbose_name = "Cотрудничество"
        verbose_name_plural = "Cотрудничество"

    def __str__(self):
        return self.title
    


class Science(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True, verbose_name="Наука")
    text = RichTextField(null=True, blank=True, verbose_name="Текст")

    class Meta:
        verbose_name = "Наука"
        verbose_name_plural = "Наука"

    def __str__(self):
        return self.title
      
    