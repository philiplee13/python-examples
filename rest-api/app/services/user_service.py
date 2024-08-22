"""
class for db service
"""

from config import config
import psycopg2
from models import user_model
from models.responses import responses


class UserService:
    def __init__(self):
        cfg = config.Config()
        self.connection: psycopg2.extensions.connection = cfg.conn

    def get_all_users(self) -> responses.CustomResponse:
        query: str = """
            SELECT * FROM users.user;
            """
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        all_users = []
        for user in result:
            user_to_add = user_model.UserModel(
                id=user["user_id"], name=user["name"], age=user["age"]
            )
            all_users.append(user_to_add)
        response = responses.CustomResponse(
            message="Successfully got all users", response_code=200, data=all_users
        )
        cursor.close()
        return response

    def create_user(self, user_to_create: user_model.UserModel):
        query: str = """
            INSERT INTO users.user (name, age) VALUES (%s, %s)
            """
        cursor = self.connection.cursor()
        cursor.execute(query, (user_to_create.name, user_to_create.age))
        self.connection.commit()
        response = responses.CustomResponse(
            message="Successfully inserted user", response_code=200
        )
        cursor.close()
        return response

    def delete_user(self, user_id: int):
        query: str = """
        DELETE FROM users.user WHERE user_id = %s
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (user_id,))
        self.connection.commit()
        response = responses.CustomResponse(message="Deleted user", response_code=200)
        cursor.close()
        return response

    def update_user(self, user_id: int, user_to_update: user_model.UserModel):
        query: str = """
        UPDATE users.user SET name = %s, age = %s
        WHERE user_id = %s    
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (user_to_update.name, user_to_update.age, user_id))
        self.connection.commit()
        response = responses.CustomResponse(message="Updated user", response_code=200)
        cursor.close()
        return response
