# Generated by Django 3.0.4 on 2020-03-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='course',
            new_name='courses',
        ),
        migrations.AddField(
            model_name='courses',
            name='detail',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
