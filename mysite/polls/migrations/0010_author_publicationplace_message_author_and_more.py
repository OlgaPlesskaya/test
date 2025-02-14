# Generated by Django 5.1.6 on 2025-02-14 06:13

import django.db.models.deletion
import polls.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0009_categorylvl_delete_categorylevel_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("identifier", models.AutoField(primary_key=True, serialize=False)),
                ("nickname", models.CharField(max_length=100, unique=True)),
                ("url", models.URLField(blank=True, null=True)),
                ("age", models.PositiveIntegerField()),
                (
                    "author_type",
                    models.CharField(
                        choices=[
                            ("Личный профиль", "Личный профиль"),
                            ("Сообщество", "Сообщество"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Мужской", "Мужской"),
                            ("Женский", "Женский"),
                            ("Неизвестен", "Неизвестен"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PublicationPlace",
            fields=[
                ("identifier", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255, unique=True)),
                (
                    "url",
                    models.URLField(
                        max_length=2048, validators=[polls.models.validate_url]
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="message",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="polls.author",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="message",
            name="publication_place",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to="polls.publicationplace",
            ),
            preserve_default=False,
        ),
    ]
