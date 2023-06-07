# Generated by Django 4.2.1 on 2023-06-05 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0015_müsteriler_meslek_alter_breakfast_aciklama_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Hizmet başlık')),
                ('description', models.CharField(max_length=300, verbose_name='Hizmet açıklama')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Hizmetler ',
                'verbose_name_plural': 'Hizmetlerimiz',
            },
        ),
    ]