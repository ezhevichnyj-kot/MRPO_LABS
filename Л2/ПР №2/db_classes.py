from datetime import datetime

class User:

    def __init__(self, email, password, name="Без имени",): 
        
        self.email: str = email
        self.password: str = password
        self.name: str = name

        self.comments: list[Comment] = []
        self.created_feedbacks: list[Feedback] = []
        self.recieved_feedbacks: list[Feedback] = []
        self.transactions: list[Transaction] = []
        self.advertisements: list[Advertisement] = []

class Category:

    def __init__(self, name):
        self.name: str = name
        advertisements: list[Advertisement] = []

class Advertisement:

    def __init__(self, user, title, description, price=None,  category=None):

        self.creation_datetime: datetime = datetime.now()

        self.title: str = title
        self.description: str = description
        self.price: float = price
        self.comments: list[Comment] = []
        self.transactions: list[Transaction] = [] 

        self.user: User = None
        self.setUser(user)

        self.category: Category = None
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

        self.creation_datetime: datetime = datetime.now()

        self.text: str = text

        self.user: User = None
        self.setUser(user)

        self.advertisement: Advertisement = None
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
        self.creation_datetime: datetime = datetime
        self.count: int = count

        self.user_customer: User = None
        self.setUser(user)

        self.advertisement: Advertisement = None
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
        self.rate: float = rate
        self.text: str = text

        self.user_creator: User = None
        self.setCreator(creator)

        self.user_reciever: User = reciever
        self.setReciever(reciever)

    def setCreator(self, value):
        if value and isinstance(value, User):
            value.created_feedbacks.append(self)
            self.user_creator = value
    
    def setReciever(self, value):
        if value and isinstance(value, User):
            value.recieved_feedbacks.append(self)
            self.user_reciever = value