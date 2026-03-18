from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>QR Lost & Found System is Online</h1><p>The server is running perfectly. Scan a tag to begin.</p>"
# Mock database mapping Tag IDs to Owner Emails
# In a real app, you'd use a SQL database
owner_db = {f"TAG{i:03d}": "hansh@example.com" for i in range(1, 101)}

@app.route('/tag/<tag_id>')
def view_tag(tag_id):
    if tag_id in owner_db:
        return render_template('index.html', tag_id=tag_id)
    return "Invalid Tag", 404

@app.route('/send-message', methods=['POST'])
def send_message():
    tag_id = request.form.get('tag_id')
    message_content = request.form.get('message')
    owner_email = owner_db.get(tag_id)
    print(f"Sending message to {owner_email}: {message_content}")
    
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
