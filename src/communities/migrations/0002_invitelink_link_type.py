# Generated by Django 5.0.3 on 2024-04-03 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitelink',
            name='link_type',
            field=models.CharField(default='join', max_length=4),
        ),
    ]