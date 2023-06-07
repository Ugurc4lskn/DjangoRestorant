# Generated by Django 4.2.1 on 2023-06-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0011_sitei_letisim_delete_sitebilgileri_delete_siteview_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='breakfast',
            options={'verbose_name': 'kahvaltı', 'verbose_name_plural': 'Kahvaltı'},
        ),
        migrations.AlterModelOptions(
            name='dinner',
            options={'verbose_name': 'akşam yemeği', 'verbose_name_plural': 'Akşam yemeği '},
        ),
        migrations.AlterModelOptions(
            name='ekipmodel',
            options={'verbose_name': 'Ekip', 'verbose_name_plural': 'Ekip Üyeleri'},
        ),
        migrations.AlterModelOptions(
            name='hakkimizda',
            options={'verbose_name': 'Hakkımızda', 'verbose_name_plural': 'Hakkımızda'},
        ),
        migrations.AlterModelOptions(
            name='launch',
            options={'verbose_name': 'öğle', 'verbose_name_plural': 'Öğle yemeği'},
        ),
        migrations.AlterModelOptions(
            name='müsteriler',
            options={'verbose_name': 'Müşteri', 'verbose_name_plural': 'Müşteri Yorumları'},
        ),
        migrations.AlterModelOptions(
            name='siteayarlari',
            options={'verbose_name': 'Ayarlar', 'verbose_name_plural': 'Site Ayarları'},
        ),
        migrations.AlterModelOptions(
            name='sitei̇letisim',
            options={'verbose_name': 'İletişim ', 'verbose_name_plural': 'Site iletişim'},
        ),
        migrations.AddField(
            model_name='sitei̇letisim',
            name='youtube',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='siteayarlari',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='oluşma tarihi'),
        ),
        migrations.AlterField(
            model_name='siteayarlari',
            name='description',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='slider açıklama'),
        ),
        migrations.AlterField(
            model_name='siteayarlari',
            name='navbarTitle',
            field=models.CharField(blank=True, default='', max_length=120, verbose_name='navbar başlık'),
        ),
        migrations.AlterField(
            model_name='siteayarlari',
            name='siteFooterTitle',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Footer başlık'),
        ),
        migrations.AlterField(
            model_name='siteayarlari',
            name='site_title',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='site başlık'),
        ),
        migrations.AlterField(
            model_name='siteayarlari',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Slider başlık'),
        ),
        migrations.AlterField(
            model_name='siteayarlari',
            name='title_image',
            field=models.ImageField(blank=True, default='static/img/menu-2.jpg', upload_to='images/settings/%Y/%m/%d', verbose_name='slider resmi'),
        ),
    ]
