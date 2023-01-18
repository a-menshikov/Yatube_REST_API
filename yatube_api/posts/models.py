from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    """Класс для постов."""
    text = models.TextField(verbose_name='Текст поста')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        'Group',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Сообщество'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='posts/',
        null=True,
        blank=True
    )

    class Meta:
        default_related_name = 'posts'

    def __str__(self):
        """Возвращает текст поста."""
        return self.text


class Comment(models.Model):
    """Модель комментариев."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор комментария'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост'
    )
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(verbose_name='Дата добавления',
                                   auto_now_add=True,
                                   db_index=True)

    class Meta:
        default_related_name = 'comments'

        def __str__(self):
            """Возвращает текст комментария."""
            return self.text


class Group(models.Model):
    """Модель для сообществ"""

    title = models.CharField(max_length=200,
                             verbose_name='Название сообщества')
    slug = models.SlugField(max_length=200,
                            unique=True,
                            verbose_name='Псевдоним сообщества')
    description = models.TextField(verbose_name='Описание сообщества')

    def __str__(self) -> str:
        """Возвращает название сообщества."""
        return f'{self.title}'


class Follow(models.Model):
    """Модель подписки."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Фолловер'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='follow_unique',)
        ]

    def __str__(self) -> str:
        """Возвращает сообщение о подписке"""
        return f'{self.user} подписан на автора {self.author}'
