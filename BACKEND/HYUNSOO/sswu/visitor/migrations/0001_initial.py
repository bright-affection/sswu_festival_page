# Generated by Django 4.2.5 on 2023-09-07 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=1000, null=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]