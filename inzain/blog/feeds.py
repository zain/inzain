from django.contrib.syndication.feeds import Feed
from inzain.blog.models import Post

class LatestPosts(Feed):
    title = "Zain Memon's Blog"
    link = "/blog/"
    description = "A conundrum wrapped in an enigma."

    def items(self):
        return Post.objects.all()[:10]
