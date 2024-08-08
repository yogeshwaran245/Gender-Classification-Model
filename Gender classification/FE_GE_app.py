from flask import Flask,request,jsonify,render_template
import json
import pickle
import numpy as np
app=Flask(__name__)

@app.route("/usecase_name",methods=["GET"])
def usecase():
    return ("Gender Classfication using face measurements")


with open("D:\\NLC_Projects\\Gender classification\\GEC.pkl","rb") as pickle_file:
        load_model=pickle.load(pickle_file)


@app.route("/predict",methods=["POST"])
def predict():
    request_data=request.json

    features=np.array([request_data['long_hair'],
        request_data['forehead_width_cm'],
        request_data['forehead_height_cm'],
        request_data['nose_wide'],
        request_data['nose_long'],
        request_data['lips_thin'],
        request_data['distance_nose_to_lip_long']
    ]).reshape(1, -1)

    prediction=load_model.predict(features)
    return jsonify({"Gender":int(prediction[0])})

@app.route("/home",methods=["GET"])
def home():
     return render_template("index.html")

@app.route('/handle_data',methods=["POST"])
def handle_data():
    long_hair=float(request.form.get("long_hair"))
    forehead_width_cm=float(request.form.get("forehead_width_cm"))
    forehead_height_cm=float(request.form.get("forehead_height_cm"))
    nose_wide=float(request.form.get("nose_wide"))
    nose_long=float(request.form.get("nose_long"))
    lips_thin=float(request.form.get("lips_thin"))
    distance_nose_to_lip_long=float(request.form.get("distance_nose_to_lip_long"))

    with open("D:\\NLC_Projects\\Gender classification\\GEC.pkl","rb") as pickle_file:
        load_model=pickle.load(pickle_file)
    features=np.array([long_hair,forehead_width_cm,forehead_height_cm,nose_wide,nose_long,lips_thin,distance_nose_to_lip_long]).reshape(1,-1)

    prediction=load_model.predict(features)
    Predicted_gender="Male" if prediction[0]== 0 else "Female"
    
    return render_template("predicit.html",Predicted_gender=Predicted_gender)

if __name__=='__main__':
    app.run(debug='True')
