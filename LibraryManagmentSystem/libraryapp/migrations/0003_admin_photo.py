# Generated by Django 3.2 on 2022-08-25 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0002_remove_admin_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='photo',
            field=models.ImageField(default=True, upload_to='admin_images/'),
        ),
    ]
