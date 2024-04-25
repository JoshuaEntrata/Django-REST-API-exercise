# Generated by Django 5.0 on 2024-04-25 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('NEWS', 'News'), ('OPINION', 'Opinion'), ('TECH', 'Technology'), ('LIFE', 'Life'), ('SPORTS', 'Sports'), ('RANDOM', 'Random')], default='RANDOM', max_length=10),
        ),
    ]
