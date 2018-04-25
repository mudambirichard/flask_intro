from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)

    
        def test_login_page_loads(self):
    	    tester = app.test_client(self)
    	    response = tester.get('/login', content_type='html/text')
    	    self.assertTrue(b'Please login' in response.data)

    	def test_correct_login(self):
    		tester = app.test_client(self)
    		response = tester.post(
    			'/login',
    			data=dict(username="admin", password="admin"),)
    		self.assertIn(b'You were just logged in!', response.data)

    	def test_correct_login(self):
    		tester = app.test_client(self)
    		response = tester.post(
    			'/login',
    			data=dict(username="wrong", password="wrong"),
    			)
    		self.assertIn(b'Invalid credentials. Please try again.', response.data)


        def test_register_page_loads(self):
    	    tester = app.test_client(self)
    	    response = tester.get('/register', content_type='html/text')
    	    self.assertTrue(b'Please register' in response.data)

    	def test_post_page_loads(self):
    	    tester = app.test_client(self)
    	    response = tester.get('/post', content_type='html/text')
    	    self.assertFalse(b'Please post' in response.data)	
    		
    	

if __name__ == '__main__':
	unittest.main()