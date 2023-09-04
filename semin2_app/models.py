from django.db import models
from datetime import datetime
from random import randint


class Kicks(models.Model):
    result = models.BooleanField()
    kick_time = models.DateTimeField(default=datetime.now())

    @staticmethod
    def statistics(n: int):
        reshka = 0
        orel = 0
        for _ in range(n):
            kick = Kicks(result=randint(0, 1))
            if kick.result:
                reshka += 1
            else:
                orel += 1
        result_dict = {
            'орёл': orel,
            'решка': reshka,
        }
        return result_dict


# Создайте модель Автор. Модель должна содержать следующие поля:
# ●	имя до 100 символов
# ●	фамилия до 100 символов
# ●	почта
# ●	биография
# ●	день рождения
# Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Article(models.Model):
    head = models.CharField(max_length=200)
    content = models.TextField()
    public_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    public = models.BooleanField()
