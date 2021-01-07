from django.contrib import admin
from .models import CategoryCompany, SubCategoryCompany


class CategoryCompanyAdmin(admin.ModelAdmin):
    pass


class SubCategoryCompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(CategoryCompany, CategoryCompanyAdmin)
admin.site.register(SubCategoryCompany, SubCategoryCompanyAdmin)