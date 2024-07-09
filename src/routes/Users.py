from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Users import Users
# Models
from models.UsersModel import UserModel

main = Blueprint('users_blueprint', __name__)


@main.route('/')
def get_users():
    print("hola")
    try:
        users = UserModel.get_movies()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_user(id):
    print("hola 24:")
    try:
        users = UserModel.get_movie(id)
        if users != None:
            return jsonify(users)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_user():
    try:
        name = request.json['name']
        second_name = request.json['second_name']
        cellphone = int(request.json['cellphone'])
        password = request.json['password']
        id = uuid.uuid4()
        user = Users(str(id), name, second_name, cellphone, password)

        affected_rows = UsersModel.add_movie(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_movie(id):
    try:
        name = request.json['name']
        second_name = request.json['second_name']
        cellphone = int(request.json['cellphone'])
        password = request.json['password']
        user = Users(id, name, second_name, cellphone, password)

        affected_rows = UserModel.update_user(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({'message': "No movie updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_movie(id):
    try:
        user = Users(id)

        affected_rows = UserModel.delete_user(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({'message': "No movie deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500