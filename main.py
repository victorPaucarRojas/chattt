from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/", methods=[ "POST"])
def hola_mundo():
    import pusher
    data = request.get_json()
   
    pusher_client = pusher.Pusher(
        app_id = "2065486",
        key = "408a069d97c7435b78a7",
        secret = "bf6a13248611bb7f2aa6",
        cluster = "mt1",
        ssl=True
    )

    pusher_client.trigger('my-channel', 'my-event', {'message':data["message"]})
    return ".."

if __name__ == "__main__":
    app.run(debug=True)