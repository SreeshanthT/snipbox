# Generated by Django 5.1.4 on 2024-12-06 09:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("snip", "0002_alter_snippet_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]