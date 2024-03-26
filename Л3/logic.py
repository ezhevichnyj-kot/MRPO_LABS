from db_classes import Advertisement, User, Comment, Feedback
from repository import Repository
from datetime import datetime

def create_advertisement(creator: User, adv: Advertisement) -> None:
    adv.user = creator
    creator.advertisements.append(adv)

def change_advertisement(creator: User, old_adv: Advertisement, new_adv: Advertisement) -> None:
    if old_adv.user != creator:
        raise Exception('Пользователь не имеет права на изменения данного объявления!')
    old_adv = new_adv
    
def delete_advertisement(actor: User, adv: Advertisement) -> None:
    if adv.user != actor:
        raise Exception('Пользователь не обладает достаточными правами для удаления данного объявления!')
    
    actor.advertisements.remove(adv)
    adv.user = None

def create_comment(user: User, adv: Advertisement, comment: Comment) -> Comment:
    
    new_comment = Comment(
        creation_datetime=datetime.now(),
        text=comment.text,
        user=user,
        advertisement=adv
    )

    user.comments.append(new_comment)
    adv.comments.append(new_comment)

    return new_comment

def create_feedback(creator: User, reciever: User, feedback: Feedback) -> Feedback:

    if creator == reciever:
        raise Exception('Пользователь не может оставлять отзывы самому себе!')

    new_feedback = Feedback(
        creation_datetime=datetime.now(),
        rate=feedback.rate,
        text=feedback.text,
        user_creator=creator,
        user_reciever=reciever
    )

    creator.created_feedbacks.append(new_feedback)
    reciever.recieved_feedbacks.append(new_feedback)

    return new_feedback