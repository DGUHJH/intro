# Generated by Django 3.2.5 on 2021-07-28 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='제목')),
                ('description', models.CharField(max_length=64, verbose_name='설명')),
                ('banner_image', models.ImageField(blank=True, upload_to='%Y/%m/%d', verbose_name='이미지')),
            ],
        ),
    ]
