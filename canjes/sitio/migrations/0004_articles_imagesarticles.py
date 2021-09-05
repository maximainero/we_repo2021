# Generated by Django 3.2.6 on 2021-09-05 00:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sitio', '0003_auto_20210824_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_one', models.ImageField(blank=True, null=True, unique=True, upload_to='')),
                ('image_two', models.ImageField(blank=True, null=True, unique=True, upload_to='')),
                ('image_three', models.ImageField(blank=True, null=True, unique=True, upload_to='')),
                ('image_four', models.ImageField(blank=True, null=True, unique=True, upload_to='')),
                ('image_five', models.ImageField(blank=True, null=True, unique=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=2055)),
                ('state', models.IntegerField(default=0)),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.imagesarticles')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
