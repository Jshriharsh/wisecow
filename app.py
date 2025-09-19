from flask import Flask, Response
import subprocess

app = Flask(__name__)

@app.route("/")
def cow():
    try:
        out = subprocess.check_output(["fortune", "-s"])
        cow = subprocess.check_output(["cowsay"], input=out)
        return Response(cow, mimetype="text/plain")
    except Exception as e:
        return Response(f"error: {e}\n", mimetype="text/plain", status=500)

@app.route("/health")
def health():
    return {"status":"ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4499)
