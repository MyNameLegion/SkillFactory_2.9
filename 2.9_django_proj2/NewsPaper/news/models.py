from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    authorRating = models.SmallIntegerField(default=0)

    def update_rating(self):

            postRat = self.post_set.aggregate(postRating=Sum('rating'))
            if postRat.get('postRating') is None:
                print("Вы еще не создавали пост")
                pRat = 0
            else:
                pRat = 0
                pRat += postRat.get('postRating')

            commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
            if commentRat.get('commentRating') is None:
                print("Вы еще не оставляли комментарий")
                cRat = 0
            else:
                cRat = 0
                cRat += commentRat.get('commentRating')

            self.authorRating = pRat * 3 + cRat
            self.save()


class Category(models.Model):
    category = models.CharField(max_length=64, unique=True, )

    def __str__(self):
        return f'{self.category}'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    CATEGORIES = [
        ('ar', 'статья'),
        ('nw', 'новость'),
    ]

    categoryType = models.CharField(max_length=2, choices=CATEGORIES, default='ar', blank=False)
    date_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField("Category", through="PostCategory")
    title = models.CharField(max_length=64)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def preview(self):
        return f"{self.text[0:124]} ..."

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.category}'


class PostCategory(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commentText = models.TextField()
    commentTime = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
