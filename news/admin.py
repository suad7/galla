from django.contrib import admin
from .models import Editor,Article,Tags, Location



# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Editor)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Tags)
admin.site.register(Location)
