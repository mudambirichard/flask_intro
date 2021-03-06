from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

	def test_home(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/auth/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)

    
        def test_login_page_loads(self):
    	    tester = app.test_client(self)
    	    response = tester.get('/api/v1/auth/login', content_type='html/text')
    	    self.assertTrue(b'Please login' in response.data)

     ## test login page
    	def test_correct_login(self):
    		tester = app.test_client(self)
    		response = tester.post(
    			'/login',
    			data=dict(username="admin", password="admin"),)
    		self.assertIn(b'You were just logged in!', response.data)


    	def test_correct_login(self):
    		tester = app.test_client(self)
    		response = tester.post(
    			'/api/v1/auth/login',
    			data=dict(username="wrong",  password="wrong"),
    			)
    		self.assertIn(b'Invalid credentials. Please try again.', response.data)


        def test_register_page_loads(self):
    	    tester = app.test_client(self)
    	    response = tester.get('/api/v1/auth/register', content_type='html/text')
    	    self.assertTrue(b'Please register' in response.data)


    	def test_post_page_loads(self):
    	    tester = app.test_client(self)
    	    response = tester.get('/api/v1/auth/post', content_type='html/text')
    	    self.assertFalse(b'Please post' in response.data)

    		
    	def test_delete_page_loads(self):
            tester = app.test_client(self)
            response = tester.get('/api/v1/auth/delete', content_type='html/text')
            self.assertFalse(b'Please delete' in response.data)

        def test_get_page_loads(self):
            tester = app.test_client(self)
            response = tester.get('/api/v1/auth/get', content_type='html/text')
            self.assertFalse(b'Please get' in response.data)

        def test_put_page_loads(self):
            tester = app.test_client(self)
            response = tester.put('/api/v1/auth/put', content_type='html/text')
            self.assertFalse(b'Please put ' in response.data)

if __name__ == '__main__':
	unittest.main()