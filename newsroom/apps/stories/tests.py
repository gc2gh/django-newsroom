from django.test import TestCase
from django.template.defaultfilters import slugify
from stories.models import Story, StoryIntegrityError

class StoryTests(TestCase):
    
    def setUp(self):
        self.story = self.create_story()
    
    def create_story(self):
        story = Story()
        story.headline = "This Is A Test Story"
        #normally slugify will be handled by the UI 
        story.slug = slugify(story.headline)
        summary = "Like I said in the headline, this is a test story."
        #TODO add an author(s)
        story.save()
        return story
    
    def _verify_page_count(self,count,story=None,msg=""):
        s = story if story else self.story
        self.failUnlessEqual(s.pages.count(),count,msg)
    
    def test_create_story(self):
        #self.failUnlessEqual(self._page_count(1),"New stories should have exactly one page")
        self._verify_page_count(1,msg="New stories should have exactly one page")
        self.failUnlessEqual(self.story.pages[0].pagenum,1,"First page should be 1")
        
    def test_story_always_has_one_or_more_pages(self):
        p1 = self.story.pages[0]
        self.assertRaises(StoryIntegrityError,p1.delete)
        
    def test_story_add_page(self):
        new_page = self.story.add_page()
        self.failUnlessEqual(new_page.pagenum,2,"This should be the second page for the story")
        self._verify_page_count(2,msg="This Story should have 2 pages")
        
    def test_add_remove_pages(self):
        p1 = self.story.page_one
        p2,p3,p4 = [self.story.add_page() for i in range(3)]

        self._verify_page_count(4,msg="This Story should have 4 pages")
        self.failUnlessEqual(p2.pagenum,2,"This should be Page 2")
        self.failUnlessEqual(p3.pagenum,3,"This should be Page 3")
        self.failUnlessEqual(p4.pagenum,4,"This should be Page 4")        
        
        p3.delete()
        
        #The live instances don't know that their page order has been updated
        # so we have to "refresh" them
        p4 = self.story.pages[2]
        self._verify_page_count(3,msg="This Story should have 3 pages")
        self.failUnlessEqual(p2.pagenum,2,"This should be Page 2")
        self.failUnlessEqual(p4.pagenum,3,"Page 4 should have become Page 3 after delete")
        
        p1.delete()
        
        p2 = self.story.pages[0]
        p4 = self.story.pages[1]
        self._verify_page_count(2,msg="This Story should have 2 pages")
        self.failUnlessEqual(p2.pagenum,1,"Page 2 should have become Page 1 after delete")
        self.failUnlessEqual(p4.pagenum,2,"Page 3 should have become Page 2 after delete")
        
        p2.delete()
        
        p4 = self.story.pages[0]
        self._verify_page_count(1,msg="This Story should have 1 page")
        self.failUnlessEqual(p4.pagenum,1,"Page 2 should have become Page 1 after delete")
        self.failUnlessEqual(self.story.page_one,p4,"Original Page 4 should be the Page 1")
        self.assertRaises(StoryIntegrityError,p4.delete)
        
        
        