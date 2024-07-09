from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Task import Task

from models.TaskModel import Task

main = Blueprint('movie_blueprint', __name__)


@main.route('/')
def get_movies():
    print("hola")
    try:
        movies = Task.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_movie(id):
    print("hola 24:")
    try:
        movie = Task.get_movie(id)
        if movie != None:
            return jsonify(movie)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_movie():
    try:
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']
        id = uuid.uuid4()
        movie = Task(str(id), title, duration, released)

        affected_rows = MovieModel.add_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_movie(id):
    try:
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']
        movie = Movie(id, title, duration, released)

        affected_rows = Task.update_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': "No movie updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_movie(id):
    try:
        movie = Task(id)

        affected_rows = Task.delete_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': "No movie deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500