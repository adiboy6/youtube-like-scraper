import db_populator


def get_likes(youtube, token=None):

    request = youtube.videos().list(
        part="snippet",
        maxResults="50",
        pageToken=token,
        myRating="like"
    )

    response = request.execute()

    if 'nextPageToken' not in response:
        db_populator.postgres(response)
        return

    token = response['nextPageToken']

    get_likes(youtube, token)

    db_populator.postgres(response)
