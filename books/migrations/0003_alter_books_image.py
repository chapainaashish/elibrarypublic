# Generated by Django 4.1.3 on 2022-11-15 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_books_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(default='book/default.jpg', upload_to='book/images'),
        ),
    ]
