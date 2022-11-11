# Generated by Django 4.1.2 on 2022-10-31 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0019_alter_course_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='course_students', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
