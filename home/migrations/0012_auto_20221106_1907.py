# Generated by Django 3.0.14 on 2022-11-06 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20221106_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='persons_adhar',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='persons_age',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='persons_gender',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='persons_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
