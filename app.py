from flask import Flask, render_template, request

app = Flask(__name__)

# Mock database mapping Tag IDs to Owner Emails
# In a real app, you'd use a SQL database
owner_db = {
    "TAG123": "owner@email.com",
    "TAG124": "another_owner@email.com"
}

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