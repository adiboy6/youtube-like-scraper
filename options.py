from extractor import old_new, new_old


def create(youtube):
    new_old.get_likes(youtube)
    print "likes are created!"


def update(youtube):
    old_new.get_likes(youtube)
