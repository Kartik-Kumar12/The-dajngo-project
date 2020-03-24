# Generated by Django 3.0.2 on 2020-01-10 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='pictures')),
                ('price', models.IntegerField()),
                ('offer', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]