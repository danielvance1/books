# Generated by Django 4.2.7 on 2023-11-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_bookdata_book_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='images/none/noimg.jpg', upload_to='images'),
        ),
    ]
