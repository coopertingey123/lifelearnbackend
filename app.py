from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_heroku import Heroku


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://fwyesgaivsfvnm:797d5fc6ec5c6f52976fdcd04665a761bf41d87bb6318dfefdd3c827aef0229b@ec2-3-91-127-228.compute-1.amazonaws.com:5432/darucigiuoj4i7"

db = SQLAlchemy(app)
ma = Marshmallow(app)

CORS(app)
Heroku(app)

SQLALCHEMY_TRACK_MODIFICATIONS = False

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True, nullable=False)
    sign_up_code = db.Column(db.Integer(), unique = False, nullable=False)
    personal_code = db.Column(db.Integer(), unique = True, nullable=False)


    def __init__(self, email, sign_up_code, personal_code):
        self.email = email
        self.sign_up_code = sign_up_code
        self.personal_code = personal_code

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "email", "sign_up_code", "personal_code")

user_schema = UserSchema()
multiple_users_schema = UserSchema(many=True)

@app.route("/user/add", methods=["POST"])
def create_user():
    if request.content_type != "application/json":
        return "Error: Data must be sent as JSON."

    post_data = request.get_json()
    email = post_data.get("email")
    sign_up_code = post_data.get("sign_up_code")
    personal_code = post_data.get("personal_code")

  

    record = User(email, sign_up_code, personal_code)
    db.session.add(record)
    db.session.commit()
    
    return jsonify("User added successfully")

#Create an api that gathers all the personal links and signup links

if __name__ == "__main__":
    app.run(debug=True)




# userData = {
#   "name": "cooper",
#   "email": "coopetingey@yahoo.com",
#   "personal link": "asdfjklj;falskdjf"
# }

# import random


# def newCode():
#   code = ""
#   for x in range(6):
#     code = code + str(random.randint(0,9))
#   return code

# def survey():
#   userEmail = input("Please enter your email address: ")
#   userFirst = input("First name: ")
#   userLast = input("Last name: ")
#   userCode = newCode()
#   # This is where I would make a function to send this info to the database
#   print(userFirst, userLast, userEmail, userCode)

# survey()