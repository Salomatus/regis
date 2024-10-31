from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=150, verbose_name="Название")),
                ("content", models.TextField()),
                ("image", models.ImageField(upload_to="images/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("publication_sign", models.BooleanField(default=True)),
                ("count_of_views", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name": "статья",
                "verbose_name_plural": "статьи",
                "ordering": ["title"],
            },
        ),
    ]
