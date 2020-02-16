import datetime
import main


class Postgre:

    def __init__(self,db_name):
        self.db_name = db_name

    def forward(self,response):
        connection = main.psql_connection

        cursor = main.psql_cursor

        for json_object in response['items'][::-1]:
            date_time_object = datetime.datetime.strptime(json_object['snippet']['publishedAt'],
                                                          '%Y-%m-%dT%H:%M:%S.%fZ')

            title = json_object['snippet']['title']

            cursor.execute("INSERT INTO Likes1 VALUES(%s,NOW(),%s)", (title, date_time_object))
            connection.commit()

    def reverse(self,response):
        connection = main.psql_connection

        cursor = main.psql_cursor

        for json_object in response['items'][::-1]:

            date_time_object = datetime.datetime.strptime(json_object['snippet']['publishedAt'],
                                                          '%Y-%m-%dT%H:%M:%S.%fZ')

            title_value = json_object['snippet']['title']

            if self.find_title(title_value):
                pass
            else:
                cursor.execute("INSERT INTO Likes1 VALUES(%s,NOW(),%s)", (title_value, date_time_object))
                connection.commit()

    def find_title(self, value):
        cursor = main.psql_cursor

        title = value

        cursor.execute("SELECT title FROM Likes1 WHERE title = %s", (title,))

        return cursor.fetchone() is not None

