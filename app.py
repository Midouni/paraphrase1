from flask import Flask, request, render_template
from model.GPT2_model import fun

app=Flask(__name__)



@app.route('/',methods=['POST',"GET"])
def index():
    if request.method=='POST':
        data=request.get_json()
        #use the paraphrase model and return to the frontend
        print(data["text"])
        test=fun(data["text"])
        response={"text":test}
        return response
    else:
        return render_template("index.html")



    

#run the server
if __name__== "__main__":
    app.run(debug=True)