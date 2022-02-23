# Generated by Django 4.0.2 on 2022-02-23 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=300)),
                ('price', models.FloatField()),
                ('stock', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='media/product/image')),
                ('catagory', models.TextField(blank=True, max_length=20, null=True)),
                ('delivery', models.SmallIntegerField(default=3)),
            ],
        ),
    ]
