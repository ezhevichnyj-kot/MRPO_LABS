from datetime import datetime
from dataclasses import dataclass, field
from typing import Type, List

@dataclass
class User:

    def __eq__(self, other):
        if (self.email == other.email and self.password == other.password):
            return True
        return False

    email: str
    password: str
    name: str

    comments: List[Type['Comment']] = field(default_factory=list)
    created_feedbacks: List[Type['Feedback']] = field(default_factory=list)
    recieved_feedbacks: List[Type['Feedback']] = field(default_factory=list)
    transactions: List[Type['Transaction']] = field(default_factory=list)
    advertisements: List[Type['Advertisement']] = field(default_factory=list)

@dataclass
class Category:

    name: str

    advertisements: List[Type['Advertisement']] = field(default_factory=list)

@dataclass
class Advertisement:
    
    def __eq__(self, other):
        if self.creation_datetime == other.creation_datetime and self.user == other.user:
            return True
        return False

    creation_datetime: datetime
    title: str
    description: str
    price: float
    count: int

    user: User = None
    category: Category = None
    comments: List[Type['Comment']] = field(default_factory=list)
    transactions: List[Type['Transaction']] = field(default_factory=list)
    
@dataclass(frozen=True)
class Comment:

    creation_datetime: datetime
    text: str

    user: User = None
    advertisement: Advertisement = None

@dataclass(frozen=True)
class Transaction:

    creation_datetime: datetime
    count: int
    details: str

    user_customer: User = None
    advertisement: Advertisement = None

@dataclass(frozen=True)
class Feedback:

    creation_datetime: datetime
    rate: float
    text: str

    user_creator: User = None
    user_reciever: User = None