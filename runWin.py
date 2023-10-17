from flask import Flask
import os
os.system('/venv/Scripts/activate')
os.system('pip install -r requirements.txt')
os.system('set FLASK_APP=BBapp')
#keep in mind the first os command depends on what you named your virtual environment and where it is located

from BBapp import app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000) #can set debug by adding debug=True
