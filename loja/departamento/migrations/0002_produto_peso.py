# Generated by Django 5.0.7 on 2024-07-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("departamento", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="peso",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
