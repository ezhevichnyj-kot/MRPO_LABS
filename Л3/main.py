from repository import Repository
from db_classes import User, Advertisement
from datetime import datetime
from logic import *
import random
from copy import deepcopy

class TestRepo(Repository):
    pass

if __name__ == "__main__":
    user_repo = TestRepo(User)
    adv_repo = TestRepo(Advertisement)

    user_repo.create(
        User(
            email="email@email.com", 
            password="password123", 
            name="Витя"
        )
    )

    user_repo.create(
        User(
            email="ant@email.com", 
            password="password123", 
            name="Вова"
        )
    )

    adv1 = Advertisement(
            title="First",
            creation_datetime=datetime.now(),
            description="Some description",
            price=12312.321,
            count=2,
            )
    
    adv2 = deepcopy(adv1)
    adv2.creation_datetime = datetime

    users = user_repo.read()

    create_advertisement(adv_repo, users[0], adv1)
    change_advertisement(adv_repo, users[1], adv2)