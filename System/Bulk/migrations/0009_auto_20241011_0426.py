# Generated by Django 3.2.7 on 2024-10-11 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bulk', '0008_auto_20241011_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products_images/'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]