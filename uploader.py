import asyncio
import requests
import os

async def TryUpload(what,holder,operation,url):
	await asyncio.sleep(0.2);
	print("\n[send attempt starting]\n\t");

	# where to sync
	theurl = url;
	verdict = "failed";
	response = {'text':"nothing yet"}

	# send file if it exists
	try:
		data = {'mykey' : 'callmecory','myfolder':holder,'operation':operation,'fname':what};
		print(f"\n what -> {what}");

		if os.path.isfile(what):
			# run updater
			with open(what) as f:
				files = {'myfile' : f}
				
				response = requests.post(theurl,data = data,files = files);
				answer = getans(response);
				verdict = "successful" if response.status_code == 200 else "failed";
		else:
			# run deletion
			response = requests.post(theurl,data = data);
			answer = getans(response)
			verdict = "successful" if response.status_code == 200 else "failed";
			# answer = "file doesnt exist"
	except Exception as e:
		answer = e;
		raise e

	print(answer);
	print(f"\n[send attempt for `{what}` {verdict}]----\n")

def send2server(fpath,container,op,theurl):
	asyncio.run(TryUpload(fpath,container,op,theurl));

def getans(what):
	response = what;

	if(response.status_code == 200):
		answer = response.text;
	else:
		answer = f"error syncing file\n[{response.status_code}] -> check if you have a stable internet connection\ncheck if `{response.url}` is correct";

	return answer;