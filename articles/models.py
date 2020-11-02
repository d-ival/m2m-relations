from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    scopes = models.ManyToManyField('Scope', through='ArticleInScope', verbose_name='Тематические разделы')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'{self.title} ({self.published_at})'


class Scope(models.Model):

    name = models.CharField(max_length=100, verbose_name='Тематика')
    articles = models.ManyToManyField('Article', through='ArticleInScope', verbose_name='Статьи по тематике')

    class Meta:
        verbose_name = 'Тематический раздел'
        verbose_name_plural = 'Тематические разделы'

    def __str__(self):
        return self.name


class ArticleInScope(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
    topic = models.ForeignKey(Scope, on_delete=models.CASCADE, verbose_name='Раздел')
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статьи'
        ordering = ('is_main',)