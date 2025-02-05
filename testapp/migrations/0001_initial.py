# Generated by Django 2.2.4 on 2019-12-06 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('School', 'School'), ('Collage', 'Collage'), ('Restaurants', 'Restaurants')], default='School', max_length=50)),
                ('brand', models.CharField(max_length=50, unique=True)),
                ('about', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('pic', models.ImageField(default='default.jpg', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=250)),
            ],
        ),
    ]
