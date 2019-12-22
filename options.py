import extractor_reverse
import extractor


def create(youtube):
    extractor.get_likes(youtube)
    print "likes are created!"


def update(youtube):
    extractor_reverse.get_likes(youtube)
