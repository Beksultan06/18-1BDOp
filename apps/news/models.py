from django.db import models
from apps.news.utils import CATEGORY

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    image = models.ImageField(upload_to="news/")
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class CategoryNews(models.Model):
    title = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        blank=True, null=True
    )
    category = models.CharField(
        choices=CATEGORY,
        max_length=155,
        verbose_name='Тип Категорий'
    )

    def __str__(self) -> str:
        return self.category

    class Meta:
        verbose_name_plural = 'Категерий'