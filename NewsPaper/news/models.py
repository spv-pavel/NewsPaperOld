from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

TYPE_POST = [
    ('article', 'статья'),
    ('news', 'новость'),
]


class Author(models.Model):
    # cвязь «один к одному» с встроенной моделью пользователей User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)  # рейтинг пользователя

    def update_rating(self):
        # суммарный рейтинг каждой статьи автора умножается на 3
        # суммарный рейтинг всех комментариев автора;
        # суммарный рейтинг всех комментариев к статьям автора
        """ author_pst_rating = self.post_set.all().aggregate(post_rating=Sum('post_rating'))['post_rating'] * 3
        author_pst_rating2 = Post.objects.filter(user_author=self).aggregate(Sum('rating_news')).get('rating_news__sum') * 3
        author_pst_rating3 = Post.objects.filter
        author_rating_of_comm = ...
        author_rating_to_comm = ...
        self.author_rate = author_pst_rating + author_rating_of_comm + author_rating_to_comm
        self.save()
        return self.author_rate
 """

class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)


class Post(models.Model):
    # связь один ко многим с Author
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=TYPE_POST)
    data_create = models.DateField(auto_now_add=True)
    # связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    text = models.TextField()
    post_rating = models.IntegerField(default=0)  # рейтинг статьи/новости

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1

    def preview(self):
        # который возвращает начало статьи (предварительный просмотр) длиной 124 символа и добавляет многоточие в конце.
        preview_text = self.text[:124] + '...'
        return preview_text


class PostCategory(models.Model):
    # связь «один ко многим» с моделью Post
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    # связь «один ко многим» с моделью Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    # связь «один ко многим» с моделью Post
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # связь «один ко многим» со встр моделью User (комментарии может оставить любой пользователь, необязательно автор)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date_create = models.DateField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)  # рейтинг комментария

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1
