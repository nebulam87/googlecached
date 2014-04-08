#!/usr/bin/python

import httplib
import optparse

def queryGoogleCache(queryUrl):
	# Configure parameters for HTTP request
	domain = 'webcache.googleusercontent.com'
	hostname = 'webcache.googleusercontent.com'
	resourc = '/search?q=cache:' + queryUrl + '&strip=1'
	userAgent = 'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0)' # AOL 9.7 WinXP IE 8 based
	print "[+] URL Address to be sent: http://" + domain + resourc + "\n"	

	# Building HTTP request
	cacheReq = httplib.HTTP(domain)
	cacheReq.putrequest('GET', resourc)
	cacheReq.putheader('Host', hostname)
	cacheReq.putheader('User-Agent', userAgent)
	cacheReq.endheaders()
	
	# Get & store responses
	respCode, respMsg, headers = cacheReq.getreply()
	return str(respCode)

def main():
	parser = optparse.OptionParser()
	parser.add_option('-u', '--url', dest='queryUrl', type='string', metavar='<URL address>', help='Stores the URL address that is going to be searched on Google cache')

	(options, args) = parser.parse_args()
	
	if options.queryUrl == None:
		print parser.print_help()
		exit(0)

	else:
		urlIsCached = queryGoogleCache(options.queryUrl)
		
		# Check if response code was 200 or 404
		if "200" in urlIsCached:
			print "The given URL Address is cached on Google."
		
		elif "404" in urlIsCached:
			print "The given URL Address is not cached on Google."
		
		elif ("404" or "200") not in urlIsCached:
			print "I can't tell if this URL Address is cached or not... check your query!"

if __name__=="__main__":
	main()
			
