from django.db import models


class Movie(models.Model):
    name = models.CharField('영화 이름', max_length=100)
    ticket_count = models.PositiveIntegerField('예매 수')
    score = models.DecimalField('평점', max_digits=4, decimal_places=2, null=True, default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'movie'