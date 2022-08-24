# Generated by Django 4.1 on 2022-08-24 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Projects",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("description", models.TextField(blank=True, max_length=2048)),
                ("type", models.CharField(blank=True, max_length=128)),
            ],
        ),
    ]
