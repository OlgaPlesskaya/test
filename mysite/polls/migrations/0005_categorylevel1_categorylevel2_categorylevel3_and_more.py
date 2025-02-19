# Generated by Django 5.1.6 on 2025-02-11 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0004_alter_supplier_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="CategoryLevel1",
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
                ("name", models.CharField(default="Здравоохранение", max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="CategoryLevel2",
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
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("Здоровье человека", "Здоровье человека"),
                            (
                                "Предоставление медицинской помощи",
                                "Предоставление медицинской помощи",
                            ),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CategoryLevel3",
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
        migrations.CreateModel(
            name="CategoryLevel4",
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
                (
                    "name",
                    models.CharField(
                        choices=[
                            (
                                "доступная среда в медучреждениях",
                                "доступная среда в медучреждениях",
                            ),
                            ("доступная среда в целом", "доступная среда в целом"),
                            ("причины", "причины"),
                            ("численность", "численность"),
                            ("рецепты", "рецепты"),
                            (
                                "наличие / нехватка / отсутствие",
                                "наличие / нехватка / отсутствие",
                            ),
                            ("услуги по реабилитации", "услуги по реабилитации"),
                            (
                                "технические средства реабилитации",
                                "технические средства реабилитации",
                            ),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SourceType",
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
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("Блоги", "Блоги"),
                            ("Видео", "Видео"),
                            ("Мессенджеры каналы", "Мессенджеры каналы"),
                            ("Мессенджеры чаты", "Мессенджеры чаты"),
                            ("Микроблоги", "Микроблоги"),
                            ("Онлайн-СМИ", "Онлайн-СМИ"),
                            ("Соцсети", "Соцсети"),
                            ("Форумы", "Форумы"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                ("identifier", models.AutoField(primary_key=True, serialize=False)),
                ("text", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "categories",
                    models.ManyToManyField(
                        related_name="messages", to="polls.categorylevel4"
                    ),
                ),
                (
                    "source_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="polls.sourcetype",
                    ),
                ),
            ],
        ),
    ]
