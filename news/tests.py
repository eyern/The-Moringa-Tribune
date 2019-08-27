from django.test import TestCase
from .models import Editor, Article, tags
import datetime as dt


# Create your tests here.
class EditorTestClass(TestCase):

    def setUp(self):
        self.james = Editor(first_name='James', last_name='Muriuki', email='jams@moringaschool.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.james, Editor))

    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)


class tagsTestClass(TestCase):

    def setUp(self):
        self.technology = tags(name="technology")

    def test_instance(self):
        self.assertTrue(isinstance(self.technology, tags))

    def test_save_method(self):
        self.technology.save_tag()
        the_tags = tags.objects.all()
        self.assertTrue(len(the_tags) > 0)

    def test_delete_method(self):
        self.technology.save_tag()
        self.technology.delete_tag()
        the_tags = tags.objects.all()
        self.assertTrue(len(the_tags) == 0)


class ArticleTestClass(TestCase):

    def setUp(self):
        # creating an editor and saving them
        self.james = Editor(first_name='James', last_name='Muriuki', email='james@moringaschool.com')
        self.james.save_editor()

        # doing the same for a tag
        self.new_tag = tags(name='testing')
        self.new_tag.save()

        # now an article
        self.new_article = Article(title='Test Article', post='This is a random test Post', editor=self.james)
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
