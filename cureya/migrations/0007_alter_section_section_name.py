# Generated by Django 4.2.3 on 2023-08-07 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cureya', '0006_teammember_is_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='section_name',
            field=models.CharField(default='', max_length=60),
        ),
    ]
