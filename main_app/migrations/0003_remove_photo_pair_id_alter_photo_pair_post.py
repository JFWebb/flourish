# Generated by Django 4.0.6 on 2022-07-12 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_post_time_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo_pair',
            name='id',
        ),
        migrations.AlterField(
            model_name='photo_pair',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main_app.post'),
        ),
    ]
