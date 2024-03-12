from datetime import datetime
from typing import List

class User:

    def __init__(self, email, password, name="Без имени",): 
        
        self.email = email
        self.password = password
        self.name = name

        self.comments = []
        self.created_feedbacks = []
        self.recieved_feedbacks = []
        self.transactions = []
        self.advertisements = []

class Category:

    def __init__(self, name):
        self.name = name
        advertisements = []

class Advertisement:

    def __init__(self, user, title, description, price=None,  category=None):

        self.creation_datetime = datetime.now()

        self.title = title
        self.description = description
        self.price = price
        self.comments = []
        self.transactions = [] 

        self.user = None
        self.setUser(user)

        self.category = None
        self.setCategory(category)
        
    def setUser(self, value):
        if value and isinstance(value, User):
            value.advertisements.append(self)
            self.user = value

    def setCategory(self, value):
        if value and isinstance(value, Category):
            value.advertisement = self
            self.category = value

class Comment:

    def __init__(self, text, user, advertisement):

        self.creation_datetime = datetime.now()

        self.text = text

        self.user = None
        self.setUser(user)

        self.advertisement = None
        self.setAdvertisement(advertisement)

    def setUser(self, value):
        if value and isinstance(value, User):
            value.comments.append(self)
            self.user = value
    
    def setAdvertisement(self, value):
        if value and isinstance(value, Advertisement):
            value.comments.append(self)
            self.advertisement = value

class Transaction:

    def __init__(self, user, advertisement, count=1):
        self.creation_datetime = datetime
        self.count = count

        self.user_customer = None
        self.setUser(user)

        self.advertisement = None
        self.setAdvertisement(advertisement)
    
    def setUser(self, value):
        if value and isinstance(value, User):
            value.transactions.append(self)
            self.user_customer = value

    def setAdvertisement(self, value):
        if value and isinstance(value, User):
            value.transactions.append(self)
            self.advertisement = value

class Feedback:

    def __init__(self, creator, reciever, rate, text=None):
        self.rate = rate
        self.text = text

        self.user_creator = None
        self.setCreator(creator)

        self.user_reciever = reciever
        self.setReciever(reciever)

    def setCreator(self, value):
        if value and isinstance(value, User):
            value.created_feedbacks.append(self)
            self.user_creator = value
    
    def setReciever(self, value):
        if value and isinstance(value, User):
            value.recieved_feedbacks.append(self)
            self.user_reciever = value