# Generated by Django 4.1.6 on 2023-02-15 15:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_alter_todo_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="created_at",
            field=models.DateField(default=datetime.date(2023, 2, 15)),
        ),
    ]
