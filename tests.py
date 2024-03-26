import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_three_new_books(self, three_books):
        assert len(three_books.get_books_genre()) == 3

    @pytest.mark.parametrize('name', ['', 'Название книги больше, чем из сорока двух символов'])
    def test_add_new_book_when_len_name_zero_or_forty_two(self, name):
        book = BooksCollector()
        book.add_new_book(name)
        assert len(book.get_books_genre()) == 0

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Крошка енот', 'Мультфильмы'],
            ['На злобу дня', 'Ужасы'],
            ['Властелин колец', 'Фантастика'],
            ['Джек Потрошитель', 'Ужасы'],
            ['Без жанра', '']
        ]
    )
    def test_set_book_genre_genre_of_the_new_book_in_self_genre(self, name, genre):
        book = BooksCollector()
        book.add_new_book(name)
        book.set_book_genre(name, genre)
        assert book.get_book_genre(name) in book.genre

    def test_get_books_with_specific_genre_detectives(self, three_books):
        assert len(three_books.get_books_with_specific_genre('Детективы')) == 2

    def test_get_books_with_specific_genre_when_genre_is_not_on_list(self, three_books):
        assert len(three_books.get_books_with_specific_genre('Ужасы')) == 0

    def test_get_books_for_children_one_book(self, three_books):
        assert len(three_books.get_books_for_children()) == 1

    def test_get_books_for_children_empty_list_zero_book(self, book):
        book.add_new_book('Джек Потрошитель')
        book.set_book_genre('Джек Потрошитель', 'Ужасы')
        assert book.get_books_for_children() == []

    def test_add_book_in_favorites_add_two_favorites_books(self, favorit):
        assert len(favorit.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites_one_book_remains(self, favorit):
        favorit.delete_book_from_favorites('Война и мир')
        assert len(favorit.get_list_of_favorites_books()) == 1









