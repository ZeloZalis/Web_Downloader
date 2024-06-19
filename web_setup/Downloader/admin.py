from django.contrib import admin
from Downloader.models import Data, User, Download

# Register your models here.

class DataDisplay(admin.ModelAdmin):
    list_display=("website", "link", "frmat")
    # De la siguiente forma se puede agregar una barra de búsqueda
    search_fields=("website", "frmat")
    # Sirve para filtrar los registros
    list_filter=("website",)

class UserDisplay(admin.ModelAdmin):
    list_display=("user_ip", "country")
    list_filter=("country",)

class DownloadDisplay(admin.ModelAdmin):
    list_filter=("date",)
    # Agrega un filtro simple arriba de los registros
    date_hierarchy=("date")

admin.site.register(Data, DataDisplay)
admin.site.register(User, UserDisplay)
admin.site.register(Download, DownloadDisplay)