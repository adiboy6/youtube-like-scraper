import psycopg2
import datetime

import main


def postgres(response):

    connection = main.psql_connection

    cursor = main.psql_cursor

    for json_object in response['items']:

        date_time_object = datetime.datetime.strptime(json_object['snippet']['publishedAt'],
                                                      '%Y-%m-%dT%H:%M:%S.%fZ')

        title = json_object['snippet']['title']

        try:
            cursor.execute("INSERT INTO Likes VALUES(%s,NOW(),%s)", (title, date_time_object))
            connection.commit()
        # Whenever the title name is found again, the list is updated
        except psycopg2.Error as e:
            print "List is updated"
            return True

    return False
