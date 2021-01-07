from django.db import models


class CategoryCompany(models.Model):
    name = models.CharField('Категория', max_length=150)
    description = models.TextField('Описание', blank=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория компании'
        verbose_name_plural = 'Категории компаний'


class SubCategoryCompany(models.Model):
    name = models.CharField('Подкатегория', max_length=150)
    description = models.TextField('Описание', blank=True)
    url = models.SlugField(max_length=160, unique=True)
    category = models.ForeignKey(CategoryCompany, on_delete=models.CASCADE, related_name='subcategory')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория компании'
        verbose_name_plural = 'Подкатегории компаний'
