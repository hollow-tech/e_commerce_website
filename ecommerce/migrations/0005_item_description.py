# Generated by Django 3.2.4 on 2021-07-02 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='This is a test description'),
            preserve_default=False,
        ),
    ]