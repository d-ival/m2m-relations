from django.conf import settings
from django.core.management.base import BaseCommand
import json
from articles.models import Article
import os

class Command(BaseCommand):
    help = u'Загрузка новостей из json-файла'

    def add_arguments(self, parser):
        parser.add_argument('src_path', type=str, help=u'Путь к файлу с исходными данными')

    def handle(self, *args, **options):
        src_path = options['src_path']
        src_full_path = os.path.join(settings.BASE_DIR, src_path)
        if not os.path.exists(src_full_path):
            print('Не найден файл по указанному адресу:', src_full_path)
            return
        with open(src_full_path, encoding='utf8') as src_file:
            data = json.load(src_file)

        for article_ds in data:
            article = Article(id=article_ds['pk'], **article_ds['fields'])
            print(article)
            article.save()
