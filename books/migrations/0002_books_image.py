# Generated by Django 4.1.3 on 2022-11-15 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='book/images'),
        ),
    ]
