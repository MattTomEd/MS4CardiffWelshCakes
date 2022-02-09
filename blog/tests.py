from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Post


class PostTests(TestCase):

    def setUp(self):
        """ Create a test post """
        self.post = Post.objects.create(
            title = "Test",
            slug = "test",
            author = User.objects.create_user("username", "email@email.com", "password"),
            content = "Test post",
        )

    def test_blogpost(self):
        """ Test post content returns correctly """
        post = Post.objects.get(id=1)
        expected_object_title = f'{post.title}'
        expected_object_slug = f'{post.slug}'
        expected_object_author = f'{post.author}'
        expected_object_content = f'{post.content}'
        self.assertEquals(expected_object_title, 'Test')
        self.assertEquals(expected_object_slug, 'test')
        self.assertEquals(expected_object_author, 'username')
        self.assertEquals(expected_object_content, 'Test post')

    def test_post_list_view(self):
        """ Ensure the blog list displays properly """
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    