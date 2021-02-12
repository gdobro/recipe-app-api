from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

HTTP_OK = 200


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@goofycompany.com',
            password='topsecret',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='bob.rooney@goofycompany.com',
            password='secret',
            name='Bob Rooney'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        # Page: Changelist
        # URL name: {{ app_label }}_{{ model_name }}_changelist
        # registered with namespace `admin`
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, HTTP_OK)
