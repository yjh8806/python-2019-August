# Generated by Django 2.2.3 on 2019-08-03 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=20)),
                ('userpw', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
            ],
        ),
    ]
