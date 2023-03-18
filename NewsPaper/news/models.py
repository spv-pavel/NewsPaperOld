from django.db import models
from django.contrib.auth.models import User


TYPE_POST = [
    ('s', 'статья'),
    ('n', 'новость'),
]


class Author(models.Model):
    # cвязь «один к одному» с встроенной моделью пользователей User
    connection_user = models.OneToOneField(User, on_delete=models.CASCADE)
    # рейтинг пользователя. Ниже будет дано описание того, как этот рейтинг можно посчитать


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)


class Post(models.Model):
    # связь один ко многим с Author
    connection_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # поле с выбором типа, статья или новость
    type = models.CharField(max_length=255, choices=TYPE_POST)
    data_create = models.DateField(auto_now_add=True)  # автоматически добавляемая дата и время создания
    # связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory)
    connection_category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    text = models.TextField()
    # рейтинг статьи/новости


class PostCategory(models.Model):
    # связь «один ко многим» с моделью Post
    connection_post = models.OneToOneField(Post, on_delete=models.CASCADE)
    # связь «один ко многим» с моделью Category
    connection_category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#
# class Comment(models.Model):
#     # связь «один ко многим» с моделью Post
#     connection_post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     # связь «один ко многим» со встр моделью User (комментарии может оставить любой пользователь, необязательно автор)
#     connection_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.CharField(max_length=255)
#     date_create = models.DateField(auto_now_add=True)
#     # рейтинг комментария
