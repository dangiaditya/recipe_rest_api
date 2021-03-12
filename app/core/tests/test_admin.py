from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):
    """Test admin site"""

    def setUp(self) -> None:
        """This method is used to create a initial setup"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@admin.com',
            password='password@123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@user.com',
            password='password@123',
            name='test user'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)
        print('test_users_listed')
        print(url)
        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """Test That the esit page works"""

        url = reverse('admin:core_user_change', args=[self.user.id])
        print('test_user_change_page')
        print(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """Test that the user page works"""
        url = reverse('admin:core_user_add')
        print('test_create_user_page')
        print(url)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
