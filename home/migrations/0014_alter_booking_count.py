# Generated by Django 4.1.1 on 2022-11-28 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_booking_id_alter_destination_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='count',
            field=models.IntegerField(default=0, max_length=5),
        ),
    ]