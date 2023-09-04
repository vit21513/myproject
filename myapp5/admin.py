from django.contrib import admin

from myapp5.models import Category, Product
from myapp2.models import Post,Author


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    list_display = ['name', ['email']]



class ProductAdmin(admin.ModelAdmin):
    """ список продуктов """
    list_display = ['name', 'category', 'quantity']
    ordering = ["category", '-quantity']
    list_filter = ['date_added', 'price']
    search_fields = ['description']
    search_help_text = 'Помск по полю Описание продукта'
    actions = [reset_quantity]
    # fields = ['name', 'description', 'category', 'date_added', 'rating']
    readonly_fields = ['date_added', 'rating']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating', 'date_added'],
            }
        ),
    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Post)
admin.site.register(Author)