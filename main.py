# -*- coding: utf-8 -*-

import os
import psycopg2
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import options

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

psql_connection = psycopg2.connect("dbname=youtube user=adiboy")

psql_cursor = psql_connection.cursor()


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

    # To create the list
    options.create(youtube)

    # To update the list
    # options.update(youtube)


if __name__ == "__main__":
    main()
    psql_cursor.close()
    psql_connection.close()