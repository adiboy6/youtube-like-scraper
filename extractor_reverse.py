import db_populator_reverse


def get_likes(youtube):
    token = None
    while True:
        request = youtube.videos().list(
            part="snippet",
            maxResults="50",
            pageToken=token,
            myRating="like"
        )

        response = request.execute()

        if 'nextPageToken' not in response:
            db_populator_reverse.postgres(response)
            return

        token = response['nextPageToken']

        if db_populator_reverse.postgres(response):
            return

