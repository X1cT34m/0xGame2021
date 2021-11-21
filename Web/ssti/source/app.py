from flask import Flask, request, render_template_string, abort

app = Flask(__name__)


@app.route("/")
def index():
    search = request.args.get("search") or "None"
    blacklist = ["class", "+", "__", "\\", "attr"]
    for i in blacklist:
        if i in search:
            abort(500)
    return render_template_string("Searching for: %s?" % search)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
