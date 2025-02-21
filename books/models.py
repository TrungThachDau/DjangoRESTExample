from django.db import models


class TypeBook(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publisher = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    pub_date = models.DateField()
    type = models.ForeignKey(TypeBook, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.title