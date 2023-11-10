# Generated by Django 4.2.7 on 2023-11-09 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FileField(upload_to='video/')),
                ('name', models.CharField(max_length=60)),
                ('likes', models.IntegerField(default=0)),
                ('description', models.TextField(null=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]