import main


def title_column(title_param):

    cursor = main.psql_cursor

    title = title_param

    cursor.execute("SELECT title FROM Likes WHERE title = %s", (title,))

    return cursor.fetchone() is not None
