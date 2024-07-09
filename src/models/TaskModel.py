from database.db import get_connection
from .entities.Task import Task


class UserModel():

    @classmethod
    def get_users(self):
        print("hola")
        try:
            connection = get_connection()
            users = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, second_name, cellphone, password FROM general_task.users ORDER BY title ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    user = Task(row[0], str(row[1]), str(row[2]), row[3], str(row[4]))
                    users.append(user.to_JSON())

            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, second_name, cellphone, password FROM general_task.users WHERE id = %s", (id,))
                row = cursor.fetchone()

                user = None
                if row != None:
                    user = Users(row[0], row[1], row[2], row[3])
                    users = user.to_JSON()

            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('select insert_user (%s,%s,%s,%s)', ( user.name, user.second_name, user.cellphone, user.password))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('select update_user (%s,%s,%s,%s,%s)', (user.id ,user.name, user.second_name, user.cellphone, user.password))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM general_task.users WHERE id = %s", (user.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
