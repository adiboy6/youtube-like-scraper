import db_populator_reverse
import find_table


def get_likes(youtube, token=None):

    request = youtube.videos().list(
        part="snippet",
        maxResults="50",
        pageToken=token,
        myRating="like"
    )

    response = request.execute()

    if find_table.title_column(response['items'][0]['snippet']['title']):
        return

    token = response['nextPageToken']

    get_likes(youtube, token)

    db_populator_reverse.postgres(response)
