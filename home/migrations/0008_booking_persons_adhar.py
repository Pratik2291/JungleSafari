# Generated by Django 4.1.1 on 2022-11-04 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_booking_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='persons_adhar',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
