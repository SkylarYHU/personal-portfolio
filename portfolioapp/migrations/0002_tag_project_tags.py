# Generated by Django 5.1.1 on 2024-10-03 09:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolioapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name="project",
            name="tags",
            field=models.ManyToManyField(to="portfolioapp.tag"),
        ),
    ]
