# Generated by Django 4.2.5 on 2023-09-09 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booth', '0002_alter_booth_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booth',
            name='content',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]