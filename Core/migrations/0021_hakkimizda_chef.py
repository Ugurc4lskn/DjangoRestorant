# Generated by Django 4.2.1 on 2023-06-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0020_hakkimizda_title_hakkimizda_title_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='hakkimizda',
            name='chef',
            field=models.IntegerField(default=2, verbose_name='Şef sayısı'),
        ),
    ]