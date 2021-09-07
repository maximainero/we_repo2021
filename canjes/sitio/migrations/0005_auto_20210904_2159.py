# Generated by Django 3.2.6 on 2021-09-05 00:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sitio', '0004_articles_imagesarticles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=2055)),
                ('state', models.IntegerField(default=0)),
                ('image_one', models.ImageField(unique=True, upload_to='')),
                ('image_two', models.ImageField(blank=True, null=True, unique=True, upload_to='')),
                ('image_three', models.ImageField(blank=True, null=True, unique=True, upload_to='')),
                ('image_four', models.ImageField(blank=True, null=True, unique=True, upload_to='')),
                ('image_five', models.ImageField(blank=True, null=True, unique=True, upload_to='')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Articles',
        ),
        migrations.DeleteModel(
            name='ImagesArticles',
        ),
    ]