# Generated by Django 3.2.13 on 2022-07-14 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('stuid', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'attendees',
            },
        ),
    ]