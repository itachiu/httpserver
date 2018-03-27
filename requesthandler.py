import time

def requesthandler(request):

	status_flag = False

	status_code = {
               	'100':'continue',
                '101':'Switching Protocals',
                '200':'OK',
                '201':'Created',
                '202':'Accepted',
                '203':'Non-Authorative Information',
                '204':'No Content',
                '205':'Reser Content',
                '206':'Partial Content',
                '300':'Multiple Choices',
                '301':'Moved Permanently',
                '302':'Found',
                '303':'See Other',
                '304':'Not Modified',
                '305':'Use Proxy',
                '307':'Temperary Redirect',
                '400':'Bad Request',
	            '401':'Unauthorized',
                '402':'Payment Required',
                '403':'Forbidden',
                '404':'Not Found',
                '405':'Method Not Allowed',

                }


	request_dismantle = request.split('\n')
	#print request_dismatle[0]
	l = request_dismantle[0].split(' ')
	request_method = l[0]
	request_http_version = l[-1]
	request_dismantle = request_dismantle[1:]

	for i in request_dismantle:
		request_charaters = i.split(':')


	index_page = open('index.html', 'r')

	if 'GET' in request_method:
		code = '200'
		status_codes = status_code['200']
		if 'HTTP/1.1' in request_http_version:
			response_http_version = 'HTTP/1.1'
		elif 'HTTP/1.0' in request_http_version:
			response_http_version = 'HTTP/1.0'
	else:
		code = '405'
		status_codes = status_code['405']
		status_flag = True

	Date = 'Date: '+str(time.ctime())+' IST\n'

	server = 'Server: Python Server\n'

	Last_modified = 'Last-modified: SUN, 4 Mar 2018, 8:38:33 PM IST\n'

	Content_Type = 'Content-Type: text/html\n'

	Connection =  'Conncetion: Closed\n'

	response_body = Date+server+Last_modified+Content_Type+Connection

	response_header = response_http_version+' '+str(code)+' '+str(status_codes)
	response = response_header+"\n"+response_body+str(index_page.read())

	return response
