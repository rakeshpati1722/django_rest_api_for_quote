# Generated by Django 2.2.3 on 2019-09-14 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='abc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quote', models.CharField(max_length=256)),
                ('Author', models.CharField(max_length=256)),
                ('Rating', models.CharField(blank=True, max_length=256)),
            ],
        ),
    ]