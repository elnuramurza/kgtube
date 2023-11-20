# Generated by Django 4.2.7 on 2023-11-20 06:54

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=100, verbose_name='Название канала')),
                ('photo', models.ImageField(blank=True, default='/static/img/avatar.jpg', null=True, upload_to='profile_photo/')),
                ('created_by', models.DateTimeField(auto_now_add=True)),
                ('subscribers', models.ManyToManyField(blank=True, related_name='subscriptions', to=settings.AUTH_USER_MODEL, verbose_name='Подписки')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
