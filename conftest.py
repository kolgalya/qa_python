import pytest

from main import BooksCollector

@pytest.fixture
def book():
    book = BooksCollector()
    return book

@pytest.fixture
def three_books():
    collector = BooksCollector()
    collector.add_new_book('Чудесный костюм')
    collector.set_book_genre('Чудесный костюм', 'Детективы')
    collector.add_new_book('Король лев')
    collector.set_book_genre('Король лев', 'Мультфильмы')
    collector.add_new_book('Война и мир')
    collector.set_book_genre('Война и мир', 'Детективы')
    return collector

@pytest.fixture
def favorit():
    favorit = BooksCollector()
    favorit.add_new_book('Чудесный костюм')
    favorit.set_book_genre('Чудесный костюм', 'Детективы')
    favorit.add_new_book('Король лев')
    favorit.set_book_genre('Король лев', 'Мультфильмы')
    favorit.add_new_book('Война и мир')
    favorit.set_book_genre('Война и мир', 'Детективы')
    favorit.add_book_in_favorites('Король лев')
    favorit.add_book_in_favorites('Война и мир')
    return favorit