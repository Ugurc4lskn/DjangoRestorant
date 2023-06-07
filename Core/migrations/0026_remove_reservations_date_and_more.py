# Generated by Django 4.2.1 on 2023-06-05 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0025_reservations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservations',
            name='date',
        ),
        migrations.AddField(
            model_name='reservations',
            name='oluşturulma_tarihi',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reservations',
            name='rezervationtarihi',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]