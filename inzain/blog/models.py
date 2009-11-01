from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=140)
    blurb = models.TextField()
    body = models.TextField()
    completed = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    markup_type = models.CharField("post format", max_length=10, choices=(
            ("html", "HTML"),
            ("rst", "reStructuredText"),
            ("markdown", "Markdown"),
        ), default="html")
    pub_date = models.DateTimeField("published", default=datetime.datetime.now)
    slug = models.SlugField()
    
    class Meta:
        ordering = ("-pub_date",)
    
    @models.permalink
    def get_absolute_url(self):
        return ('blog-post', (), dict(slug=self.slug))