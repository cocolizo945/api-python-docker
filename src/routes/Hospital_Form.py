from flask import Blueprint, jsonify, request
import json
from json import dumps
import uuid


from models.GeneralModel import StandarModel

main = Blueprint('hospitalform_blueprint', __name__) 

@main.route('/register', methods = ['POST'])
def register_folio():
    store_procedure = 'public.\"injuriesForm\"'
    try:
        option = request.json['option']
        data_entry = json.dumps(request.json["data"])  
        params = (option, data_entry)
        print(params)
   
        folioReturns = StandarModel.standar_crud(store_procedure, params)
        emptyData = 0
        emptyArray = []
        try:
            emptyData = len(folioReturns)
            emptyArray = folioReturns
        except:
            emptyData = 0
            emptyArray = []
        if emptyData == 0:
            return jsonify(
                message = "Error",
                category = "fail",
                data = emptyArray,
                status = 400,
            )
        else:
            return jsonify(
                message = "elementos obtenidos",
                category = "succes",
                data = emptyArray,
                status = 200,
            )
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/save-form', methods = ['POST'])
def save_form():
    store_procedure = 'public.\"injuriesFormbyParts\"'
    try:
        option = request.json['option']
        data_entry = json.dumps(request.json["data"])  
        params = (option, data_entry)
        print(params)
   
        folioReturns = StandarModel.standar_crud(store_procedure, params)
        emptyData = 0
        emptyArray = []
        try:
            emptyData = len(folioReturns)
            emptyArray = folioReturns
        except:
            emptyData = 0
            emptyArray = []
        if emptyData == 0:
            return jsonify(
                message = "Error",
                category = "fail",
                data = emptyArray,
                status = 400,
            )
        else:
            return jsonify(
                message = "elementos obtenidos",
                category = "succes",
                data = emptyArray,
                status = 200,
            )
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500