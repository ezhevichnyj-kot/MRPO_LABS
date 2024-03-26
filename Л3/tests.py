import unittest

from db_classes import Advertisement, User, Comment, Feedback
from repository import Repository
from logic import *
from main import TestRepo

class TestAdvertisementFunctions(unittest.TestCase):
    def setUp(self):
        
        self.user1 = User(
            email="email@email.com", 
            password="password123", 
            name="Витя"
        )      
        self.user2 = User(
            email="another@mail.com", 
            password="password456", 
            name="Алексей"
        )
        self.adv1 = Advertisement(
            title="First",
            creation_datetime=datetime.now(),
            description="Some description",
            price=12312.321,
            count=2,
        )
        self.adv2 = Advertisement(
            title="Second",
            creation_datetime=datetime.now(),
            description="Another secription",
            price=293.1,
            count=1,
        )

    def test_create_adv(self):
        create_advertisement(self.user1, self.adv1)
        create_advertisement(self.user2, self.adv2)

        # а1 приндлежит п1, но не п2
        self.assertEqual(self.adv1.user, self.user1)
        self.assertNotEqual(self.adv1.user, self.user2)

        # а2 приндлежит п2, но не п1
        self.assertEqual(self.adv2.user, self.user2)
        self.assertNotEqual(self.adv2.user, self.user1)        

        # а1 записана в п1, а2 - нет
        self.assertIn(self.adv1, self.user1.advertisements)
        self.assertNotIn(self.adv2, self.user1.advertisements)

        # а2 записана в п2, а1 - нет
        self.assertIn(self.adv2, self.user2.advertisements)
        self.assertNotIn(self.adv1, self.user2.advertisements)

    def test_change_advertisement(self):

        create_advertisement(self.user1, self.adv1)
        create_advertisement(self.user2, self.adv2)

        change_advertisement(self.user1, self.adv1, self.adv2)
        
        with self.assertRaises(Exception) as context:
            change_advertisement(self.user1, self.adv2, self.adv1)
        self.assertEqual(str(context.exception), 'Пользователь не имеет права на изменения данного объявления!')

        self.assertEqual(self.adv1.user, self.user1)
        self.assertNotEqual(self.adv1.user, self.user2)

    def test_delete_advertisement(self):
        create_advertisement(self.user1, self.adv1)
        delete_advertisement(self.user1, self.adv1)

        self.assertNotIn(self.adv1, self.user1.advertisements)

class TestCommentFunctions(unittest.TestCase):
    def setUp(self):
        self.user1 = User(
            email="email@email.com", 
            password="password123", 
            name="Витя"
        )      
        self.user2 = User(
            email="another@mail.com", 
            password="password456", 
            name="Алексей"
        )
        self.adv1 = Advertisement(
            title="First",
            creation_datetime=datetime.now(),
            description="Some description",
            price=12312.321,
            count=2,
        )
        self.adv2 = Advertisement(
            title="Second",
            creation_datetime=datetime.now(),
            description="Another secription",
            price=293.1,
            count=1,
        )
        self.comment1 = Comment (
            creation_datetime=datetime.now,
            text='some text'
        )
        self.comment2 = Comment (
            creation_datetime=datetime.now,
            text='another text'
        )

    def test_create_comment(self):

        create_advertisement(self.user1, self.adv1)
        self.comment2 = create_comment(self.user2, self.adv1, self.comment2)

        self.assertIn(self.comment2, self.user2.comments)
        self.assertIn(self.comment2, self.adv1.comments)

class TestFeedbackFunctions(unittest.TestCase):
    def setUp(self):
        self.user1 = User(
            email="email@email.com", 
            password="password123", 
            name="Витя"
        )      
        self.user2 = User(
            email="another@mail.com", 
            password="password456", 
            name="Алексей"
        )
        self.adv1 = Advertisement(
            title="First",
            creation_datetime=datetime.now(),
            description="Some description",
            price=12312.321,
            count=2,
        )
        self.adv2 = Advertisement(
            title="Second",
            creation_datetime=datetime.now(),
            description="Another secription",
            price=293.1,
            count=1,
        )
        self.feed1 = Feedback (
            creation_datetime=datetime.now,
            text='some text',
            rate=1
        )
        self.feed2 = Feedback (
            creation_datetime=datetime.now,
            text='another text',
            rate=5
        )

    def test_create_feedback(self):

        create_advertisement(self.user1, self.adv1)
        self.feed2 = create_feedback(self.user2, self.user1, self.feed2)

        self.assertIn(self.feed2, self.user2.created_feedbacks)
        self.assertIn(self.feed2, self.user1.recieved_feedbacks)
   
        with self.assertRaises(Exception) as context:
            create_feedback(self.user1, self.user1, self.feed1)
        self.assertEqual(str(context.exception), 'Пользователь не может оставлять отзывы самому себе!')
        
        self.assertNotIn(self.feed1, self.user1.recieved_feedbacks)
        self.assertNotIn(self.feed1, self.user1.created_feedbacks)