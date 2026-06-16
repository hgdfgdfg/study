from django.db import models

class Book(models.Model):
    book_id = models.CharField(db_column='book_id', max_length=20, primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        db_table = 'book'