# 1. Изучить документацию по sqlite3:  https://docs.python.org/3/library/sqlite3.html
# 2. Подключится к созданной базе данных в IDE. Проверить работоспособность подключения.

import sqlite3
with sqlite3.connect("movies2.db") as con:
    cur = con.cursor()

# 3. Напишите SQL-запрос, который вычисляет средний возраст актеров (используйте таблицу "actors")
# по полу (столбец "sex") и выводит результат в виде двух столбцов: "sex" и "average_age".

    datas = cur.execute(
        """
        SELECT sex, AVG(age) AS average_age
        FROM actors
        GROUP BY sex
        """
    )
    for data in datas:
        print(data)

# 4. Напишите SQL-запрос, который находит режиссера (имя и фамилия) с максимальным бюджетом фильма.

    datas = cur.execute(
        """
        SELECT directors.name, directors.surname, MAX(movies.budjet)
        FROM directors
        INNER JOIN movies
        USING (director_id)
        """
    )
    for data in datas:
        print(data)

# 5. Напишите SQL-запрос, который выводит список режиссеров (имя и фамилия) и количество фильмов, которые они сняли,
# причем только для режиссеров, у которых есть хотя бы один фильм в базе данных.
# Отсортируйте результат по убыванию количества фильмов.

    datas = cur.execute(
        """
        SELECT COUNT(*) AS count_movies, directors.name, directors.surname
        FROM directors
        INNER JOIN movies
        USING (director_id)
        GROUP BY director_id
        HAVING COUNT(*) > 0
        ORDER BY COUNT(*) DESC
        """
    )
    for data in datas:
        print(data)

# 6. Напишите SQL-запрос, который находит актеров (имя и фамилия) и названия фильмов, в которых они снимались,
# но только для фильмов с бюджетом более 50 миллионов долларов.

    datas = cur.execute(
        """
        SELECT actors.name, actors.surname, movies.name_movie
        FROM actors
        INNER JOIN actors_movies
        USING (actor_id)
        INNER JOIN movies
        USING (movie_id)
        WHERE movies.budjet > 50000000
        GROUP BY actor_id
        """
    )
    for data in datas:
        print(data)

# 7. Напишите SQL-запрос, который находит пять самых популярных актеров (те, кто снялся в наибольшем количестве фильмов)
# и выводит их имена и фамилии, а также количество фильмов, в которых они снимались.

    datas = cur.execute(
        """
        SELECT COUNT(*) AS count_movies, actors.name, actors.surname
        FROM actors
        INNER JOIN actors_movies
        USING (actor_id)
        INNER JOIN movies
        USING (movie_id)
        GROUP BY actor_id
        ORDER BY COUNT(*) DESC 
        LIMIT 5
        """
    )
    for data in datas:
        print(data)

# 8. Напишите SQL-запрос, который выводит список режиссеров (имя и фамилия) и количество фильмов, которые они сняли,
# для каждого года выпуска фильмов. Посчитайте отдельно для каждого года.

    datas = cur.execute(
        """
        SELECT COUNT(movie_id) AS count_movies, directors.name, directors.surname, movies.releace
        FROM directors
        INNER JOIN movies
        USING (director_id)
        GROUP BY movies.releace
        """
    )
    for data in datas:
        print(data)
