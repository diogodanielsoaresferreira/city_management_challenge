# Generated by Django 2.2.1 on 2019-05-04 21:03

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('author', models.CharField(max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(choices=[('TBV', 'To Be Validated'), ('VAL', 'Validated'), ('SOL', 'Solved')], default='TBV', max_length=3)),
                ('category', models.CharField(choices=[('CON', 'Construction'), ('SPE', 'Special Event'), ('INC', 'Incident'), ('WEC', 'Weather Condition'), ('ROC', 'Road Condition')], max_length=3)),
            ],
            options={
                'ordering': ('-update_date',),
            },
        ),
    ]
