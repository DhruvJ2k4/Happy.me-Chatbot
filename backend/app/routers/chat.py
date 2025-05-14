# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from app import schemas
# from app.auth import oauth2
# from app.db.database import get_db
# from app.db import models
# from app.utils.gemini import (
#     generate_conversation_summary,
#     get_chat_summary,
#     update_chat_history,
#     delete_chat_history,
#     mental_health_chatbot
# )

# router = APIRouter(
#     tags=['Chat'],
#     prefix="/chat",
# )

# @router.post("/", response_model=schemas.ChatResponse)
# def chat_with_bot(
#     message: schemas.ChatMessage,
#     latest_emotions: list[str],
#     db: Session = Depends(get_db),
#     current_user: models.User = Depends(oauth2.get_current_user)
# ):
#     user_name = current_user.username
#     user_input = message.message
#     emotion = message.emotion

#     latest_emotions.append(emotion)
#     if len(latest_emotions) > 2:
#         latest_emotions.pop(0)

#     response = mental_health_chatbot(user_name, user_input, emotion, db)

#     update_chat_history(user_name, user_input, response, emotion, db)

#     if user_input.lower() in {"bye", "exit", "quit", "bubye", "talk to you later", "sayonara", "c u", "see you", "ttyl", "okay bye"}:
#         farewell_message = (
#             "Hope you are doing alright. If there's anything, I'm always here for you. Don't stress yourself. "
#             "Things will get better.\nTake care! Remember, you are not alone."
#             if latest_emotions.count("sad") >= 2 or latest_emotions.count("fear") >= 2 or latest_emotions.count("anger") >= 2
#             else "Take care! Remember, you are not alone."
#         )

#         chat_history = get_chat_summary(user_name, db)
#         generate_conversation_summary(user_name, chat_history, db)
#         delete_chat_history(user_name, db)

#         return {"message": farewell_message, "chat_history": chat_history, "latest_emotions": latest_emotions}

#     return {"message": response, "chat_history": get_chat_summary(user_name, db), "latest_emotions": latest_emotions}

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas
from app.auth import oauth2
from app.db.database import get_db
from app.db import models
from app.utils.gemini import (
    generate_conversation_summary,
    get_chat_summary,
    update_chat_history,
    delete_chat_history,
    mental_health_chatbot
)

router = APIRouter(
    tags=['Chat'],
    prefix="/chat",
)

@router.post("/", response_model=schemas.ChatResponse)
def chat_with_bot(
    message: schemas.ChatMessage,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    user_name = current_user.username
    user_input = message.message
    emotion = message.emotion

    response = mental_health_chatbot(user_name, user_input, emotion, db)

    update_chat_history(user_name, user_input, response, emotion, db)

    if user_input.lower() in {"bye", "exit", "quit", "bubye", "talk to you later", "sayonara", "c u", "see you", "ttyl", "okay bye"}:
        farewell_message = "Take care! Remember, you are not alone."

        chat_history = get_chat_summary(user_name, db)
        generate_conversation_summary(user_name, chat_history, db)
        delete_chat_history(user_name, db)

        return {"message": farewell_message, "chat_history": chat_history}

    return {"message": response, "chat_history": get_chat_summary(user_name, db)}
