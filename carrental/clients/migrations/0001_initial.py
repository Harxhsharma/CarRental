# Generated by Django 4.0.4 on 2022-04-16 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carnumber', models.CharField(default='No', max_length=100)),
                ('fromm', models.DateField(default='')),
                ('to', models.DateField(default='')),
                ('bookedcar', models.CharField(default='No', max_length=100)),
                ('user', models.OneToOneField(default='None', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
