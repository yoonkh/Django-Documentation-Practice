"""
Post 모델
    author = User와 연결
    comments = MTM으로 Comment와 연결
    title
    content
    created_date
        DateTimeField
    modified_date
        DateTimeField

Comment 모델
    post = Post와 연결
    author = User와 연결
    content
    created_date
    modified_date

User모델
    name
    created_date
    modified_date
"""

from django.db import models
from utils.models.mixins import TimeStampedMixin


class User(TimeStampedMixin):
    name = models.CharField(max_length=30)


class Post(TimeStampedMixin):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = models.TextField()
    # # 이 Post에 좋아요를 누른사람들
    like_users = models.ManyToManyField(
        User,
        related_name='like_posts',
        through='PostLike',
    )
    # # like_users가 through를 이용해서 PostLike를  Intermediate모델로 거쳐가도록 설정
    #


#
class Comment(TimeStampedMixin):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    content = models.TextField()


class PostLike(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     db_table = 'introduction_to_models_post_like_users'

#

# class PostLike(models.Model):
#     post = models.ForeignKey(Post)
#     user = models.ForeignKey(User)
#     # created_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return '{author}의 Post({post_title})에 대한 ' \
#                '{like_user}의 좋아요 ({like_datetime})'.format(
#             author=self.post.author.name,
#             post_title=self.post.title,
#             like_user=self.user.name,
#             like_datetime=self.created_date,
#         )
#
#     class Meta:
#         db_table = 'introduction_to_models_post_like_users'
