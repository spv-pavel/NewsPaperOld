from django.db import models


class Author(models.Model):
    # cвязь «один к одному» с встроенной моделью пользователей User
    # рейтинг пользователя. Ниже будет дано описание того, как этот рейтинг можно посчитать
    pass


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)


class Post(models.Model):
    # связь один ко многим с Author
    # поле с выбором типа, статья или новость
    data_create = models.DateField(auto_now_add=True)  # автоматически добавляемая дата и время создания
    # связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory)
    title = models.CharField(max_length=255)
    text = models.TextField()
    # рейтинг статьи/новости


class PostCategory(models.Model):
    # связь «один ко многим» с моделью Post
    # связь «один ко многим» с моделью Category
    pass


class Comment(models.Model):
    # связь «один ко многим» с моделью Post
    # связь «один ко многим» со встроенной моделью User (комментарии может оставить любой пользователь, необязательно автор)
    text = models.CharField(max_length=255)
    date_create = models.DateField(auto_now_add=True)
    # рейтинг комментария
    pass
