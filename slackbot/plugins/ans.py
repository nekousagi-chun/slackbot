from slackbot.bot import respond_to,listen_to

@respond_to('登山')
def ans(message):
     message.reply('頑張ってよう来たかび')

@respond_to('下山')
def ans(message):
	message.reply('今日もよう頑張ったかび')

@respond_to('眠い')
def ans(message):
	message.reply('ねろかび')

@respond_to('おなかすいた')
def ans(message):
	message.reply('ぶたかび')

@respond_to('大阪の天気')
def weather(message):
	import urllib
	import json

	url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
	# '130010'とすると東京の情報を取得してくれる
	# ここを変えれば任意の地域の天気情報を取得できる
	city_id = '270000'
	
	html = urllib.request.urlopen(url+city_id)
	jsonfile = json.loads(html.read().decode('utf-8'))
	text = jsonfile['description']['text']

	message.send(text)

@respond_to('和歌山の天気')
def weather(message):
	import urllib
	import json

	url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
	# '130010'とすると東京の情報を取得してくれる
	# ここを変えれば任意の地域の天気情報を取得できる
	city_id = '300010'
	
	html = urllib.request.urlopen(url+city_id)
	jsonfile = json.loads(html.read().decode('utf-8'))
	text = jsonfile['description']['text']

	message.send(text)

a = []

@respond_to('BMI計算して')
def height(message):
	message.reply('身長なんぼ？')
	
global h 	
@listen_to('身長' )
def weight(message):
	mes = message.body['text']
	mes = mes.split()
	h = mes[1]
	a.append(h)
	message.reply('体重なんぼ？')

global w 
@listen_to('体重' )
def ans(message):
	print(a)
	mes = message.body['text']
	mes = mes.split()
	w = mes[1]
	message.reply('BMI計算するわ')	
	bmi = 0
	bmi = float(w) /pow(float(a[0])/100,2)
	print(bmi)
	if bmi < 18.5:
		message.reply('痩せすぎやわ，太ろか')
	elif 18.5 < bmi < 25.0:
		message.reply('ちょうどええわ')
	else:
		message.reply('うん，痩せよか')
	
	del a[0]


