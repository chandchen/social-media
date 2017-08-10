from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from users.models import Profile


class UsersRegisterTest(TestCase):

    def test_register_success(self):
        body = {
            'username': 'test',
            'email': 'test@123.com',
            'password1': 'asd123456',
            'password2': 'asd123456',
        }
        response = self.client.post(reverse('users:register'), body)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_register_fail_by_email(self):
        body = {
            'username': 'test',
            'email': 'test.com',
            'password1': 'asd123456',
            'password2': 'asd123456',
        }
        response = self.client.post(reverse('users:register'), body)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors, {'email': [u'Enter a valid email address.']})

    def test_register_fail_by_password_numeric(self):
        body = {
            'username': 'test',
            'email': 'test@123com',
            'password1': '123456',
            'password2': '123456',
        }
        response = self.client.post(reverse('users:register'), body)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors,
                         {'password2': [u'This password is too short. It must contain at least 8 characters.',
                                        u'This password is too common.',
                                        u'This password is entirely numeric.'],
                          'email': [u'Enter a valid email address.']})

    def test_register_fail_by_password_not_match(self):
        body = {
            'username': 'test',
            'email': 'test@123.com',
            'password1': 'asd123456',
            'password2': 'asd654321',
        }
        response = self.client.post(reverse('users:register'), body)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors, {'password2': [u"The two password fields didn't match."]})


class UsersLoginTest(TestCase):

    def setUp(self):
        User.objects.create_user(username='test', email='test@123.com', password='asd123456')

    def test_login_success(self):
        body = {
            'username': 'test',
            'password': 'asd123456',
        }
        response = self.client.post(reverse('users:login'), body)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_login_fail_by_username(self):
        body = {
            'username': 'users',
            'password': 'asd123456',
        }
        response = self.client.post(reverse('users:login'), body)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors, {'__all__': [u'Please enter a correct username and password. '
                                                                       u'Note that both fields may be case-sensitive.']})

    def test_login_fail_by_password(self):
        body = {
            'username': 'test',
            'password': 'asd654321',
        }
        response = self.client.post(reverse('users:login'), body)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors, {'__all__': [u'Please enter a correct username and password. '
                                                                       u'Note that both fields may be case-sensitive.']})


class UsersProfileTest(TestCase):

    def setUp(self):
        User.objects.create_user(username='test', email='test@123.com', password='asd123456')
        Profile.objects.update(user_id=1, photo='upload_file/users/demo1.jpg', gender=2, bio='666',
                               location='USA', birthday='2012-02-02', website='http://abc.com')

    def test_edit_profile_success(self):
        user = User.objects.get(username='test')
        self.client.user = user
        self.client.login(username=user.username, password='asd123456')
        profile = Profile.objects.get(user=user)
        profile_old_info = {
            'photo': profile.photo,
            'gender': profile.gender,
            'bio': profile.bio,
            'location': profile.location,
            'birthday': profile.birthday,
            'website': profile.website,
        }
        body = {
            'photo': 'upload_file/users/test.jpg',
            'gender': 1,
            'bio': 'test',
            'location': 'China',
            'birthday': '2010-01-01',
            'website': 'http://123.com',
        }
        response = self.client.post(reverse('users:profile_edit', args=(user.id, )), body)
        profile = Profile.objects.get(user=user)
        self.assertEqual(response.status_code, 302)
        profile_new_info = {
            'photo': profile.photo,
            'gender': profile.gender,
            'bio': profile.bio,
            'location': profile.location,
            'birthday': profile.birthday,
            'website': profile.website,
        }
        self.assertNotEqual(profile_old_info, profile_new_info)

    def test_edit_profile_fail_by_birthday(self):
        user = User.objects.get(username='test')
        self.client.user = user
        self.client.login(username=user.username, password='asd123456')
        body = {
            'birthday': '20100101',
        }
        response = self.client.post(reverse('users:profile_edit', args=(user.id,)), body)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors, {'birthday': [u"Enter a valid date."]})

    def test_edit_profile_fail_by_website(self):
        user = User.objects.get(username='test')
        self.client.user = user
        self.client.login(username=user.username, password='asd123456')
        body = {
            'website': r'abcdefg',
        }
        response = self.client.post(reverse('users:profile_edit', args=(user.id,)), body)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors, {'website': [u"Enter a valid URL."]})
