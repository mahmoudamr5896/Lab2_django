# Generated by Django 5.0.2 on 2024-02-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Day1", "0004_remove_users_confirm_password"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("s_name", models.CharField(max_length=50)),
                ("S_Email", models.EmailField(max_length=20)),
                ("Age", models.IntegerField()),
            ],
        ),
    ]
