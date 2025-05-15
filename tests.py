from main import BooksCollector


class TestBooksCollector:


    def test_add_new_book_add_two_books(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

import pytest

@pytest.mark.parametrize('book_name, genre',
                             [
                                 ['Котобой', 'Мультфильмы'],
                                 ['Приключения Шерлока Холмса', 'Детективы'],
                                 ['Война миров', 'Фантастика']
                             ]
                             )
def test_set_book_genre_parametrized(books_collector, book_name, genre):
    books_collector.add_new_book(book_name)
    books_collector.set_book_genre(book_name, genre)
    assert books_collector.get_book_genre(book_name) == genre

def test_set_book_genre(books_collector):
    books_collector.add_new_book('Война миров')
    books_collector.set_book_genre('Война миров', 'Фантастика')
    assert books_collector.get_book_genre('Война миров') == 'Фантастика'

def test_get_book_genre_returns_dict_value(books_collector):
    book_name = "Метро 2033"
    books_collector.add_new_book(book_name)
    books_collector.books_genre[book_name] = "Фантастика"
    assert books_collector.get_book_genre(book_name) == "Фантастика"

def test_get_books_genre_returns_dict(books_collector):
    books_collector.add_new_book("Мастер и Маргарита")
    books_dict = books_collector.get_books_genre()
    assert books_dict == {"Мастер и Маргарита": ""}


def test_get_books_for_children(books_collector):
    books_collector.add_new_book("Чук и Гек")
    books_collector.set_book_genre("Чук и Гек", "Мультфильмы")
    result = books_collector.get_books_for_children()
    assert result == ["Чук и Гек"]


def test_book_not_for_children(books_collector):
    books_collector.add_new_book("Оно")
    books_collector.set_book_genre("Оно", "Ужасы")
    children_books = books_collector.get_books_for_children()
    assert "Оно" not in children_books


def test_add_book_to_favorites(books_collector):
    books_collector.add_new_book("Гарри Поттер")
    books_collector.add_book_in_favorites("Гарри Поттер")
    assert "Гарри Поттер" in books_collector.get_list_of_favorites_books()

def test_delete_book_from_favorites(books_collector):
    books_collector.add_new_book('Девушка в тумане')
    books_collector.add_book_in_favorites('Девушка в тумане')
    books_collector.delete_book_from_favorites('Девушка в тумане')
    assert 'Девушка в тумане' not in books_collector.get_list_of_favorites_books()

def test_get_book_from_favorites(books_collector):
    books_collector.add_new_book('Чук и Гек')
    books_collector.add_book_in_favorites('Чук и Гек')
    favorites = books_collector.get_list_of_favorites_books()
    assert favorites == ['Чук и Гек']
