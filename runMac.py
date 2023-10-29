import os
os.system('source venv/bin/activate')
os.system('pip install -r requirements.txt')
os.system('export FLASK_APP=BBapp')

from BBapp import app

if __name__ == '__main__':
    #using loopback address and default flask port
    app.run(host='127.0.0.1', port=5000) #can set debug by adding debug=True