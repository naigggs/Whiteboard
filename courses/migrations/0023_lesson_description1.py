# Generated by Django 4.1.2 on 2022-11-07 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0022_course_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='description1',
            field=models.TextField(default=''),
        ),
    ]
