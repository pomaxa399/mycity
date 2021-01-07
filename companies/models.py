from django.db import models
from categories.models import CategoryCompany, SubCategoryCompany


class Company(models.Model):
    name = models.CharField('Название', max_length=160)
    description = models.TextField('Описание', blank=True)
    logo = models.ImageField(verbose_name='Логотип', blank=True)
    advantage = models.CharField('Преимущества', max_length=250)
    url = models.SlugField(max_length=170, unique=True)
    frame_in = models.CharField('Фрейм внутри', max_length=250, blank=True)
    frame_out = models.CharField('Фрейм снаружи', max_length=250, blank=True)
    category = models.ManyToManyField(CategoryCompany, related_name='category_company')
    subcategory = models.ManyToManyField(SubCategoryCompany, related_name='subcategory_company')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Filial(models.Model):
    frame_in = models.CharField('Фрейм внутри', max_length=250, blank=True)
    frame_out = models.CharField('Фрейм снаружи', max_length=250, blank=True)
    company = models.ForeignKey(Company, verbose_name='Компания',
                                on_delete=models.CASCADE, related_name='filial_company')

    def __str__(self):
        return self.company.name

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'


class Foto(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='company_foto/')
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name='foto_company', null=True, blank=True)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE,
                               related_name='foto_filial', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
