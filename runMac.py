from flask import Flask
import os
os.system('source venv/bin/activate')
os.system('pip install -r requirements.txt')
os.system('export FLASK_APP=BBapp')
#disclaimer I don't have a mac so haven't tested this also keep in mind the first os command depends on what you named your virtual environment and where it is located

from BBapp import app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000) #can set debug by adding debug=True