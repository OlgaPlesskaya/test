# Generated by Django 5.1.6 on 2025-02-14 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0007_alter_message_categories"),
    ]

    operations = [
        migrations.CreateModel(
            name="CategoryLevel",
            fields=[
                ("identifier", models.AutoField(primary_key=True, serialize=False)),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("инвалидность", "инвалидность"),
                            ("смертность", "смертность"),
                            ("лекарства", "лекарства"),
                            ("реабилитация", "реабилитация"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="CategoryLevel3",
        ),
    ]
