"""
this file should be the api of your remote server
for example, your login service from your company
e.g. provide email and password, send this information to your remote server
waiting for the response from remote server. If remote server authorized this email and password
then it will be ok to login this user.
"""

def authenticate(username, password):
	"""

	:param username:
	:param password:
	:return:
	"""
	server_url = "https://yourloginservice.com"
	auth_url = '%s/auth' % server_url
	param_dict = dict(login=username, password=password)
	headers = "prepare your data"
	""" 
	# this is an example of real world case
	auth_result = requests.post(
	    auth_url, json=param_dict, headers=headers, verify=False)
	if auth_result.status_code != 200:
	    logger.warn("failed to auth user: %s, status: %s, response: %s " %
	                (username, auth_result.status_code, auth_result.text))
	    return None
	result_dict = auth_result.json()
	userinfo = dict(
	    username=username)
	return userinfo
	"""

	# mock the server response here
	if username == 'Admin@example.com':
		userinfo = dict(username=username)
		return userinfo
	else:
		return None
