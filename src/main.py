from flask import Flask

app = Flask(__name__)

content_paths = {
    "audio1":"static/audio1"
} # follows <cdn file name>:<static file path>

@app.route('/')
def index():
    return 'Ping!'

@app.route('/cdn/get/<fileName>')
def cdnGet(fileName):
    fileName = str(fileName)
    if fileName == "":
        return "No file name", 401
    # Get and return the file
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=true)
