from RandCRM import app

@app.route("/")
def index():
    return "Hello CRM"
