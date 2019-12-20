import psycopg2
import datetime

import main


def postgres(response):

    connection = main.psql_connection

    cursor = main.psql_cursor

    for json_object in response['items'][::-1]:

        date_time_object = datetime.datetime.strptime(json_object['snippet']['publishedAt'],
                                                      '%Y-%m-%dT%H:%M:%S.%fZ')

        title = json_object['snippet']['title']

        try:
            cursor.execute("INSERT INTO Likes2 VALUES(%s,NOW(),%s)", (title, date_time_object))
            connection.commit()
        except psycopg2.Error as e:
            print "List is updated"
            break
