from django.contrib import admin
from .models import Genre, Filmwork, GanreFilmwork, PersonFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


class GenreFilmworkInline(admin.TabularInline):
    model = GanreFilmwork


class PersonFilmWorkInline(admin.TabularInline):
    model = PersonFilmwork


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'description', 'creation_date', 'rating')
    search_fields = ('title', 'type')
    list_filter = ('creation_date', 'rating')
    inlines = (GenreFilmworkInline, PersonFilmWorkInline)