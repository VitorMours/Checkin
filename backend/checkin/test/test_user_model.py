from django.test import TestCase
from django.contrib.auth import get_user_model

# Use the Django-recommended way to get the User model
User = get_user_model()


class TestUserModel(TestCase):
    def setUp(self):
        self.mocked_user = {
            "first_name": "Julio",
            "last_name": "Thiago",
            "email": "asdasdsad@gmail.com",
            "password": "123213asdsad"
        }
        
    def test_create_user(self) -> None:
        user = User.objects.create(
            first_name="Lucas",
            last_name="pietro",
            email="asdasdsad@gmail.com",
            password="123213asdsad"
        )

        self.assertIsInstance(user, User)
        self.assertEqual(user.first_name, "Lucas")
        self.assertEqual(user.last_name, "pietro")
        self.assertEqual(user.email, "asdasdsad@gmail.com")
        
    def test_update_created_user(self) -> None:
        user = User.objects.create(
            first_name="Lucas",
            last_name="pietro",
            email="asdasdsad@gmail.com",
            password="123213asdsad"
        )
        
        self.assertIsInstance(user, User)
        user.first_name = "Julio"
        self.assertEqual(user.first_name, "Julio")
        user.last_name = "Thiago"
        self.assertEqual(user.last_name, "Thiago")
        user.save()
        
        getted_user = User.objects.get(id=user.id) 
        self.assertIsInstance(getted_user, User)
        self.assertEqual(getted_user.first_name, getted_user.first_name)
        self.assertEqual(getted_user.last_name, getted_user.last_name)
        self.assertEqual(getted_user.email, getted_user.email)


        

