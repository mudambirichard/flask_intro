from flask import Flask , render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def home():
	return " Kisumu Hotel"

	
@app.route('/welcome')
def welcome():
	return render_template('welcome.html')
	
@app.route('/login')
def login():
	return redirect(url_for('login_page'))
@app.route('/api/v1/auth/login', methods=['GET', 'POST'])
def login_page():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin'  or  request.form['password'] != 'admin':
			error = 'Invalid credentials. Please try again.'
		else:
			
			return redirect(url_for('login.html'))
	return render_template('login.html', error=error)

@app.route('/register')
def register():
	return redirect(url_for('register_page'))
@app.route('/api/v1/auth/register', methods=['GET', 'POST'])
def register_page():
	error = None
	if request.method == 'POST':

	    return redirect(url_for('register.html'))
	return render_template('register.html', error=error)


@app.route('/post')
def post():
	return redirect(url_for('post_page'))
@app.route('/api/v1/auth/post', methods=['GET', 'POST'])
def post_page():
	error = None
	if request.method == 'POST':
		
	    return redirect(url_for('post.html'))
	return render_template('post.html', error=error)

@app.route('/delete')
def delete():
	return redirect(url_for('post_page'))
@app.route('/api/v1/auth/delete', methods=['GET', 'POST'])
def delete_page():
	error = None
	if request.method == 'POST':
		
	    return redirect(url_for('delete.html'))
	return render_template('delete.html', error=error)


@app.route('/get')
def get():
	return redirect(url_for('get_page'))
@app.route('/api/v1/auth/get', methods=['GET', 'POST'])
def get_page():
	error = None
	if request.method == 'POST':
		
	    return redirect(url_for('get.html'))
	return render_template('get.html', error=error)


@app.route('/put')
def put():
	return redirect(url_for('post_page'))
@app.route('/api/v1/auth/put', methods=['GET', 'POST'])
def put_page():
	error = None
	if request.method == 'POST':
		
	    return redirect(url_for('put.html'))
	return render_template('put.html', error=error)
	

if __name__ == '__main__':
	app.run(debug=True)