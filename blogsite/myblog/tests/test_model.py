from django.test import TestCase
from myblog.models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse

class PostModelTest(TestCase):

    def create_post(self):
        test_author = User.objects.create_user(username='testUser', email='test@email.com', password='testing123')
        return Post.objects.create(
            title='Test blog title',
            body='This is the test blog body',
            author= test_author
        )

    def test_blog_post_creation(self):
        test_post = self.create_post()
        self.assertTrue(isinstance(test_post, Post))
        self.assertEqual(str(test_post),'Test blog title')

    def test_blog_post_absolute_url(self):
        test_post = self.create_post()
        self.assertEqual(test_post.get_absolute_url(), reverse("blog:home"))