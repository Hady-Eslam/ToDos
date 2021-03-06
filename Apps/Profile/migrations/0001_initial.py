# Generated by Django 3.0.5 on 2022-02-08 17:34

import Apps.Profile.models
import Apps.Profile.storages
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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, storage=Apps.Profile.storages.LocalStorage, upload_to=Apps.Profile.models.user_directory_path, verbose_name='Profile Picture')),
                ('bio', models.CharField(blank=True, max_length=100, null=True, verbose_name='Bio')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Birthday Date')),
                ('gender', models.CharField(choices=[('M', 'Male Gender'), ('F', 'Female Gender'), ('U', 'Unknown Gender')], default='U', max_length=2, verbose_name='Gender')),
                ('phone', models.CharField(blank=True, max_length=32, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('zip', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
