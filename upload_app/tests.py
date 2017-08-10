# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from upload_app.models import AlbumModel, ImageModel


class UploadAlbumTest(TestCase):

    def setUp(self):
        User.objects.create_user(username='test', email='test@123.com', password='asd123456')
        user = User.objects.get(username='test')
        AlbumModel.objects.create(user=user, title='test', description='nothing')

    def test_show_album_success(self):
        self.client.login(username='test', password='asd123456')
        response = self.client.get(reverse('upload:show_album'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['albums'], ['<AlbumModel: test>'])

    def test_add_album_success(self):
        self.client.login(username='test', password='asd123456')
        body = {
            'title': 'post',
            'description': 'This is a post',
        }
        response = self.client.post(reverse('upload:add_album'), body)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/upload/show_album/')

    def test_add_album_fail_by_title(self):
        self.client.login(username='test', password='asd123456')
        body = {
            'title': '',
            'description': 'This is a post',
        }
        response = self.client.post(reverse('upload:add_album'), body)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors, {'title': [u'This field is required.']})

    def test_edit_album_success(self):
        user = User.objects.get(username='test')
        self.client.login(username='test', password='asd123456')
        album = AlbumModel.objects.get(user=user, title='test')
        body = {
            'title': 'change',
            'description': 'This is change post',
        }
        response = self.client.post(reverse('upload:edit_album', args=(album.id, )), body)
        self.assertEqual(response.status_code, 302)
        album = AlbumModel.objects.get(user=user, title='change')
        body_new = {
            'title': album.title,
            'description': album.description,
        }
        self.assertEqual(body_new, body)

    def test_delete_album_success(self):
        user = User.objects.get(username='test')
        self.client.login(username='test', password='asd123456')
        album = AlbumModel.objects.get(user=user, title='test')
        response = self.client.get(reverse('upload:delete_album', args=(album.id, )))
        self.assertEqual(response.status_code, 302)


class UploadImageTest(TestCase):

    def setUp(self):
        User.objects.create_user(username='test', email='test@123.com', password='asd123456')
        user = User.objects.get(username='test')
        AlbumModel.objects.create(user=user, title='test', description='nothing')

    def test_upload_image_success(self):
        user = User.objects.get(username='test')
        self.client.login(username='test', password='asd123456')
        album = AlbumModel.objects.get(user=user, title='test')
        with open('/home/daihu/Downloads/demo.jpg') as img:
            response = self.client.post(reverse('upload:upload_image', args=(album.id, )), {'image': img})
        self.assertEqual(response.status_code, 302)
        self.assertQuerysetEqual(ImageModel.objects.all(), [u'<ImageModel: test>'])
