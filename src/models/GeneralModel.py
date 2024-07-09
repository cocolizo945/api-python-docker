from database.db import get_connection
from flask import jsonify
import numpy as np
import json
import jsonpickle   

class StandarModel():
    @classmethod
    def standar_crud(self, store_procedure, params):
        connection = get_connection()
        try:
            
            with connection.cursor() as cursor:
                cursor.callproc(store_procedure,params)
                connection.commit()

                row = cursor.fetchone()

                if row != None:
                    responsedb = row[0]
                
            connection.close()

            return responsedb
        
        except Exception as ex:
            raise Exception(ex)
            connection.rollback()
            connection.close()
        finally:
            if connection is not None:
                connection.close()

    @classmethod
    def standar_query(self, store_procedure, params):
        connection = get_connection()
        try:
            
            with connection.cursor() as cursor:
                cursor.callproc(store_procedure,params)
                connection.commit()

                row = cursor.fetchone()

                if row != None:
                    responsedb = row[0]
                
            connection.close()

            return responsedb
        
        except Exception as ex:
            connection.rollback()
            connection.close()
            
        finally:
            if connection is not None:
                connection.close()

