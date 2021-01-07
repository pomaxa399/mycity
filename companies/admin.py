from django.contrib import admin
from .models import Company, Filial, Foto


class CompanyAdmin(admin.ModelAdmin):
    pass


class FilialAdmin(admin.ModelAdmin):
    pass


class FotoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
admin.site.register(Filial, FilialAdmin)
admin.site.register(Foto, FotoAdmin)
