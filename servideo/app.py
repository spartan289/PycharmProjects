from flask import Flask
from flask_autoindex import AutoIndex

app = Flask(__name__)

ppath = r"C:\Users\sagar\PycharmProjects\servideo\videofiles" # update your own parent directory here

AutoIndex(app, browse_root=ppath)

if __name__ == "__main__":
    app.run()