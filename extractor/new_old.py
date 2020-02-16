from db import postgres


def get_likes(youtube, token=None):
    postgres_obj = postgres.Postgre("Likes")

    request = youtube.videos().list(
        part="snippet",
        maxResults="50",
        pageToken=token,
        myRating="like"
    )

    response = request.execute()

    if 'nextPageToken' not in response:
        postgres_obj.forward(response)
        return

    token = response['nextPageToken']

    get_likes(youtube, token)

    postgres_obj.forward(response)
