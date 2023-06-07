from django.db import models

class EkipModel(models.Model):
    adi = models.CharField(max_length=100, default='')
    soyadi = models.CharField(max_length=100, default='')
    aciklama = models.CharField(max_length=200, default='', blank=True, null=True)
    oluşturulma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        verbose_name='kullanici',
        upload_to='images/team/%Y/%m/%d',
        default='static/img/user.jpg',
        blank=True
    )
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    
    
    class Meta:
        verbose_name = 'Ekip'
        verbose_name_plural = 'Ekip Üyeleri'

    def __str__(self):
        return self.adi
    

    

class Breakfast(models.Model):
    isim = models.CharField(max_length=300, default='')
    aciklama = models.CharField(max_length=100, default='', blank=True, null=True)
    oluşturulma_tarihi = models.DateTimeField(auto_now_add=True)
    fiyat = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    image = models.ImageField(
        verbose_name='kahvaltı',
        upload_to='images/breakfast/%Y/%m/%d',
        default='static/img/menu-1.jpg',
        blank=True
    )


    class Meta:
        verbose_name = 'kahvaltı'
        verbose_name_plural = 'Kahvaltı'


    def __str__(self):
        return self.isim

class Launch(models.Model):
    isim = models.CharField(max_length=300, default='')
    aciklama = models.CharField(max_length=700, default='', blank=True, null=True)
    oluşturulma_tarihi = models.DateTimeField(auto_now_add=True)
    fiyat = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    image = models.ImageField(
        verbose_name='lauch',
        upload_to='images/lauch/%Y/%m/%d',
        default='static/img/menu-1.jpg',
        blank=True
    )

    class Meta:
        verbose_name = 'öğle'
        verbose_name_plural = 'Öğle yemeği'

    def __str__(self):
        return self.isim
    


class Dinner(models.Model):
    isim = models.CharField(max_length=300, default='')
    aciklama = models.CharField(max_length=700, default='', blank=True, null=True)
    oluşturulma_tarihi = models.DateTimeField(auto_now_add=True)
    fiyat = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    image = models.ImageField(
        verbose_name='dinner',
        upload_to='images/dinner/%Y/%m/%d',
        default='static/img/menu-1.jpg',
        blank=True
    )


    class Meta:
        verbose_name = 'akşam yemeği'
        verbose_name_plural = 'Akşam yemeği '
    def __str__(self):
        return self.isim
    

class Müsteriler(models.Model):
    isim = models.CharField(max_length=300, default='')
    aciklama = models.CharField(max_length=200, default='', blank=True, null=True)
    oluşturulma_tarihi = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        verbose_name='users',
        upload_to='images/user/%Y/%m/%d',
        default='static/img/user.jpg',
        blank=True
    )

    meslek = models.CharField(max_length=100, default="", blank=True, null=True)


    class Meta:
        verbose_name = 'Müşteri'
        verbose_name_plural = 'Müşteri Yorumları'

    def __str__(self):
        return self.isim
    





class Hakkimizda(models.Model):
    title = models.CharField(max_length=255, default='')
    title_icon = models.CharField(max_length=255, default='', blank=True,null=True)
    description = models.CharField(max_length=350, blank=True, null=True, default='')
    experience  = models.IntegerField(default=1, blank=True, null=True)
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    chef = models.IntegerField(default=2, verbose_name="Şef sayısı")

    start1 = models.ImageField(
        verbose_name='İlk 1',
        upload_to='images/about/%Y/%m/%d',
        default='static/img/menu-1.jpg',
        blank=True
    )
    start2 = models.ImageField(
        verbose_name='ilk 2',
        upload_to='images/about/%Y/%m/%d',
        default='static/img/menu-1.jpg',
        blank=True
    )

    end1 = models.ImageField(
        verbose_name='Son 1',
        upload_to='images/about/%Y/%m/%d',
        default='static/img/menu-1.jpg',
        blank=True
    )
    end2 = models.ImageField(
        verbose_name='Son 2',
        upload_to='images/about/%Y/%m/%d',
        default='static/img/menu-1.jpg',
        blank=True
    )

    icon = models.CharField(
        verbose_name="Hakkımızda iconu",
        max_length=100,
        default="",
        blank=True,
        null=True
    )
    

    def __str__(self):
        return self.description
    


    class Meta:
        verbose_name = 'Hakkımızda'
        verbose_name_plural = 'Hakkımızda'




class SiteAyarlari(models.Model):
    WindowTitle = models.CharField(max_length=39, help_text='Site pencere başlığı', default='Restorant', verbose_name='Site pencere başlığı')
    windowIcon = models.ImageField(
        verbose_name='Site pencere iconu',
        upload_to='images/site/%Y/%m/%d',
        blank=True
    )

    navbarTitle = models.CharField(max_length=120, default='', blank=True, verbose_name='navbar başlık')
    navbarIcon = models.CharField(max_length=100, blank=True,null=True, verbose_name='navbar icon')
    
    title = models.CharField(max_length=100, default='', blank=True, null=True, verbose_name='Slider başlık')
    description = models.CharField(max_length=300, default='', blank=True, verbose_name='slider açıklama')
    title_image = models.ImageField(
        verbose_name='slider resmi',
        upload_to='images/settings/%Y/%m/%d',
        default='static/img/menu-2.jpg',
        blank=True
    )
    date_time = models.DateTimeField(auto_now_add=True, verbose_name="oluşma tarihi")

    footerTitle  = models.CharField(max_length=200, default='', blank=True, verbose_name="Footer Başlık")
    footerDescription = models.CharField(max_length=200, default='', blank=True, verbose_name="Footer açıklama")

    class Meta:
        verbose_name = 'Ayarlar'
        verbose_name_plural = 'Site Ayarları'


    def __str__(self) -> str:
        return self.title

class Siteİletisim(models.Model):
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    youtube = models.URLField(blank=True, null=True)
   

    adres = models.CharField(max_length=120, default='' ,blank=True, null=True)
    telefon = models.CharField(max_length=20, default='', blank=True, null=True)
    email = models.EmailField(max_length=100, default='',blank=True, null=True)

    oluşturulma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'İletişim '
        verbose_name_plural = 'Site iletişim'


    def __str__(self) -> str:
        return self.adres





class Services(models.Model):
    title = models.CharField(max_length=100, verbose_name="Hizmet başlık")
    description = models.CharField(max_length=300, verbose_name="Hizmet açıklama")
    icon = models.CharField(max_length=300, verbose_name='hizmet başlık iconu', help_text='Hizmet başlık icon adı https://icons.getbootstrap.com/', default='bi bi-people')
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Hizmetler '
        verbose_name_plural = 'Hizmetlerimiz'

    
    def __str__(self) -> str:
        return self.title
    

class Reservations(models.Model):
    isim = models.CharField(max_length=200, unique=True)
    soyisim = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    kisi_sayisi = models.IntegerField()
    rezervationtarihi = models.DateTimeField(blank=True,null=True)
    oluşturulma_tarihi = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    ekİstek = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.isim



class SayfaModelleri(models.Model):
    title = models.CharField(max_length=100, verbose_name="Sayfa ismi")
    link = models.URLField()
    
    class Meta:
        
        verbose_name = 'Sayfalar'
        verbose_name_plural = 'Sayfalar'

    def __str__(self) -> str:
        return self.title
    

class HizmetGünleri(models.Model):
    openDate = models.CharField(max_length=210, verbose_name='Açılış günü', help_text="Restorantın açılış günü")
    closeDate = models.CharField(max_length=210, verbose_name='Kapanış günü', help_text="Restorantın kapanış günü")
    timeOpen = models.TimeField(blank=True, verbose_name='Açılış saati', help_text="Kapanış saati")
    timeClose = models.TimeField(blank=True, verbose_name='Kapanış saati', help_text="Açılış saati")


    class Meta:
        verbose_name = 'Hizmet Günleri'
        verbose_name_plural = 'Hizmet Günleri'


    def __str__(self) -> str:
        return self.openDate
    



class Userİletisim(models.Model):
    isim = models.CharField(max_length=200, default="")
    soyisim = models.CharField(max_length=120, default="")
    baslik = models.CharField(max_length=122, default="")
    mesaj = models.TextField(default="")

    class Meta:
        verbose_name = 'kullanıcı iletişim'
        verbose_name_plural = 'Kullanıcı iletişim'

    
class ContactSettings(models.Model):
    eposta1Title = models.CharField(
       max_length=100,
       default="",
       blank=True
   )
    eposta1Mail = models.EmailField(default="", null=True, blank=True)

    eposta2Title = models.CharField(
       max_length=100,
       default="",
       blank=True
   )
    eposta2Mail = models.EmailField(default="", null=True, blank=True)

    eposta3Title = models.CharField(
       max_length=100,
       default="",
       blank=True
   )
    eposta3Mail = models.EmailField(default="", null=True, blank=True)

    location = models.URLField(verbose_name="Konum embed linki ", help_text='Restorant konumu iframe içinde bulunan src linki http://embedgooglemaps.com/en/', blank=True, default="", null=True)
    
    class Meta:
        verbose_name = 'İletişim Ayarları'
        verbose_name_plural = 'İletişim Ayarları'


    def __str__(self) -> str:
        return ''


