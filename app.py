from flask import Flask, render_template, request

app = Flask(__name__)

# 1. Automatically create a database for TAG001 through TAG100
# Replace 'hansh@example.com' with your actual email if you want it in the logs
owner_db = {f"TAG{i:03d}": "hansh@example.com" for i in range(1, 101)}

@app.route('/')
def home():
    return "<h1>QR Lost & Found System is Online</h1><p>The server is running perfectly. Scan a tag to begin.</p>"

@app.route('/tag/<tag_id>')
@app.route('/TAG/<tag_id>')  # Handles phones that auto-capitalize
def view_tag(tag_id):
    # Convert input to uppercase to match our owner_db keys
    tag_id_upper = tag_id.upper()
    
    if tag_id_upper in owner_db:
        return render_template('index.html', tag_id=tag_id_upper)
    
    return f"<h1>Invalid Tag: {tag_id}</h1><p>This tag is not registered in the system.</p>", 404

@app.route('/send-message', methods=['POST'])
def send_message():
    tag_id = request.form.get('tag_id')
    message_content = request.form.get('message')
    owner_email = owner_db.get(tag_id, "Unknown Owner")

    # This message will appear in your Render Dashboard 'Logs'
    print(f"--- NEW MESSAGE FOR {tag_id} ---")
    print(f"Owner Email: {owner_email}")
    print(f"Message from Finder: {message_content}")
    print("---------------------------------")

    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
