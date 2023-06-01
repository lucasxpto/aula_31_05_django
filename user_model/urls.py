from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.site_header = 'IFRO-X9'
admin.site.site_title = 'Sistema de X9'
admin.site.index_title = 'Minhas denúncias'
