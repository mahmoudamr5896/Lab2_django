# Generated by Django 5.0.2 on 2024-02-17 19:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Day1", "0005_student"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
