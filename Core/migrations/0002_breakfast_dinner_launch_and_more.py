# Generated by Django 4.2.1 on 2023-06-04 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breakfast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(default='', max_length=300)),
                ('aciklama', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('oluşturulma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('fiyat', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
                ('image', models.ImageField(blank=True, default='static/img/menu-1.jpg', upload_to='images/breakfast/%Y/%m/%d', verbose_name='kahvaltı')),
            ],
        ),
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(default='', max_length=300)),
                ('aciklama', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('oluşturulma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('fiyat', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
                ('image', models.ImageField(blank=True, default='static/img/menu-1.jpg', upload_to='images/dinner/%Y/%m/%d', verbose_name='dinner')),
            ],
        ),
        migrations.CreateModel(
            name='Launch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(default='', max_length=300)),
                ('aciklama', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('oluşturulma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('fiyat', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
                ('image', models.ImageField(blank=True, default='static/img/menu-1.jpg', upload_to='images/lauch/%Y/%m/%d', verbose_name='lauch')),
            ],
        ),
        migrations.RenameField(
            model_name='ekipmodel',
            old_name='description',
            new_name='aciklama',
        ),
        migrations.RenameField(
            model_name='ekipmodel',
            old_name='created_at',
            new_name='oluşturulma_tarihi',
        ),
        migrations.AlterField(
            model_name='ekipmodel',
            name='image',
            field=models.ImageField(blank=True, default='static/img/user.jpg', upload_to='images/team/%Y/%m/%d', verbose_name='kullanici'),
        ),
    ]
