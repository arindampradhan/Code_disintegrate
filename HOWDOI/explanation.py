import argparse
import glob
import os
import random
import requests
import requests_cache
import sys
# from . import __version__

try:
	from urllib.parse import quote as url_quote
except ImportError:
	from urllib import quote as url_quote



try:
	from urllib import getproxies
except ImportError:
	from urllib.request import getproxies

# from pygments import hightlight
# from pygments.lexers import guess_lexer,get_lexer_by_name
# from pygments.formatters import TerminalFormatter
# from pygments.util import ClassNotFound

# from pyquery import PyQuery as pq
# from request.exceptions import ConnectionError
from requests.exceptions import SSLError

if sys.version < '3':
	import codecs 
	def u(x):
		return codecs.unicode_escape_decode(x)[0]
else:
	def u(x):
		return x







# def get_proxies():


# def is_question(link):

def get_links(query):
	# calling get_result for answers 
	result = get_result(SEARCH_URL.format(URL,url_quote(query)))
	html = pq(result)
	return [a.attrib['href'] for a in html)'.l']


def get_result(url):
	try:
		# requsting the related urls
		return requests.get(url, headers={'User-Agent': random.choice(USER_AGENTS)}, proxies=get_proxies()).text
	except requests.exceptions.SSLError as e:
		print('[ERROR] Encountered an SSL Error. Try using HTTP instead of '
              'HTTPS by setting the environment variable "HOWDOI_DISABLE_SSL".\n')
        raise e



# def get_link_at_pos(links,position):

# def format_output(code,args):

# def get_answer(args,links):

def get_instructions(args):
	links = get_links(args['query'])
	"""sends a string of query with \'?\' deleted"""
	if not links:
		return False

	answers=[]
	append_header = args['num_answers'] > 1
	initial_position = args['pos']


def enable_cache():
	if not os.path.exists(CACHE_DIR):
		os.makedirs(CACHE_DIR)
	requests_cache.install_cache(CACHE_FILE)

def clear_cache():
	for cache in glob.glob('{0}*'.format(CACHE_FILE)):
		os.remove(cache)
		# The method remove() removes the file path. If the path is a directory, OSError is raised
		# os.remove(path)


def howdoi(args):
	"""args is a dictionary and here the query tag's element is changed 
	joining all the elements in list by spaces and removing ? character""" 
	args['query']=' '.join(args['query']).replace('?','')
	
		# calling get_instructions if not found give a sorry statement
		# if does not call then network conectn problem
	try:
		return get_instructions(args) or "Sorry ,couldn\'t find any help with that topic\n"
	except:
		return "failed to establish network connection\n"


def get_parser():
	parser = argparse.ArgumentParser(description='instant coding answers via the command line')	
	parser.add_argument('query',metavar='QUERY',type=str,nargs='*',help='the question to answer')
	parser.add_argument('-p','--pos',help='display the full text of the answer',action='store_true')
	parser.add_argument('-a','--all',help='display the full text of the answer',action='store_true')
	parser.add_argument('-l','--link',help='display the answer link',action='store_true')
	parser.add_argument('-c','--color',help='enable colorized output',action='store_true')
	parser.add_argument('-n','--num-answers',help='number of answer to return',default=1,type=int)
	parser.add_argument('-C','--clear_cache',help='clear the cache',action='store_true')
	parser.add_argument('-v','--version',help='displays the current version of howdoi',action='store_true')
	return parser



def command_line_runner():
	parser = get_parser()
	args = vars(parser.parse_args())
	# vars() and locals()
	# ===================
	# Now, to answer another part of your question.  vars() (or locals()) provides low level access to variables created by python. Thus the following two lines are equivalent.
	# locals()['x'] = 4
	# x = 4
	# The scope of vars()['x'] is exactly the same as the scope of x. One problem with locals() (or vars()) is that it will let you put stuff in the namespace that you can't get out of the namespace by normal means. So you can do something like this: locals()[4] = 'An integer', but you can't get that back out without using locals again, because the local namespace (as with all python namespaces) is only meant to hold strings.
	# http://stackoverflow.com/questions/980249/difference-between-dir-and-vars-keys-in-python
	
	if args['version']:
		print (__version__)
		return 
	# http://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package

	if args['clear_cache']:
		clear_cache()
		print('Cache cleared successfully')
		return
	if not args['query']:
		parser.print_help()
		return 

	# enable the cache if user doesn't want it to be disabled
	if not os.getenv('HOWDOI_DISABLE_CACHE'):
		# https://mail.python.org/pipermail/new-bugs-announce/2007-September/000149.html
		enable_cache()

	if sys.version < '3':
		print(howdoi(args).encode('utf-8','ignore'))
		# calling howdoi function
	else:
		print(howdoi(args))



if __name__ == '__main__':
	command_line_runner()


args is a directory 

# command_line_runner
# 				|----------parser object
# 				|----------creating args object from parser as vars
# 				|----------version
# 				|----------clear_cache
# 				|			|-------format_file
# 				|
# 				|----------not given any Argument
# 				|			|-------print_help
# 				|----------not disable cache
# 				|			|-------enable_cache
# 				|					|-----if cache not exist
# 				|							|-----make a folder CACHE_DIR and requests_cache install
# 				|-----------call howdoi(args)



args = {'query':["all",'that','i','asked']}

howdoi
	|-------join the query list with spaces
	|			|------list is now a string with spaces 'query':"all that i asked"
	|-------try---get_instructions(args)
	|				|------link->get_link(args[query_string])
	|								|---->>>
	|
	|-------except ConnectionError


>>>get_link("single string of the name you gave as args"):
	|----result=get_result(SEARCH_URL.format(URL,url_quote(query)))
	|			|---
	|
	|----html = pq(result)
	|----return [a.attrib['href'] for a in html('.l')] or \
        [a.attrib['href'] for a in html('.r')('a')]
