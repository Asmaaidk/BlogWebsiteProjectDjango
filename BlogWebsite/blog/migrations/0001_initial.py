# Generated by Django 5.0 on 2023-12-07 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Content', models.TextField()),
                ('Category', models.CharField(max_length=100)),
                ('Date_Published', models.DateField()),
            ],
        ),
    ]