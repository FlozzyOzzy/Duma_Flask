# importing flask
from flask import *

# Initializing the flask app
app = Flask(__name__)

# defining a simple route/endpoint
# designtated endpoint for our web application function
@app.route("/api/home")
# function for our web application
def home():
    return jsonify ({"Message": "Welcome to the home api"})




# defining a simple route/endpoint
@app.route("/api/products")
# corresponding function for our web application
def products():
    return jsonify ({"Message" : "Welcome to the products api"})


# run the app when this file is executed
app.run(debug= True)