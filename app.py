from resources.upload_geo_files import Upload_Geo_Files
from resources.geo_data import Geo_Data, Geo_Data_By_Name, Geo_Data_Delete_By_Name

from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.before_request
def before_request_func():
    sgeol_instance = request.headers.get('sgeol-instance')
    user_token = request.headers.get('user-token')
    print(sgeol_instance, user_token)
    if user_token == None or sgeol_instance == None:
        # TODO: AUTH
        return make_response(
            jsonify({'message': '\'user-token\' or \'sgeol-instance\' is not present.'}), 401)
    
    return make_response(
            jsonify({'message': 'You do not have \'gerente\' role to access API'}), 401)


api.add_resource(Upload_Geo_Files, '/upload-geo-files')
api.add_resource(Geo_Data, '/geo-data')
api.add_resource(Geo_Data_By_Name, '/geo-data/<data_set_name>')
api.add_resource(Geo_Data_Delete_By_Name, '/geo-data/<data_set_name>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1028)
