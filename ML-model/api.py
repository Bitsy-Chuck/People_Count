import json
import os
import sys
from flask import Flask,jsonify, request, redirect, url_for
# from flask_cors import CORS
# import people_counter


app= Flask(__name__)
# CORS(app)

ans=None

@app.route("/getResult", methods=["GET", "POST"])
def getResult():
    try:
        print("inside GetResult")
        if request.method=="GT":
            print("abc")
            uid= request.json
            print("uid", uid)
            error_code=run_countPeople(uid)
            if(error_code==1):
                line=""
                with open("res.txt", 'r') as f:
                    line=f.read()
                    print(line)
                return jsonify({"total": line})
            else:
                print("error in security footage")
        else:
            print("not")
            uid=1
            error_code=1#run_countPeople(uid)
            if(error_code==1):
                line=""
                with open("res_1.txt", 'r') as f:
                    line=f.read()
                    print(line)
                return jsonify({"total": line})
            else:
                print("error in security footage")
                return "noni"

    except:
        print("error in getResult")

# def run_countPeople(place_uid):
#     try:
#         people_counter.run(place_uid)
#         return 1
#     except:
#         print("Error in run_countPeople")
#         return -1

if __name__=='__main__':
    app.run(debug=True)
