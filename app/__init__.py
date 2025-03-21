from flask import Flask
from routes import main

def creat_app():
    app=Flask(__name__)
    app.config('SECRET_KEY')='yabhabisthegratestever'
    app.register_blueprint(main)
    return app

# if __name__=='__main__':
#     app.run(debug=True)