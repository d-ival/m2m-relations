from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, ArticleInScope

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_scopes_count = 0
        total_scopes = 0
        for form in self.forms:
            if len(form.cleaned_data) == 0:
                continue # строка не связана с разделом
            total_scopes += 1
            main_scopes_count += form.cleaned_data['is_main']

        if main_scopes_count == 0 and total_scopes > 0:
            raise ValidationError('Укажите основной раздел')

        elif main_scopes_count > 1:
            raise ValidationError('Основным может быть только один раздел')

        return super().clean()  # вызываем базовый код переопределяемого метода

class ArticleInScopeInline(admin.TabularInline):
    model = ArticleInScope
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleInScopeInline]

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
