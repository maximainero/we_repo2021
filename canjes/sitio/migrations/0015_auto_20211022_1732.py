# Generated by Django 3.2.8 on 2021-10-22 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sitio', '0014_chat_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='participants',
        ),
        migrations.AddField(
            model_name='chat',
            name='participant1',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='participant1', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chat',
            name='participant2',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='participant2', to='auth.user'),
            preserve_default=False,
        ),
    ]