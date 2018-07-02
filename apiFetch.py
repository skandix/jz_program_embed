# -*- coding: utf-8 -*-
from requests import get

def getData(url="https://sleepingpill.javazone.no/public/allSessions/javazone_2018"):
    return get(url).json()

def api_format(url):
	api = getData()['sessions']
	sessid = url.split('/')[-1]

	for data in range(len(api)):
		if (api[data]['sessionId']) in sessid:
			speaker_url = (api[data]['speakers'][0]['pictureUrl'])
			speaker_name = (api[data]['speakers'][0]['name'])
			abstract = (api[data]['abstract'])
			room = (api[data]['room'])[0].upper()+(api[data]['room'])[1:]
			formaat =  (api[data]['format'])[0].upper()+(api[data]['format'])[1:]
			length = (api[data]['length'])+" Min"
			title = (api[data]['title'])
			return (speaker_url, speaker_name, abstract, room, formaat, length, title)

if __name__ == '__main__':
	hmm = (api_format("https://2018.javazone.no/program/92799046-8f4d-45ef-af0f-20767b8041f9"))
	for k in hmm:
		print(k)