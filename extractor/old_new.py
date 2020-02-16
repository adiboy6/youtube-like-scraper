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

    if postgres_obj.find_title(response['items'][0]['snippet']['title']):
        return

    token = response['nextPageToken']

    get_likes(youtube, token)

    postgres_obj.reverse(response)
