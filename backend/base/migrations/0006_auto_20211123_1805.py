# Generated by Django 3.2.9 on 2021-11-23 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_product_countinstock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='qty',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='numReviews',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
