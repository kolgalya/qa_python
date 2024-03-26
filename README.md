# qa_python

1. test_add_new_book_add_three_new_books добавляет 3 новые книги в словарь books_genre и проверяет, что его длина равна 3.
2. test_add_new_book_when_len_name_zero_or_forty_two проверяет, что в словарь books_genre не добавляются книги с длиной названия 0 или 42.
3. test_set_book_genre_genre_of_the_new_book_in_self_genre проверяет, что в словарь books_genre добавляются только книги жанр которых есть в списке доступных жанров genre.
4. test_get_books_with_specific_genre_detectives проверяет, что из 3х добавленных книг (2 с жанром «Детективы», 1 – «Мультфильмы») в список books_with_specific_genre добавляются только книги с выбранным жанром (для «Детективы» длина списка = 2).
5. test_get_books_with_specific_genre_when_genre_is_not_on_list проверяет, что из 3х добавленных книг (2 - «Детективы», 1 – «Мультфильмы») в список books_with_specific_genre не добавляются книги с выбранным жанром 'Ужасы' (длина списка = 0).
6. test_get_books_for_children_one_book проверяет, что из 3х добавленных книг (2 - «Детективы», 1 – «Мультфильмы») в список books_for_children добавляется 1 книга с подходящим жанром (длина списка = 1).
7. test_get_books_for_children_empty_list_zero_book проверяет, что в список books_for_children не добавляется книга с жанром 'Ужасы' (длина списка = 0).
8. test_add_book_in_favorites_add_two_favorites_books проверяет, что в список favorites добавились 2 выбранные книги (длина списка = 2).
9. test_add_book_in_favorites_add_two_favorites_books проверяет, что в список favorites добавились 2 выбранные книги (длина списка = 2).
