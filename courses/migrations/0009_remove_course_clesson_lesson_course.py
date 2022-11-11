# Generated by Django 4.1.2 on 2022-10-18 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_alter_course_clesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='clesson',
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]