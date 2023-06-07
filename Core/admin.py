from django.contrib import admin
from .models import *


from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()

@admin.register(ContactSettings)
class ContactSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'eposta1Title', 'eposta1Mail', 'location')

@admin.register(Userİletisim)
class ContactSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'isim', 'soyisim', 'baslik')

@admin.register(EkipModel)
class EkipModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'adi', 'soyadi')
    search_fields = ('adi', 'soyadi')
    list_filter = ('adi', 'soyadi')
    ordering = ('adi', 'soyadi')
    list_per_page = 10

@admin.register(Breakfast)
class BreakfastAdmin(admin.ModelAdmin):
    list_display = ('id', 'isim', 'aciklama')
    search_fields = ('isim', 'aciklama')
    list_filter = ('isim', 'aciklama')
    ordering = ('isim', 'aciklama')
    list_per_page = 10

@admin.register(Launch)
class LaunchAdmin(admin.ModelAdmin):
    list_display = ('id', 'isim', 'aciklama')
    search_fields = ('isim', 'aciklama')
    list_filter = ('isim', 'aciklama')
    ordering = ('isim', 'aciklama')
    list_per_page = 10

@admin.register(Dinner)
class DinnerModel(admin.ModelAdmin):
    list_display = ('id', 'isim', 'aciklama')
    search_fields = ('isim', 'aciklama')
    list_filter = ('isim', 'aciklama')
    ordering = ('isim', 'aciklama')
    list_per_page = 10


@admin.register(Müsteriler)
class MüsteriAdmin(admin.ModelAdmin):
    list_display = ('id', 'isim', 'aciklama', 'oluşturulma_tarihi')
    search_fields = ('isim', 'aciklama')
    list_filter = ('isim', 'aciklama')
    ordering = ('isim', 'aciklama')
    list_per_page = 10



@admin.register(Hakkimizda)
class hakkimizdaModel(admin.ModelAdmin):
    list_display = ('id', 'description', 'experience', 'olusturulma_tarihi')




@admin.register(SiteAyarlari)
class SiteayarlariModel(admin.ModelAdmin):
    list_display = ('id', 'navbarTitle', 'title', 'description','title_image')
    search_fields = ('navbarTitle',)




@admin.register(Siteİletisim)
class iletisim(admin.ModelAdmin):
    list_display = ('id', 'twitter', 'facebook', 'instagram','adres')
    

@admin.register(Services)
class hizmetler(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title', 'description')


    
@admin.register(Reservations)
class rezervasyon(admin.ModelAdmin):
    list_display = ('id', 'isim', 'soyisim', 'email', 'rezervationtarihi')
    search_fields = ('isim', 'soyisim', 'email')
    list_filter = ('isim', 'soyisim', 'email')
    ordering = ('isim', 'soyisim', 'email')
    list_per_page = 10


@admin.register(SayfaModelleri)
class sayfaModelleri(admin.ModelAdmin):
    list_display = ('id', 'title', 'link')


@admin.register(HizmetGünleri)
class hizmetGünleri(admin.ModelAdmin):
    list_display = ('id', 'openDate', 'closeDate')
    search_fields = ('openDate', 'closeDate')
    
