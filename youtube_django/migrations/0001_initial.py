# Generated by Django 2.1.1 on 2018-09-21 04:42

from django.db import migrations, models
import oauth2client.contrib.django_util.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleAPIOauthInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credentials', oauth2client.contrib.django_util.models.CredentialsField(null=True)),
            ],
        ),
    ]
