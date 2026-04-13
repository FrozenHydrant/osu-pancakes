from flask import Flask

class App:
    
    my_app: Flask = Flask(__name__)
    instance = None
    

    def __init__(self):
        if App.instance is None:
            App.instance = self
        else:
            raise Exception("Can't have more than one app.")


    @my_app.route("/")
    def read_root():
        return "Hello World"
        
    
    def start(self):
        App.my_app.run()


if __name__ == "__main__":
    app = App() # Need initialization
    app.start()