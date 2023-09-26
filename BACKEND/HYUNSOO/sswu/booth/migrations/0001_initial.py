# Generated by Django 4.2.1 on 2023-09-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.CharField(blank=True, max_length=200, null=True)),
                ('kind', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.CharField(blank=True, max_length=20, null=True)),
                ('time', models.CharField(blank=True, max_length=20, null=True)),
                ('locate', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image')),
            ],
        ),
    ]