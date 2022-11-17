from django.contrib import admin
from TF.models import image_table
# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_title', 'image_class')


admin.site.register(image_table, ImageAdmin)