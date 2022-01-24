from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

tickets =[]

class BUS(Resource):
    def get(self, name):
        for bus in tickets:
            if bus['name'] == name:
                return bus
            return {'bus': None},404

    def post (self,name):
        data = request.get_json()
        bus = {'name': name, 'age': data['age'],'gender':data['gender'],'no of ticket':data['no of ticket'],'seater or sleeper':data['seater or sleeper'],'mode of transport':data['mode of transport'],'phone no':data['phone no']}

        tickets.append(bus)
        return bus
    
    def delete(self, name):
        global tickets
        tickets = list(filter(lambda x: x['name'] != name, tickets))
        return {'message': 'bus ticket  deleted'}
    def put (self,name):
        data = request.get_json()
        bus = {'name': name, 'age': data['age'],'gender':data['gender'],'no of ticket':data['no of ticket'],'seater or sleeper':data['seater or sleeper'],'mode of transport':data['mode of transport'],'phone no':data['phone no']}

        tickets.append(bus)
        return bus


class Train(Resource):
    def get(self, name):
        for train in tickets:
            if train['name'] == name:
                return train
            return {'train': None},404

    def post (self,name):
        data = request.get_json()
        train = {'name': name, 'age': data['age'],'gender':data['gender'],'no of ticket':data['no of ticket'],'general or sleaper or ac':data['general or sleaper or ac'],'mode of transport':data['mode of transport'],'phone no':data['phone no']}

        tickets.append(train)
        return train
    
    def delete(self, name):
        global tickets
        tickets = list(filter(lambda x: x['name'] != name, tickets))
        return {'message': 'train ticket  deleted'}
    def put (self,name):
        data = request.get_json()
        train = {'name': name, 'age': data['age'],'gender':data['gender'],'no of ticket':data['no of ticket'],'general or sleaper or ac':data['general or sleaper or ac'],'mode of transport':data['mode of transport'],'phone no':data['phone no']}

        tickets.append(train)
        return train


class Flight(Resource):
    def get(self, name):
        for flight in tickets:
            if flight['name'] == name:
                return flight
            return {'flight': None},404

    def post (self,name):
        data = request.get_json()
        flight = {'name': name, 'age': data['age'],'gender':data['gender'],'no of ticket':data['no of ticket'],'economic or business or first':data['economic or business or first],'mode of transport':data['mode of transport'],'phone no':data['phone no']}

        tickets.append(flight)
        return flight
    
    def delete(self, name):
        global tickets
        tickets = list(filter(lambda x: x['name'] != name, tickets))
        return {'message': 'flight ticket  deleted'}
    def put (self,name):
        data = request.get_json()
        flight = {'name': name, 'age': data['age'],'gender':data['gender'],'no of ticket':data['no of ticket'],'economic or business or first':data['economic or business or first '],'mode of transport':data['mode of transport'],'phone no':data['phone no']}

        tickets.append(flight)
        return flight

class List(Resource):
     def get(self):
        return {'tickets': tickets}

api.add_resource(BUS, '/bus/<string:name>')
api.add_resource(Train, '/train/<string:name>')
api.add_resource(Flight, '/flight/<string:name>')
api.add_resource(List, '/tickets')

if __name__ == '__main__':
    app.run(debug=True)
