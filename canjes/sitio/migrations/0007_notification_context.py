# Generated by Django 3.2.8 on 2021-10-12 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0006_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='context',
            field=models.CharField(default='Tienes un canje pendiente', max_length=255),
            preserve_default=False,
        ),
    ]
