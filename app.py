
from flask import Flask, render_template, request

app = Flask(__name__)

# This creates the database for 100 tags
owner_db = {f"TAG{i:03d}": "hansh@example.com" for i in range(1, 101)}

@app.route('/')
def home():
    return "<h1>System is Online</h1><p>Type /tag/TAG001 at the end of the URL to test.</p>"

# This route is "Bulletproof" - it handles /tag/, /TAG/, and different IDs
@app.route('/tag/<tag_id>')
@app.route('/TAG/<tag_id>')
def view_tag(tag_id):
    clean_id = tag_id.upper().strip()
    if clean_id in owner_db:
        return render_template('index.html', tag_id=clean_id)
    return f"<h1>ID Not Found: {clean_id}</h1><p>Check your owner_db!</p>", 404

@app.route('/send-message', methods=['POST'])
def send_message():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
