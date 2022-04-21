# Generated by Django 4.0.4 on 2022-04-16 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cardetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carimage', models.ImageField(blank=True, default='', null=True, upload_to='images/')),
                ('carimagefront', models.ImageField(blank=True, default='', null=True, upload_to='images/')),
                ('carimageback', models.ImageField(blank=True, default='', null=True, upload_to='images/')),
                ('carimageleft', models.ImageField(blank=True, default='', null=True, upload_to='images/')),
                ('carimageright', models.ImageField(blank=True, default='', null=True, upload_to='images/')),
                ('carno', models.CharField(default=0, max_length=15)),
                ('ownermobileno', models.IntegerField(default='None', max_length=100)),
                ('carcolor', models.CharField(default='None', max_length=100)),
                ('seatingcapacity', models.IntegerField(default=0, max_length=15)),
                ('onrent', models.CharField(default='No', max_length=100)),
                ('carmodel', models.IntegerField(default=0, max_length=15)),
                ('carcompany', models.CharField(default='XYZ', max_length=100)),
                ('cartype', models.CharField(default='Petrol/Diesel', max_length=100)),
                ('cargears', models.CharField(default='Automatic/Gear', max_length=100)),
                ('priceperday', models.IntegerField(default=0, max_length=15)),
            ],
        ),
    ]
