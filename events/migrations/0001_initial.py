# Generated by Django 3.2.13 on 2022-07-27 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conference', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('room', models.CharField(max_length=255)),
                ('speaker', models.CharField(max_length=50)),
                ('start_time', models.CharField(max_length=50)),
                ('end_time', models.CharField(max_length=50)),
                ('start_date', models.CharField(max_length=50)),
                ('end_date', models.CharField(max_length=50)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conference.conference')),
            ],
            options={
                'db_table': 'events',
            },
        ),
    ]
