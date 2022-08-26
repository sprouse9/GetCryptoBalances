
import requests
import json
import time
import datetime
import AppKit


headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15',
	'Accept-Language': 'en-us',
	'Referer': 'https://www.google.com',
	'Accept-Encoding': 'gzip, deflate, br'
}

apikey='HTNSPQ164XX8PT6H5JRAMWW7WIBKMQG3YB'

mmAddresses = [	'0x0243d644f57A6e9C62c4F353eBd2490F3853bA40',
				'0xE276AF5FBad054Bef5a7db32c3624d1aEFfdc283',
				'0xc1ce6c003b96d45035937fa567f20319291d8b40',
				'0xc2bb1be2e17b69228cd9c4a17a5908a508ac92af',
				'0xa8237f1b810428687e8cbd2639b14cacf5e37e5d',
				'0x876475b6dc308ed04415e336f9601d7de8b7806a',
				'0x7352a521d4b95cf9e765e7840212f10a0e64d01b',
				'0x7009da437ad1f38fdba38c299d9e27fc9bad8304',
				'0x01da681b00de990dc96bfeb364f250f1b5569150',
				'0x0805b0562d4bb9821cb6418a9d1bca35c09b0097',
				'0x4477c3d5390247f623b4d98b22e7904ac9c7ee7d',
				'0xf62e8638649995149782b4058dac4c41ca5ba95e' ]

URLS = []
runningTotal = 0.0

# build the URL's

for mmAddress in mmAddresses:
	URLS.append("https://api.bscscan.com/api?module=account&action=balance&address=" + mmAddress + "&apikey=" + apikey)

e = datetime.datetime.now()
print("%s/%s %s:%s" % (e.month, e.day, e.hour, e.minute) )

# Now call (GET) each item in URLS
count = 0

for url in URLS:
	r = requests.get(url, headers = headers)
	data = r.json()

	# Data looks like this:		{'status': '1', 'message': 'OK', 'result': '98213164370370370380'}

	# cast the string to float and set to 2 decimal places on one line
	balance = data.get("result")
	floatBalance = float( balance) / 1000000000000000000
	count += 1
	print ("MM-%2.2d: %3.4f" % (count, floatBalance) )
	#print ( "MM-: ", {:.}, "{:.2f}".format(floatBalance) )

	runningTotal += floatBalance



print ("\nTotal: %3.4f BNB" % runningTotal )












