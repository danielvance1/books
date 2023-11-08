from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', default='images/none/noimg.jpg')
    rating = models.FloatField()
    description = models.CharField(max_length=2000)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Page(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page_number = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return f"Page {self.page_number} of {self.book.title}"
