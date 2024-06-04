# Generated by Django 3.2.12 on 2024-06-04 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]