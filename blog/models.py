from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    image = models.ImageField(upload_to="images/", verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    publication_sign = models.BooleanField(
        default=True, verbose_name="Признак публикации"
    )
    count_of_views = models.IntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = ["title"]
