# Generated by Django 3.1.4 on 2020-12-17 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20201217_2134'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Echo',
            new_name='CourseOutline',
        ),
        migrations.RenameField(
            model_name='courseoutline',
            old_name='courseID',
            new_name='courseId',
        ),
    ]
