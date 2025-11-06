from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

    return render_template('contact.html')

# @app.route('/send_message', methods=['POST'])
# def send_message():
#     name = request.form.get('name')
#     email = request.form.get('email')
#     message = request.form.get('message')

#     # In a real application, you would process the form data here
#     # For now, we'll just show a success message
#     flash(f'Thank you {name} for your message! We will get back to you soon.', 'success')
#     # print("Send message button called")
#     return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
