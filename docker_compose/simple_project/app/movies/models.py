import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = _('genre')
        verbose_name_plural = 'Жанры'


class TypeStatusChoces(models.TextChoices):
    movies = "MOVIES"
    tv_show = "TV Show"


class Filmwork(models.Model):
    title = models.TextField(_('title'), null=False, blank=False)
    description = models.TextField(_('description'), null=True, blank=True)
    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)
    rating = models.FloatField(_('rating'), blank=True,
                               validators=[MinValueValidator(0),
                                           MaxValueValidator(100)])
    type = models.CharField(_('Type'), choices=TypeStatusChoces.choices)
    ganre = models.ManyToManyField(Genre, through='GanreFilmwork')
    person = models.ManyToManyField('Person', through='PersonFilmwork')

    def __str__(self):
        return self.title

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = _('film')
        verbose_name_plural = _('films')


class GanreFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"
        unique_together = ('film_work_id', 'genre_id')


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(_('full name'), blank=True)

    class Meta:
        db_table = "content\".\"person"


class PersonFilmwork(UUIDMixin):
    film_work = models.ForeignKey(Filmwork, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Role(models.TextChoices):
        ACTOR = 'actor', _('actor')
        DIRECTOR = 'director', _('director')
        SCREENWRITER = 'screenwriter', _('screenwriter')

    role = models.TextField(_('role'), choices=Role.choices, max_length=64, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"
        unique_together = ('film_work_id', 'person_id', 'role')