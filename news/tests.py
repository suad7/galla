from django.test import TestCase
from .models import Editor,Article,Tags
import datetime as dt
# Create your tests here.

class EditorTestClass(TestCase):

# Set up method
    def setUp(self):
        self.jido= Editor(first_name = 'jido', last_name ='shire', email ='suadshire98@gamil.com')
        self.jido.save_editor()

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.jido,Editor))

# Testing Save Method
    def test_save_method(self):
        self.jido.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

# Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.jido)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)

    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news

        