from flask import Blueprint, jsonify, request
import uuid

from models.GeneralModel import StandarModel

main = Blueprint('newusers_blueprint', __name__) 

@main.route('/type', methods = ['POST'])
def get_all_users():
    store_procedure = 'users.\"UsersOperations\"'
    try:
        id_type = request.json['id_type']
        option = request.json['option']
        params = (option,id_type)

        dateReturns = StandarModel.standar_crud(store_procedure, params)
        emptyData = 0
        emptyArray = []
        try:
            emptyData = len(dateReturns)
            emptyArray = dateReturns
        except:
            emptyData = 0
            emptyArray = []
        if emptyData == 0:
            return jsonify(
                message = "{} elementos obtenidos".format(emptyData),
                category = "fail",
                data = emptyArray,
                status = 400,
                registros = format(emptyArray)
            )
        else:
            return jsonify(
                message = "{} elementos obtenidos".format(emptyData),
                category = "succes",
                data = emptyArray,
                status = 200,
                registros = format(emptyArray)
            )
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500



