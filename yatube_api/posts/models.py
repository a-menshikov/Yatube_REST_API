from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    """Класс для постов."""
    text = models.TextField(verbose_name='Текст поста',
                            help_text='Семь раз отмерь, один раз напиши')
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
        'Изображение',
        upload_to='posts/',
        null=True,
        blank=True
    )

    class Meta:
        default_related_name = 'posts'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text


class Comment(models.Model):
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
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        default_related_name = 'comments'

        def __str__(self):
            return self.text


class Group(models.Model):
    """Класс для сообществ"""

    title = models.CharField(max_length=200,
                             verbose_name='Название сообщества',
                             help_text='200 символов максимум')
    slug = models.SlugField(max_length=200,
                            unique=True,
                            verbose_name='Псевдоним сообщества',
                            help_text='200 символов максимум')
    description = models.TextField(verbose_name='Описание сообщества',
                                   help_text='Тематика постов')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self) -> str:
        """Возвращает строку с названием сообщества"""
        return f'{self.title}'


class Follow(models.Model):
    """Подписка на авторов"""

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
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='follow_unique',)
        ]

    def __str__(self) -> str:
        """Возвращает сообщение о подписке"""
        return f'{self.user} подписан на автора {self.author}'
