# Generated by Django 2.2.3 on 2019-08-04 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=20)),
                ('time', models.TimeField(auto_now=True)),
                ('text', models.TextField(max_length=1000)),
            ],
        ),
    ]
