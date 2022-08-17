from email import message
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource,Api,marshal_with, fields


app = Flask(__name__)
api=Api(app)#api= Api(app) # api class to instantiate the app we have set up


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' 
# we have file path, database type("sqlite" or "postgresql") and the name of the database("todo.db")
db = SQLAlchemy(app)


class Details(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    phone=db.Column(db.Integer, nullable=False)
    message=db.Column(db.String, nullable=True)
  

    def __repr__(self):
        return self.phone # every time we call this class we make sure phone number is the one that represents the class

infoFields= {
    'id': fields.Integer,   
    'phone':fields.Integer,
    'message':fields.String,   
 
}

class Info(Resource):
    
    @marshal_with(infoFields)    
    def get(self):
        infos=Details.query.all() 
        return infos


    @marshal_with(infoFields) 
    def post(self):
        data=request.json  
        print(data)         
        info=Details(phone=data['phone'], message=data['message'])           
        db.session.add(info)        
        db.session.commit()
       

        infos=Details.query.all()

        
       
        return infos


api.add_resource(Info, '/')
# api.add_resource(Infos, '/<int:pk>')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)