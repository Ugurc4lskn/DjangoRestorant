from django.shortcuts import redirect, render, HttpResponse

from Core.forms import ReservationForm, ReservationQuery, ContactForm
from .models import (
    EkipModel,
    Reservations,
    Userİletisim
)
import datetime

from django.contrib import messages



def convertDatetime(reservationTime):
    datetime_obj = datetime.datetime.fromisoformat(str(reservationTime))
    formatted_date = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date

def index(request) -> HttpResponse:
    return render(request=request, template_name="index.html",)


def about(request) -> HttpResponse:
    return render(request=request, template_name="about.html")


def menü(request) -> HttpResponse:
    return render(request=request, template_name="menu.html")


def reservation(request) -> HttpResponse:
    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid() :
            date = convertDatetime(form.cleaned_data.get('date_field'))
            name = form.cleaned_data.get('name')
            lastName = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            kisiSayisi = form.cleaned_data.get('kisi')
            special = form.cleaned_data.get('specialRequest')

            if not Reservations.objects.filter(isim=name, soyisim=lastName, email=email).first():
                reservation = Reservations(
                    isim=name,
                    soyisim=lastName,
                    email=email,
                    kisi_sayisi=kisiSayisi,
                    rezervationtarihi=date,
                    ekİstek=special
                )
                reservation.save()

                messages.success(request, 'Rezervasyonunuz başarıyla kaydedildi')
                return redirect(request.path)
            else:
                messages.error(request, 'Bu e-posta adresi ile rezervasyon yapılamaz')
                return redirect(request.path)

        else:
            return redirect(request.path)
        
    else:
        form = ReservationForm(request.POST)
        context = {
            'form': form
        }
        return render(request=request, template_name="reservation.html", context=context)


def team_view(request) -> HttpResponse:
    teamMember = EkipModel.objects.all()

    context = {
        "team":teamMember
    }
    return render(request=request, template_name="team.html", context=context)


def contact(request) -> HttpResponse:
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            lastName = form.cleaned_data.get('lastname')
            baslik = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            contact = Userİletisim(
                    isim=name,
                    soyisim=lastName,
                    baslik=baslik,
                    mesaj=content
                )
            contact.save()

            messages.success(request, 'Mesajınız başarıyla gönderildi')
            return redirect(request.path)
        
        else:

            return redirect(request.path)
    else:
        form = ContactForm()
        return render(request=request, template_name="contact.html", context={"form":form})


def services_view(request) -> HttpResponse:
    return render(request=request, template_name="service.html")



def user_comments(request) -> HttpResponse:
    return render(request=request, template_name="users.html")


def reservation_query(request) -> HttpResponse:
    query: bool

    if request.method == "POST":
        form = ReservationQuery(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            lastName = form.cleaned_data.get('last_name')
            print(name, lastName)
            query = Reservations.objects.filter(isim=name, soyisim=lastName)
            if query:
                query = True
        
            return render(request=request, template_name="reservationQuery.html", context={"query": query, "form":form})
                
        else:
            return redirect(request.path)
    

    else:
        form = ReservationQuery(request.POST)
        return render(request=request, template_name="reservationQuery.html", context={"form": form})
    