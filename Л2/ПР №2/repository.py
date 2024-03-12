from db_classes import *

class ClassStorage:
    
    def __init__(self, class_to_store):
        self.__instances = []
        self.__classtype = class_to_store

    def get(self):
        return self.__instances

    def add(self, value):
        if isinstance(value, self.__classtype):
            self.__instances.append(value)
        else:
            raise ValueError(f"Для массива {self.__classtype} был передан неверный тип данных: {type(value)}!")
     
    def delete(self, value):
        self.__instances.remove(value)

class Repository:  
    
    def __init__(self):
        self.users = ClassStorage(User)
        self.comments = ClassStorage(Comment)
        self.feedbacks = ClassStorage(Feedback)
        self.advertisements = ClassStorage(Advertisement)
        self.transactions = ClassStorage(Transaction)
        self.categories = ClassStorage(Category)