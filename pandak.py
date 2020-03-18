import websocket, json, time, datetime,requests
from datetime import datetime

import time, requests, random
sandi = input('Masukan password : ')
if sandi == 'firman12':
	print('Welcome client roki /njangan lupa istirahat?')
else:
    ws.close()
xz = 1
status = 'tidur'
nama = 'xyx'
judul = 'xyz'
timeh = datetime.today()
response3 = '{"div":"hai"}'
createdl = datetime.today()
z = 0
namal = 'xyz'
judull = 'xwx'
timehl2 = datetime.today()


botauthtoken2 = 'f2403d5c8c8a51ad7dba69e1c75f72e75349d5aa' #token lu disini

rscode=0
while rscode!=1:
	#nomor = "06802143801"
	nomor="085705873584"
	###nomor = input("masukkan nomor telepon : ")
	password="kambing1"
	###password = input("masukkan password : ")
	headers={"User-Agent":"Mozilla/5.0"}
	response=requests.post('https://id-api.spooncast.net/signin/?version=2',headers=headers,json={"sns_type":"phone","sns_id":nomor,"password":password})
	#print(response.json())
	rscode = response.json()['results'][0]['result_code']
	if rscode !=1:
		print("nomor atau password salah , ulangi lagi")
print("berhasil login")
tirublock=response.json()['results'][0]['tag']
#time.sleep(100)
tokenl=response.json()['results'][0]['token']
print(response.json()['results'][0]['nickname'])
botauthtoken2=tokenl

txtid = input('Link Live nya  : ')
response = requests.get(txtid)
urlo = response.url
slink = urlo[34:-59]
socketstring = ("wss://id-heimdallr.spooncast.net/" + slink)
print(socketstring)

mypesan = '{"live_id":'+slink+',"token":"'+botauthtoken2+'","event":"live_join","appversion":"4.3.16","useragent":"Android"}'###### end 



def on_message(ws, message):
        global judul
        global nama
        global response3
        global status
        global timeh
        global timehl2
        global xz
        global z
        global response2
        chat = json.loads(message)
        uid = chat['data']['author']['id']
        nick = chat['data']['author']['nickname']
        evn = chat['event']
        kesurupan = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"HAI TUANKU PANPAN, ANDA MEMANGGIL SAYA...."}'
        if 1 == 1:
            if z == 0:
                ws.send(kesurupan)
                z = 1
        if evn == 'live_message':
            psn = chat['data']['message']
            tag = chat['data']['author']['tag']
            print(chat['data']['author']['tag'])
        emot = ['🤭🤭🤭', '🙄🙄🙄', '😝😝😝', '😇😇😇', '😌😌😌', '😔😔😔', '🥺🥺🥺']
        ya = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"' + nick + '   Sokap Lau Nanya Mulu💆  ' + random.choice(emot) + '"}'
        tidak = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"' + nick + '  Tanyakan Saja Pada Rumput Yang Bergoyang ' + random.choice(emot) + '"}'
        bisajadi = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":"' + nick + '  Saya Tidak Perduli Dengan Pertanyaan Anda ' + random.choice(emot) + '"}'
        bodoamat = '{"appversion":"4.3.16","event":"live_message","token":" ","useragent":"Android","message":"' + nick + ' bodo amat 😝 ga peduli 😚 ' + random.choice(emot) + '"}'
        listjawaban = [
         ya, tidak, bisajadi, bodoamat]
        if evn == 'live_message' and psn[:1].lower() == 'a' and psn[-1:] == '?':
           kambeng = random.choice(listjawaban)
           print(kambeng)
           ws.send(kambeng)
        hantu = [' Ku Kasih Tau Ya... Kau Itu Nge Ghost [👻] ',' Astagaa Malah Nge Ghost [👻] ','  Jangan Nge Ghost [👻] Anjiir" ','  Kamu Nge Ghost [👻] Ku Kick" ' ]
        lsjoin = '{"appversion":"4.3.16","event":"live_message","token":"","useragent":"Android","message":" ' + nick + random.choice(hantu) + '😕' + '"}'
        sapa = ['   Hii, Kamu Imut 😙 . Tapi Boong 🤣 ','   Gimana Kabar Nya😉 ','   Long Time No See..🙆 ','   Semoga Harimu Menyenangkan ','    Hi. Rindu aku Ya😄 ','   kamu Apa Kabar ','  Tap❤️ Ya Atau Ngga Kasih Gift
