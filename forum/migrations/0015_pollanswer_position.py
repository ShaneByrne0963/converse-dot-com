# Generated by Django 3.2.22 on 2023-12-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0014_auto_20231209_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollanswer',
            name='position',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
