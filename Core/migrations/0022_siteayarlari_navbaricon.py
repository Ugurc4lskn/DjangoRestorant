# Generated by Django 4.2.1 on 2023-06-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0021_hakkimizda_chef'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteayarlari',
            name='navbarIcon',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='navbar icon'),
        ),
    ]