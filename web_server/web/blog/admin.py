from django.contrib import admin

from .models import Post, Category
# Register your models here.


# Here is the stuff help you to display the tables better
class PAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_posted']


admin.site.register(Post, PAdmin)
admin.site.register(Category)
