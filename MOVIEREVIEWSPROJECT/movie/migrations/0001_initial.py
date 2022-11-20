# Generated by Django 4.1.3 on 2022-11-19 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('image', models.ImageField(upload_to='movie/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]