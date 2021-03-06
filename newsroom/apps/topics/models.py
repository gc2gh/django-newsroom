from django.db import models


class TopicPath(models.Model):
    """
    A Topic Path is a term we are using to describe free-from strings defined by editors or authors that allow you to categorize content.
    The strings follow a simple convention using forward slashes:

    /people/george_bush
    /places/europe/france/region/paris/neighborhood
    /topics/immigration
    /events/2009/inauguration
    /topics/housing

    """
    topic_path = models.CharField(max_length=256)

    def __unicode__(self):
        return self.topic_path
        

class Topic(models.Model):
    """
    Topics are a top level collection of stories grouped by topic.
    For instance, a topic on the site related to the Housing Crisis could list stories based on the following more general topics:
    "housing," "banking," "mortgages"
    and would live under the site at http://news21.com/economy/housing-crisis/
    the topic_path would be responsible for gathering the topic paths for housing, banking and mortages
    and the topic_slug would be responsible for creating the url economy/housing-crisis from the root of the site.
    The topic Title would be a string, like "The Home Mortage Meltdown"
    There might also be a topic description.
    """
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    collection = models.ManyToManyField(TopicPath) 
        
    def __unicode__(self):
        return self.title
