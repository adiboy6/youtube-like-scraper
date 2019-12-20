# -*- coding: utf-8 -*-

import os
import datetime

import psycopg2

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = os.environ.get('GOOGLE_CLIENT_SECRET')

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    token = None

    conn = psycopg2.connect("dbname=youtube user=adiboy")

    cur = conn.cursor()

    while True:
        request = youtube.videos().list(
            part="snippet",
            maxResults="50",
            pageToken=token,
            myRating="like"
        )

        response = request.execute()

        flag = False

        for json_object in response['items']:

            date_time_object = datetime.datetime.strptime(json_object['snippet']['publishedAt'],
                                                          '%Y-%m-%dT%H:%M:%S.%fZ')

            title = json_object['snippet']['title']

            try:
                cur.execute("INSERT INTO Likes1 VALUES(%s,NOW(),%s)", (title, date_time_object))
                conn.commit()
            except psycopg2.Error as e:
                print "List is updated"
                flag = True
                break

        if ('nextPageToken' not in response) or flag:
            break

        token = response['nextPageToken']

    conn.close()
    cur.close()


if __name__ == "__main__":
    main()