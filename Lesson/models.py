from django.db import models


class LessonMaterial(models.Model):
    """Материалы к уроку"""

    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    material1 = models.CharField(
        max_length=255,
        verbose_name='Материал 1',
        blank=True
    )
    material2 = models.TextField(
        verbose_name='Материал 2',
        blank=True
    )
    material3 = models.ImageField(
        upload_to='lesson_materials/%Y/%m/%d/',
        verbose_name='Материал 3',
        blank=True
    )
    material4 = models.FileField(
        upload_to='lesson_materials/%Y/%m/%d/',
        verbose_name='Материал 4',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    class Meta:
        verbose_name = 'Материал к уроку'
        verbose_name_plural = 'Материалы к уроку'

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """Уроки"""

    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    anons = models.TextField(
        verbose_name='Анонс',
        blank=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    link_to_video = models.CharField(
        max_length=255,
        verbose_name='Ссылка на видео',
        blank=True
    )
    link_to_file = models.CharField(
        max_length=255,
        verbose_name='Ссылка на файл',
        blank=True
    )
    position = models.PositiveIntegerField(
        default=1,
        verbose_name='Позиция'
    )
    materials = models.ManyToManyField(
        LessonMaterial,
        related_name='lessons',
        verbose_name='Материалы к уроку',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    class Meta:
        ordering = ['position']
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.title
