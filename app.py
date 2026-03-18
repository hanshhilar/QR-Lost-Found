from flask import Flask, render_template, request

app = Flask(__name__)

# 1. Database for TAG001 through TAG100
# All tags are currently mapped to your email for testing.
owner_db = {f"TAG{i:03d}": "hansh@example.com" for i in range(1, 101)}

@app.route('/')
def home():
    return "<h1>QR Lost & Found System is Online</h1><p>The server is running perfectly. Scan a tag to begin.</p>"

@app.route('/tag/<tag_id>')
@app.route('/TAG/<tag_id>')  # Handles browsers that auto-capitalize
def view_tag(tag_id):
    # Standardize the ID to uppercase
    clean_id = tag_id.upper()
    
    if clean_id in owner_db:
        # Passes the tag_id to your index.html template
        return render_template('index.html', tag_id=clean_id)
    
    return f"<h1>Error: Tag {clean_id} Not Found</h1><p>This ID is not in the system.</p>", 404

@app.route('/send-message', methods=['POST'])
def send_message():
    tag_id = request.form.get('tag_id')
    message_content = request.form.get('message')
    owner_email = owner_db.get(tag_id, "Unknown Owner")

    # These messages appear in your Render 'Logs' tab
    print(f"--- NEW MESSAGE FOR {tag_id} ---")
    print(f"Finder Message: {message_content}")
    print("---------------------------------")

    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
