# Generated by Django 3.2.9 on 2021-11-27 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20211123_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='placeholder.png', null=True, upload_to=''),
        ),
    ]