# Generated by Django 5.0.6 on 2024-05-23 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontendfood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdb',
            name='con_message',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
