# Generated by Django 4.2.1 on 2023-06-07 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0034_contactsettings_useri_letisim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactsettings',
            name='location',
            field=models.TextField(blank=True, default='', help_text='Restorant konumu iframe içinde bulunan src linki http://embedgooglemaps.com/en/', null=True, verbose_name='Konum embed linki '),
        ),
    ]