from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class ReservationForm(forms.Form):
    name = forms.CharField(label='Adınız', min_length=2, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınız', 'name':'isim'}), required=True)
    last_name = forms.CharField(label='Soyadınız',  min_length=2 ,max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyadınız', 'name':'soyad'}), required=True)
    email = forms.CharField(label='Email', min_length=2, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eposta adresiniz', 'name':'email'}), required=True)
    kisi = forms.CharField(label='Kişi Sayısı', min_length=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Kişi sayısı', 'name':'user'}), required=True)
    specialRequest = forms.CharField(label='Kişi Sayısı',  min_length=1 , max_length=200, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Varsa spesifik bir isteğiniz', 'name':'specialrequest'}), required=False)
    date_field = forms.DateTimeField(label='Randevu tarihi ', widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    

    
    def clean(self):
        cleaned_data = super(ReservationForm, self).clean()
        name = cleaned_data.get('name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        kisi = cleaned_data.get('kisi')
        specialRequest = cleaned_data.get('specialRequest')
        date_field = cleaned_data.get('date_field')
        if name == '':
            self.add_error('name', 'Adınız boş bırakılamaz')
            return False
        if last_name == '':
            self.add_error('last_name', 'Soyadınız boş bırakılamaz')
            return False
        if email == '':
            self.add_error('email', 'Email boş bırakılamaz')
            return False
        if kisi == '':
            self.add_error('kisi', 'Kişi sayısı boş bırakılamaz')
            return False
        if date_field == '':
            self.add_error('date_field', 'Randevu tarihi boş bırakılamaz')
            return False
        
        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' not in email:
            self.add_error('email', 'Geçerli bir email adresi giriniz')
            return False
        return email

    

        



class ReservationQuery(forms.Form):
    name = forms.CharField(label='Adınız', min_length=2, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınız', 'name':'isim'}), required=True)
    last_name = forms.CharField(label='Soyadınız',  min_length=2 ,max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyadınız', 'name':'soyad'}), required=True)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
   
    
    def clean(self):
        cleaned_data = super(ReservationQuery, self).clean()
        name = cleaned_data.get('name')
        last_name = cleaned_data.get('last_name')
        if name == '':
            self.add_error('name', 'Adınız boş bırakılamaz')
            return False
        if last_name == '':
            self.add_error('last_name', 'Soyadınız boş bırakılamaz')
            return False
        
        return cleaned_data
  
    


class ContactForm(forms.Form):
    name = forms.CharField(label='Adınız', min_length=2, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınız', 'name':'isim'}), required=True)
    lastname = forms.CharField(label='Soyadınız', min_length=2, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyadınız', 'name':'lastname'}), required=True)
    title = forms.CharField(label='Başlık', min_length=2, max_length=120, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Başlık', 'name':'baslik'}), required=True)
    content = forms.CharField(label='Mesajınız', min_length=2, max_length=100, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mesajınız', 'name':'icerik'}), required=True)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        lastname = cleaned_data.get('lastname')
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if name == '':
            self.add_error('name', 'Adınız boş bırakılamaz')
            return False
        if lastname == '':
            self.add_error('lastname', 'Soyadınız boş bırakılamaz')
            return False
        if title == '':
            self.add_error('title', 'Başlık boş bırakılamaz')
            return False
        if content == '':
            self.add_error('content', 'Mesajınız boş bırakılamaz')
            return False
        
        return cleaned_data



  
    