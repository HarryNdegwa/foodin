from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    person = models.CharField("No. of persons", max_length=10)
    date = models.CharField(max_length=12)
    message = models.CharField(max_length=200)


class Contact(models.Model):
    email = models.EmailField(max_length=254)
    enquiry = models.CharField(max_length=200)


class Comment(models.Model):
    comment = models.CharField(max_length=200)


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="meals/", null=True)

    def __str__(self):
        return self.name

