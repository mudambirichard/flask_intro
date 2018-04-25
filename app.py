from flask import Flask , render_template, redirect, url_for, request



app = Flask(__name__)


@app.route('/')
def home():
	return " Kisumu Hotel"

	
@app.route('/welcome')
def welcome():
	return render_template('welcome.html')
	
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials. Please try again.'
		else:
			
			return redirect(url_for('login.html'))
	return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
	error = None
	if request.method == 'POST':

	    return redirect(url_for('home'))
	return render_template('register.html', error=error)


@app.route('/post', methods=['GET', 'POST'])
def post():
	error = None
	if request.method == 'POST':
		
	    return redirect(url_for('home'))
	return render_template('post.html', error=error)

if __name__ == '__main__':
	app.run(debug=True)