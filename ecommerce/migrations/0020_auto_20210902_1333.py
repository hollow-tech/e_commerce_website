# Generated by Django 3.2.4 on 2021-09-02 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0019_coupon_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='being_delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='refund_granted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='refund_requested',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='reveived',
            field=models.BooleanField(default=False),
        ),
    ]
