from django.db import models

# Create your models here.

MAX_LENGTH = 255
class ProductType(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, unique=True, verbose_name="Тип продукта")

    def __str__(self):
        return f" {self.name}"
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, unique=True, verbose_name="Имя продукта")
    price = models.FloatField( verbose_name="Цена")
    img = models.ImageField(upload_to="image/%Y/%m/%d", verbose_name="Фото")
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, verbose_name="Тип продукта")

    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Supplier(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name="Название поставщика")
    adress = models.CharField(max_length=MAX_LENGTH, verbose_name="Адрес")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

class Stock(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, unique=True, verbose_name="Название склада")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

class Ingredient(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, unique=True, verbose_name="Название ингридиента")
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, verbose_name="Поставщик")
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT, verbose_name="На каком складе хранится")
    img = models.ImageField(upload_to="image/%Y/%m/%d", verbose_name="Фото")
    quantity = models.IntegerField(verbose_name="Кол-во")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Инридиент'
        verbose_name_plural = 'Инридиенты'

class Recipe(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT,verbose_name="Продукт")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT, verbose_name="Ингридиент")

    def __str__(self):
        return f"{self.product} - {self.ingredient}"
    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")
    summ = models.FloatField(verbose_name="Сумма")
    status = models.BooleanField(default=False, verbose_name="Готовность")

    def __str__(self):
        return f"Order {self.id} by {self.client}"
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class ProductInCheck(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.product} in Order {self.order.id}"
    class Meta:
        verbose_name = 'Продукт в заказе'
        verbose_name_plural = 'Продукты в заказе'