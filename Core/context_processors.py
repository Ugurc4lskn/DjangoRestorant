from .models import *


def footer_data(request):
    siteSettings = SiteAyarlari.objects.first()
    iletisim = Siteİletisim.objects.first()
    members = EkipModel.objects.all()

    #Yemek modelleri

    breakfast = Breakfast.objects.all()
    launch = Launch.objects.all()
    dinner = Dinner.objects.all()

    # Kullanıcı yorumları

    yorumlar = Müsteriler.objects.all()

    # Hizmetler

    service = Services.objects.all()

    #Hakkımızda

    about = Hakkimizda.objects.first()

    
    page = SayfaModelleri.objects.all()
    hizmetsüresi = HizmetGünleri.objects.first()

    #contact sayfası model
    contact = ContactSettings.objects.first()

    return {
        'settings': siteSettings,
        'contact': iletisim,
        'teamMembers': members,
        'breakfast':breakfast,
        "launch":launch,
        "dinner":dinner,
        "yorum":yorumlar,
        "services":service,
        "about":about,
        "page":page,
        "hizmet":hizmetsüresi,
        "siteContact":contact


    }