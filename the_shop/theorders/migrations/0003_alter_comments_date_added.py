# Generated by Django 4.2.3 on 2023-08-07 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theorders', '0002_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
