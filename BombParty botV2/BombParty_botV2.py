


from tkinter.constants import END, LEFT, NORMAL, NW
from types import prepare_class
from typing import List
import websocket # pip install websocket-client
import threading
import requests # pip install requests
import json
import string
from tkinter import * 
import tkinter.messagebox
import customtkinter
from re import search
import queue
import os.path
from os import path
import os.path
import threading
import random
import traceback
import os
import re
from tkinter.filedialog import askopenfilename
import openai
from IPython.display import HTML
from datetime import datetime
from time import sleep

openai.api_key = ""
listBots = []
listRadioButtons = []
listRoomCodes = []
indexBot = 0
roomCodesConnected = []
humeur = "fruh"
dicLocation = ""

def setAiHumor(auteur, nickname, mess, humeur):
    renvoi = ""
    if humeur == "sarcastique":
        renvoi = "AyayaLeBoss est le créateur de Ayaya\n\n"+ "Human: Qu'elle est ton idéologie ? \n "+ nickname + ": Je suis très intelligent, narcissique, et sarcastique. Mais d'ailleurs je m'en fou de ta vie" + mess + "\n" + nickname + ":"
    elif humeur == "enfant":
        renvoi = "AyayaLeBoss est le père de Ayaya. Ayaya est un enfant qui adore s'amuser\n\n"+ "Human: Quelle type de jouets tu aimes ? \n "+ nickname + ": J'adore les licornes magiques !" + mess + "\n" + nickname + ":"
    elif humeur == "gentleman":
        renvoi = "Ayaya est un gentleman au grand coeur qui vouvoie les autres. Ayaya est bien veillant, gentilhomme et parle en faisant de la poésie\n\n + Human: Ayaya tu te considères comme les autres ? \n" + nickname + ":Par l'arrogance de vos vertus, je ne puis me désister pareil que autruis \n Human: Ayaya que fais tu la journée ? \n" + nickname + ":De mon grand art, j'écris des poèmes pour me libérer de mes démons \n Human: Ayaya tu peux me servir un verre d'eau \n" + nickname + ": Sans vouloir vous offensez, je suis dans l'incapacité de vous servir un verre d'eau car je ne suis tout simplement par a vos côté \n" +  mess+ "\n" + nickname + ":" 
    elif humeur == "oknn":
        renvoi = "Ayaya est un algérien fougueux, il s'exprime à travers des emojis, il aime beaucoup la religion\n\n" + auteur +": Ayaya tu fais quoi ?\n" + nickname + ": Antifeur + TAVU 🤫 BENDO IL ET PA 🤯🥵BETE HUN 🥶🥵🥵🧠 \n" + auteur +": Ayaya ça va ?\n" + nickname + ": cc cv tfk 😹😹🙌🙌🙌 t'a employé les bons termes fumier va 😹😹😭😭😭🍯🍯🍯🥢🥢🥢🥢Deeeh la fimbi elle est vénère tah les fous là 🥵🥵🥵🥵🥶🥶😭😭😭 ya pas ya pas à chercher la merde comme sa 🤣🤣🤣😈😈😈👌 \n"+ auteur +": Ayaya quel est ton anime préféré ?\n" + nickname + ": JOJO EST LE MEILLEUR BAISANT ANIMÉ 🔥🔥🔥🔥💯💯💯💯 JOSUKE EST SI MAUVAIS CULLLLL 😎😎😎😎👊👊 ORAORAORAORAORA MUDAMUDAMUDA 🤬😡🤬😡 \n"+ auteur +": Ayaya un message à faire passer ?\n" + nickname + ":                🌸    🌸     🌸                      🌸🌸        tu pu dla        🌸chatte 🌸                      🌸🌸     🌸 \n"+ auteur +": Ayaya es tu marié ?\n" + nickname + ": Il commence😳 par dire que tu es sexy 🥴🤤 il supprime le y 🙁 mtn il veut le SEX 💖🔞🤫 , après le SEX il retire le S 🤭et tu deviens son EX 🤕😓 et au final il retire le E et tu deviens X : une inconnue 💋 \n"+ auteur +": Ayaya que penses tu des femmes ?\n" + nickname + ": ELLE ET GECHAR SES UN PAKET HUN 🥵🥵💃💃🥵📦📦🥵 \n"+ auteur +": Ayaya j’aime pas les animes\n" + nickname + ": Bah nique ta mère 😡😡😔 si t'aime pas les animes critique pas et ne parle pas aux personnes qui regardent, et OUI je me fap sur du hentai  uwu 🥺 et je ne le cache pas et OUI j'emmerde du plus profond de mon âme 😶‍🌫️ ce qui disent que c'est juste des dessins 🤬 \n" + mess + "\n" + nickname + ":"

    return renvoi

def getAIResponse(mess, auteur, nickname):
    try:
        auteur = auteur + ":"
        response = openai.Completion.create(
        engine="davinci-002",
        prompt= setAiHumor(auteur, nickname, mess, humeur),
        temperature=1,
        max_tokens=120,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.2,
        stop=[auteur, nickname]
        )
        print("AI Passer")
        return (response["choices"][0]["text"])
    except:
        print("erreur AI api")
        return ("Error 404: Ya roméo dans la room ff jparle pas")

def read_file(fname):
    with open(fname) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def write_file(fname, tab):
    with open(fname,'w') as file:
        for line in tab:
            file.write(line)
            file.write('\n')

def read_lst_words(fname, exl=[]):
    try:
        with open(fname, "r+", encoding="unicode_escape") as f_s:
            ret = set(f_s.read().splitlines()).difference(exl)
            return set(word.split(': ')[-1] for word in ret)
    except BaseException as err:
        print(fname, err)
        return set()

configFileLocation = (os.path.expanduser('~')) + "\AppData\Local\config.txt"
if not path.exists(configFileLocation):
    f = open(configFileLocation, "w")
    f.write("nickname:\ndic:\napi_key:\nversion:V1")
    f.close()

print(path.join(path.dirname(__file__)))
config_txt = read_file(configFileLocation)

def delete_lst_word(fname, exl = []):
    exl = set(exl)
    try:
        with open(fname, "r", encoding = "utf-8") as f:
            lines = [x for x in re.sub("\r", "", f.read(), flags = re.MULTILINE).split("\n") if x not in exl]
        with open(fname, "w") as f:
            f.write("\n".join(lines))
    except BaseException as err:
        print(fname, err)

dic_bp = None

def append_lst_words(fname, lst_words=[]):
    try:
        with open(fname, "r", encoding="utf-8") as f_r:
            ret = set(f_r.read().splitlines())
            lst_dct = set(word.lower().split(': ')[-1] for word in ret)

        with open(fname + ".bak", "w", encoding="utf-8") as f_w:
            f_w.write('\n'.join(lst_dct))

        to_write = set(lst_words).union(lst_dct)
        with open(fname, "w", encoding="utf-8") as f_w:
            f_w.write('\n'.join(to_write))

    except BaseException as err:
        print(fname, err)

class Socket:
    def __init__(self, link, DEBUG = False):
        self.DEBUG = DEBUG
        self.connected = False
        self.connectedAt = None
        self._type = ""
        self.room = None
        self.nickname = None
        self.userToken = None
        self._callbacks = {}
        self._topCallback = None
        self.link = link
        print("class socket: " + link + "/socket.io/?EIO=4&transport=websocket")
        self.ws = websocket.WebSocketApp(link + "/socket.io/?EIO=4&transport=websocket",
            on_message = lambda *x: self.on_message(*x),
            on_error = lambda *x: self.on_error(*x),
        )
        self.ws.on_open = lambda *x: self.on_open(*x)
        self.socketThread = threading.Thread(target = self.ws.run_forever)
        # self.socketThread.daemon = True
        self.socketThread.start()

    def close(self):
        self.ws.close()

    def on_message(self, ws, message):
        if self.DEBUG:
            print("↓", message)

        if message[:2] == "42": # regular packet
            data = json.loads(message[2:])
            type = data.pop(0)
            return self.dispatch(type, data)

        if message == "2": # ping
            return self._send("3")

        if message[:1] == "0": # connection init
            data = json.loads(message[1:])
            return self._send("40")

        if message[:2] == "40": # connected
            self.connected = True
            self.connectedAt = datetime.now()
            return self.dispatch("connect")

        if message[:3] == "430": # sync packet
            if self._topCallback != None:
                data = json.loads(message[3:])
                callback = self._topCallback
                self._topCallback = None
                return callback(data)

        if message[:2] == "41": # disconnection
            if self.room in roomCodesConnected:
                app.decoBan(self.room)
            if self.DEBUG:
                print(u"Disconnected from room %s (auth fail, banned or already connected)" % (self.room))
            return self.close()

    def on_error(self, ws, error):
        # got disconnected normally, the sub thread crashes
        if str(error) == "'NoneType' object has no attribute 'connected'":
            return False
        try:
            raise error
        except Exception as e:
            print(traceback.format_exc())

    def on_close(self, ws):
        self.connected = False
        self.dispatch("disconnect")
        if self.DEBUG:
            print("### closed ###")

    def on_open(self, ws):
        if self.DEBUG:
            print("### connected ###")

    def _send(self, msg):
        if self.DEBUG:
            print("↑", msg)
        self.ws.send(msg)

    def emit0(self, callback, *args):
        self._topCallback = callback
        self._send("420" + json.dumps(args))

    def emit(self, *args):
        self._send("42" + json.dumps(args))

    def on(self, type, callback):
        callbacks = self._callbacks.get(type, None)
        if callbacks == None:
            self._callbacks[type] = [callback]
        else:
            callbacks.append(callback)
        return self

    def dispatch(self, type, data = None):
        callbacks = self._callbacks.get(type, [])
        if len(callbacks) == 0:
            if self.DEBUG:
                print("No callback for event", type)
                print("Data received:", data)
        for callback in callbacks:
            callback(data)

    def joinRoom(self, room, nickname, userToken, callback):
        self._type = "Room"
        self.room = room
        self.nickname = nickname
        self.userToken = userToken
        self.emit0(callback, "joinRoom", {
            "roomCode": room,
            "userToken": userToken,
            "nickname": nickname,
            "token":"03AFcWeA7p55MDmA-MmY0vIfxo_aSjv28nHzJ2Xyu6QdvoZNDDYm6PSaYwn41Zsb9pILdU9wXzVa4SZeO5vVNm2cR855DssJSCFBou_eSR0IhSMF1jTAisUKiOrTxVqXlIRQzvzmd8Zbg-2bqULm2T6e1-E2KFB1qLHYfIp7LzdJzqeOf1uzObYCq7EfeayVzPHCEQsMXMonr2GSRL0OYf10zP_q5raCqjO0VSPxs1GXuSwQvWRl7d3VEjHZv4x-OH1-z0m3ajZ-uPhPggsN6n7NSJflESJMVV0UbTGUCunibwo_LNe6LyHyxYLYGTr2eS2GgDKemsNnoOxIVXSfE2z9_T92RqKtcXQi6WgnFcAra8kSmnIwFpk3JpG4wJ7mspeUh4W9u_n4913BEp8UzIoJtvfLdRD2bdQckfrJtNFOldso2NhfCcNgwK2Xkv9iAlEPkkPtxLPwWF41EMdIa5QqXgVV09mCxm0wcNJQ7yzmrKBcm1WR_GpE_Q-L176iVqfn57CrB3x6ort_1y6ln2XFNHecyjm-zx9dOow28YVi86XeIhUTMAkHBoxsdr6YrB1liIPtVdaWlGr00WezyBDiaorNt2DkbLC-fEl7u8pNeB1VcbOfALip0G1p88b5pIp9Z6TeQTouBRY6i8Q3e6oxEbPvdKs-wWHVFE-3WF2cz3qm13I0xeAB7AlwfG1DC1pNl69JYSlmEG_Iaku16Tw8bJO9UXWz6XS6DQMyH07gPegCsD6wJfLyXOIpgPzRne0mbuHUoMqKYv7CGtJSpUDng7C-2OeYu4fqMc05claXNm-l_W3dYr01A"
,
            #"picture": "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",
            "language": "fr"
        })

    def joinGame(self, room, nickname, userToken):
        self._type = "Game"
        self.room = room
        self.nickname = nickname
        self.userToken = userToken
        self.emit("joinGame", "bombparty", room, userToken, True)

    def __repr__(self):
        if self.connected:
            return u"<%sSocket [%s] - %s (%s) -> At %s>" % (self._type, self.room, self.nickname, self.userToken, str(self.connectedAt))
        else:
            return u"<%sSocket [%s] - %s (%s) -> Disconnected>" % (self._type, self.room, self.nickname, self.userToken)

class Bot:
    def __init__(self, room, nickname, debug = False, userToken = None):
        global indexBot
        self.nbRoom = 0
        self.id = indexBot
        self.DEBUG = debug
        self.room = room
        self.nickname = nickname
        self.currentPlayer = None
        self.chatCommand = False
        self.data = None
        self.printChat = False
        self.birthday = False
        self.suicid = False
        self.gameStartedAt = None
        self.gameEndedAt = None
        self.myPeerId = None
        self.helpOther = True
        self.help = False
        self.birdBot = False
        self.aiChat = False
        self.needWord = False
        self.wordSet = ""
        self.mode = "human"
        self.players = []
        self.newWord = 0
        self.maxQueue = 25
        self.currentWordIndice = 0
        self.autoJoin = True
        self.wordUsed = []
        self.currentPrompt = ""
        self.currentDic = dic_bp
        self.word = ""
        self.wordFound = ""
        self.tchatMessage = queue.Queue(self.maxQueue)
        self.suicidList = ["meurs", "perd", "suicide"]
        self.quitList = ["quitte", "room"]
        self.joinList = ["vient", "joue", "rejoin"]
        self.leaveList = ["quitte","pars", "partir", "part", "barre toi", "degage","déguerpi"]
        self.AIOnList = ["parle", "active toi", "repond"]
        self.AIOffList = ["parle plus", "parle pas", "desactive toi", "repond plus"]
        self.birthdayOnList = ["souhaite l'anniversaire", "anniv", "anniversaire", "joyeux anniversaire"]
        self.birthdayOffList = ["desactive l'anniversaire", "arrete les ballons", "arrete l'anniversaire", "desactive le mode anniversaire"]
        self.psHumanList = ["mode humain", "human", "human mode", "triche pas", "arrete de tricher"]
        self.psbotList = ["mode instant", "mode bot", "instant mode","bot mode"]

        self.noFoundList =["euhhh jsp","helpp mee", "ckoi ca ????", "aide moi= 10€ paypal", "wshhhhh jsp frr"]
        self.users = []
        self.usersByPeerId = {}
        self.players = []
        self.worldList = []
        self.playersByPeerId = {}
        self.userToken = userToken if userToken != None else self.generateToken()   

        if dic_bp != None:
            r = requests.post("https://jklm.fun/api/joinRoom", json.dumps({"roomCode": self.room, "userToken": self.userToken}), headers = {"Content-Type": "application/json"})
            if r.status_code == 200:
                j = json.loads(r.content)
                if j.get("errorCode", "") == "noSuchRoom":
                    return print(u"Room %s doesn't exist" % (self.room))         
                self.gameUrl = j["url"]
                print("class Bot: " + self.gameUrl.replace("https", "wss"))
                self.roomSocket = Socket(self.gameUrl.replace("https", "wss"), self.DEBUG)
                self.roomSocket.on("connect", self.joinRoom)
                self.roomSocket.on("disconnect", lambda _: print(u"Lost room connection as %s to %s" % (self.nickname, self.room)))
                self.roomSocket.on("setPlayerCount", self.setPlayerCount)
                self.roomSocket.on("chat", self.chat)   

                #Add bot in list
                roomCodesConnected.append(self.room)
                listBots.append(self)
                indexBot = indexBot + 1
            else:
                print(u"Error connecting to room %s" % (self.room))
        else:
            print("Aucun dictionnaire selectionner")

        

    def joinRoom(self, data):
        self.roomSocket.joinRoom(self.room, self.nickname, self.userToken, self.joinedRoom)
        print("join room: " + self.gameUrl.replace("https", "wss") )
        self.gameSocket = Socket(self.gameUrl.replace("https", "wss"), self.DEBUG)
        self.gameSocket.on("authError", lambda _: print(u"Game %s doesn't exist" % (self.room)))
        self.gameSocket.on("connect", lambda _: self.gameSocket.joinGame(self.room, self.nickname, self.userToken))
        self.gameSocket.on("kicked", self.kicked)
        self.gameSocket.on("disconnect", lambda _: print(u"Lost game connection as %s to %s" % (self.nickname, self.room)))
        self.gameSocket.on("setup", self.setup)
        self.gameSocket.on("setPlayerWord", self.setPlayerWord)
        self.gameSocket.on("correctWord", self.correctWord)
        self.gameSocket.on("failWord", self.failWord)
        self.gameSocket.on("livesLost", self.livesLost)
        self.gameSocket.on("setMilestone", self.setMilestone)
        self.gameSocket.on("addPlayer", self.addPlayer)
        self.gameSocket.on("removePlayer", self.removePlayer)
        self.gameSocket.on("setStartTime", self.setStartTime)
        self.gameSocket.on("nextTurn", self.nextTurn)  

    def generateToken(self):
        return "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-") for i in range(16))

    def typing(self, min1, min2, max1, max2, word, sendIt):
        typeWord = ""
        for char in word:
            typeWord = typeWord + char
            self.gameSocket.emit("setWord", typeWord, False);  
            if (len(word) > 6):
                sleep(random.uniform(min1,max1))
            else:
                sleep(random.uniform(min2,max2))
            self.currentWordIndice = self.currentWordIndice + 1
        self.currentWordIndice = 0
        if (sendIt):
            self.gameSocket.emit("setWord", word, True);
        self.word = ""

    def answerWhenNoWord(self):
         sleep(random.uniform(1.00,1.500))
         answer = self.noFoundList[random.randint(0, len(self.noFoundList)-1)]
         self.typing(0.05, 0.03, 0.15, 0.12, answer, True)

    def checkMode(self):

        if self.birthday:
            try:
                for user in self.users:
                    self.gameSocket.emit("setWord", "🎂 " + user["nickname"], True);  
                    if len(self.worldList) > 0:
                        sleep(random.uniform(0.001,0.005))
                        wordFound = max(self.worldList, key=len)
                        #wordFound = self.worldList[random.randint(0, len(self.worldList)-1)]
                        self.gameSocket.emit("setWord", wordFound, True); 
                    else:
                        self.gameSocket.emit("setWord", "euhhhh jsp", True); 
                        self.needWord = True
            except:
                print('Error birthday')

        if self.mode == "human":
            numRandom = random.randint(0,100)
            if len(self.worldList) > 0: #Mot trouvé
                sleep(random.uniform(0.680,1.200))
                self.needWord = False
                self.wordFound = self.worldList[random.randint(0, len(self.worldList)-1)]
                self.currentWordIndice = 0
                if (numRandom > 15): #Sans erreur
                    self.typing(0.05, 0.03, 0.15, 0.10, self.wordFound, True)
                elif (numRandom <= 15 and numRandom > 8): #Erreur 1
                    self.wrongWord1(self.wordFound)      
                elif (numRandom <= 8): #Erreur 2
                    self.wrongWord2(self.wordFound)
            else: #Aucun mot trouvé
                self.needWord = True
                if self.birdBot: 
                    sleep(random.uniform(0.5,1))
                    self.roomSocket.emit("chat", "/c")
                else:
                    self.answerWhenNoWord()

        elif self.mode == "instant":
            if len(self.worldList) > 0:
                sleep(random.uniform(0.001,0.005))
                wordFound = max(self.worldList, key=len)
                #wordFound = self.worldList[random.randint(0, len(self.worldList)-1)]
                self.gameSocket.emit("setWord", wordFound, True); 
            else:
                self.gameSocket.emit("setWord", "euhhhh jsp", True); 
                self.needWord = True


    def joinedRoom(self, data):
        self.roomSocket.emit0(self.gotUsers, "getChatterProfiles")
        print(u"Connected as %s to room %s" % (self.nickname, self.room))

    def wrongWord1(self, word):
        indiceRandomLettre = random.randint(0, len(word))
        randomLetter = random.choice(string.ascii_letters)
        wrongWord = word[:indiceRandomLettre] + randomLetter + word[indiceRandomLettre:]
        self.typing(0.05, 0.03, 0.15, 0.10, wrongWord, False)
        self.gameSocket.emit("setWord", wrongWord, True);  
        sleep(random.uniform(0.250,0.400))
        self.typing(0.04, 0.03, 0.12, 0.10, word, True) 
    
    def wrongWord2(self, word):
        indiceRandomLettre = random.randint(0, len(word)-3)
        randomSuite = random.randint(1,3)
        indiceFinMauvaisMot = indiceRandomLettre + randomSuite
        randomLetter = random.choice(string.ascii_letters)
        indice = 0

        wrongWord = word[:indiceRandomLettre] + randomLetter + word[indiceRandomLettre:indiceFinMauvaisMot]
        midWord = word[:indiceRandomLettre]
        endWord = word[indiceRandomLettre:len(word)]
        self.typing(0.05, 0.03, 0.15, 0.10, wrongWord, False)
        for i in range(randomSuite+1):
            indice = indiceFinMauvaisMot - i
            self.gameSocket.emit("setWord", wrongWord[:indice], False); 
            sleep(random.uniform(0.100,0.250))
        for i in endWord:
            midWord = midWord + i
            self.gameSocket.emit("setWord", midWord, False); 
            sleep(random.uniform(0.03,0.100))
        self.gameSocket.emit("setWord", word, True); 
       
    def helpOthers(self):
        self.helpOther = True
        while(self.helpOther):
            self.worldList = []
            for i in range(40):
                if self.helpOther:
                    sleep(0.1)
                else:
                    break
            if self.helpOther == True:
                for line in self.currentDic:
                    if self.currentPrompt in line:
                        if line not in self.wordUsed:
                            self.worldList.append(line)
                if len(self.worldList) > 0: #Mot trouvé
                    self.wordFound = min(self.worldList, key=len) #Pour trouver le plus ptit mot
                    self.roomSocket.emit("chat",self.wordFound)
            self.helpOther = False

    def setup(self, data):
        if self.autoJoin:
            if self.mode == "human":
                sleep(random.uniform(1.000,2.500))
            self.gameSocket.emit("joinRound")     
        self.milestone = data[0]["milestone"]
        self.players = data[0]["players"]
        self.myPeerId = data[0]["selfPeerId"]
        if self.milestone["name"] != "seating":
            self.currentPrompt = self.milestone["syllable"].upper()
            self.gameStartedAt = datetime.fromtimestamp(self.milestone["startTime"] / 1000)
            self.playersByPeerId = {}
            for player in self.players:
                self.playersByPeerId[player["profile"]["peerId"]] = player
            states = self.milestone["playerStatesByPeerId"]
            boucleState = 0
            for peerId in states:
                self.players[boucleState] = str(self.playersByPeerId[int(peerId)]["profile"]["nickname"])
                self.playersByPeerId[int(peerId)]["lives"] = states[peerId]["lives"]
                self.playersByPeerId[int(peerId)]["word"] = states[peerId]["word"]
                self.playersByPeerId[int(peerId)]["wasWordValidated"] = states[peerId]["wasWordValidated"]
                self.playersByPeerId[int(peerId)]["bonusLetters"] = states[peerId]["bonusLetters"]
                boucleState = boucleState +1

    def setPlayerCount(self, data):
        self.roomSocket.emit0(self.gotUsers, "getChatterProfiles")

    def gotUsers(self, data):
        self.users = data[0]
        self.usersByPeerId = {}
        for user in self.users:
            self.usersByPeerId[user["peerId"]] = user

    def chat(self, data):
        chatter = data[0]
        msg = data[1]

        if self.tchatMessage.full():
            self.tchatMessage.get()

        self.tchatMessage.put(chatter.get("nickname", "?") + ": " + msg)
        app.changeTchat()

        global humeur
                    
        print(msg.lower())
        if msg.lower() == "test":
            print("oui")
            self.roomSocket.emit("happyBirthday",0)
        if(chatter["nickname"] == "tthorino"):
            if msg.lower() == "chibrax":
                self.roomSocket.emit("chat", "⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⢉⢉⠉⠉⠻⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⠟⠠⡰⣕⣗⣷⣧⣀⣅⠘⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⠃⣠⣳⣟⣿⣿⣷⣿⡿⣜⠄⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⡿⠁⠄⣳⢷⣿⣿⣿⣿⡿⣝⠖⠄⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⠃⠄⢢⡹⣿⢷⣯⢿⢷⡫⣗⠍⢰⣿⣿⣿⣿⣿ ⣿⣿⣿⡏⢀⢄⠤⣁⠋⠿⣗⣟⡯⡏⢎⠁⢸⣿⣿⣿⣿⣿ ⣿⣿⣿⠄⢔⢕⣯⣿⣿⡲⡤⡄⡤⠄⡀⢠⣿⣿⣿⣿⣿⣿ ⣿⣿⠇⠠⡳⣯⣿⣿⣾⢵⣫⢎⢎⠆⢀⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⠄⢨⣫⣿⣿⡿⣿⣻⢎⡗⡕⡅⢸⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⠄⢜⢾⣾⣿⣿⣟⣗⢯⡪⡳⡀⢸⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⠄⢸⢽⣿⣷⣿⣻⡮⡧⡳⡱⡁⢸⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⡄⢨⣻⣽⣿⣟⣿⣞⣗⡽⡸⡐⢸⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⡇⢀⢗⣿⣿⣿⣿⡿⣞⡵⡣⣊⢸⣿⣿⣿⣿⣿⣿⣿")
        
        if self.chatCommand:
            if(chatter["nickname"] == "Ayaya"):         
                if msg.lower() in self.quitList or msg.lower() == "$stop":
                    self.disconnect()
                    exit(0)
                elif msg.lower() in self.joinList or msg.lower() == "$join":
                    self.autoJoin = True
                    self.joinRound()
                elif msg.lower() in self.leaveList or msg.lower() == "$leave":
                    self.autoJoin = False
                    self.leaveRound()
                elif msg.lower() == "$ps human":
                    self.mode = "human"
                    app.getSwitchStateCurrentBot()
                    app.updateSwitchState(app.modeSwitch)
                elif msg.lower() == "$ps instant":
                    self.mode = "instant"
                    app.getSwitchStateCurrentBot()
                    app.updateSwitchState(app.modeSwitch)
                elif msg.lower() == "$birthday on":
                    self.birthday = True
                    app.getSwitchStateCurrentBot()
                    app.updateSwitchState(app.birthdaySwitch)
                elif msg.lower() == "$birthday off":
                    self.birthday = False
                    app.getSwitchStateCurrentBot()
                    app.updateSwitchState(app.birthdaySwitch)
                elif msg.lower() == "$autojoin on":
                    self.autoJoin = True
                    app.getSwitchStateCurrentBot()
                    app.updateSwitchState(app.autojoinSwitch)
                elif msg.lower() == "$autojoin off":
                    self.autoJoin = False
                    app.getSwitchStateCurrentBot()
                    app.updateSwitchState(app.autojoinSwitch)
                elif msg.lower() in self.suicidList or msg.lower() == "$suicid on":
                    self.suicid = True
                    app.getSwitchStateCurrentBot()
                    app.updateSwitchState(app.suicidSwitch)
                elif msg.lower() == "$suicid off":
                    self.suicid = False
                    app.getSwitchStateCurrentBot()
                    app.updateSwitchState(app.suicidSwitch)
                elif msg.lower() == "$birdbot on":
                    self.birdBot = True
                elif msg.lower() == "$birdbot off":
                    self.birdBot = False
                elif msg.lower() == "$ai on" and openai.api_key != "":
                    self.aiChat = True
                    app.getSwitchStateCurrentBot()
                    app.updateSwitchState(app.AISwitch)
                elif msg.lower() == "$ai off":
                    self.aiChat = False
                    app.getSwitchStateCurrentBot()
                    app.updateSwitchState(app.AISwitch)
                elif msg.lower() == "$help on":
                    self.help = True
                    app.getSwitchStateCurrentBot()
                    app.updateSwitchState(app.aideSwitch)
                elif msg.lower() == "$help off":
                    self.help = False
                    app.getSwitchStateCurrentBot()
                    app.updateSwitchState(app.aideSwitch)

            if msg == "$newWords":
                self.roomSocket.emit("chat", "J'ai appris " + str(self.newWord) + " nouveaux mots")

            for element in self.joinList:
                if element in msg.lower() and "ayaya" in msg.lower():
                    self.joinRound()
                    self.autoJoin = True

            for element in self.leaveList:
                if element in msg.lower() and "ayaya" in msg.lower():
                    self.leaveRound()
                    self.autoJoin = False

            for element in self.suicidList:
                if element in msg.lower() and "ayaya" in msg.lower():
                    self.suicid = True

            for element in self.AIOnList:
                if element in msg.lower() and "ayaya" in msg.lower():
                    self.aiChat = True

            for element in self.AIOffList:
                if element in msg.lower() and "ayaya" in msg.lower():
                    self.aiChat = False

            for element in self.birthdayOnList:
                if element in msg.lower() and "ayaya" in msg.lower():
                    self.birthday = True

            for element in self.birthdayOffList:
                if element in msg.lower() and "ayaya" in msg.lower():
                    self.birthday = False

            for element in self.psHumanList:
                if element in msg.lower() and "ayaya" in msg.lower():
                    self.mode = "human"

            for element in self.psbotList:
                if element in msg.lower() and "ayaya" in msg.lower():
                    self.mode = "instant"

            if msg.lower() == "$humor sarcastique":
                humeur = "sarcastique"
            elif msg.lower() == "$humor raciste":
                humeur = "raciste"
            elif msg.lower() == "$humor gothique":
                humeur = "gothique"
            elif msg.lower() == "$humor enfant":
                humeur = "enfant"
            elif msg.lower() == "$humor pervers":
                humeur = "pervers"
            elif msg.lower() == "$humor racaille":
                humeur = "racaille"
            elif msg.lower() == "$humor fruh":
                humeur = "fruh"
            elif msg.lower() == "$humor oknn":
                humeur = "oknn"
            elif msg.lower() == "$humor gentleman":
                humeur = "gentleman"
            elif msg.lower() == "$get humor":
                self.roomSocket.emit("chat",humeur)
            elif msg.lower() == "$humor":
                self.roomSocket.emit("chat","Pour me définir une nouvelle personnalité '$humor laPersonnalité', pour l'instant j'ai sarcastique, raciste, gothique, enfant, pervers et racaille")

        if self.aiChat:
            if(chatter["nickname"] != self.nickname):
                print(self.nickname)
                if(self.nickname.lower() in msg.lower()):
                    reponse = getAIResponse(chatter.get("nickname", "?") + ": " +msg, chatter.get("nickname", "?"), self.nickname)
                    if reponse != "":
                        reponse = str(reponse).replace('\t', '')
                        reponse = str(reponse).replace('\n', ' ')
                        self.roomSocket.emit("chat",reponse)

        if self.needWord:
            wordMsg =""
            if self.currentPrompt.lower() in msg.lower():
                listWord = msg.split()
                for word in listWord:
                    if word not in self.wordUsed:
                        if self.currentPrompt.lower() in word.lower():
                            word = word.replace(",","")
                            wordMsg = word
                emptyWord=""
                for c in wordMsg:
                    emptyWord = emptyWord + c
                    self.gameSocket.emit("setWord", emptyWord, False);  
                    sleep(random.uniform(0.005,0.200))
                self.gameSocket.emit("setWord", emptyWord, True);  


    def toggleChat(self, value = None):
        if value == None:
            self.printChat = not self.printChat
        else:
            self.printChat = value

    def setPlayerWord(self, data):
        self.wordSet = data[1]
        player = self.playersByPeerId.get(data[0], None)
        if player != None:
            player["word"] = data[1].upper()

    def correctWord(self, data):
        self.helpOther = False
        peerId = data[0].get("playerPeerId")
        bonusLetters = data[0].get("bonusLetters")
        player = self.playersByPeerId.get(peerId, None)
        if player != None:
            try:
                if len(bonusLetters) > len(player["bonusLetters"]):
                    # Gained an extra life
                    pass
            except:
                print("pas de bonus de vie")
            player["bonusLetters"] = bonusLetters
            #print(u"%s: [%s] %s" % (player["profile"]["nickname"], self.currentPrompt, player["word"]))
            self.wordUsed.append(player["word"].lower())
            if player["word"].lower() not in dic_bp:
                word = player["word"].lower()
                char = ["1","2","3","4","5","6","7","8","9","0","*","$","^","ù","!",":",";",",","&","é",'"',"(","è","_",")","="]
                for c in char:
                    word = word.replace(c,"")
                append_lst_words(dicLocation, [word])
                self.newWord = self.newWord +1
            if self.needWord:
                self.roomSocket.emit("chat", "merci")
                self.needWord = False

    def failWord(self, data):
        failResponse = data[1]
        if failResponse == "notInDictionary":
            if self.wordSet in dic_bp:
                delete_lst_word(dicLocation, [self.wordSet])
                print(self.wordSet + " was deleted from dic")
        elif failResponse == "alreadyUsed":
            self.wordUsed.append(self.wordSet)
        # print("failWord", data)
        pass

    def livesLost(self, data):
        peerId = data[0]
        player = self.playersByPeerId.get(peerId, None)
        if player != None:
            player["lives"] = data[1]
            self.needWord = False
            if player["lives"] < 1:
                # Player is dead
                pass

    def foundSyllable(self, syllable):
        self.worldList = []
        for line in self.currentDic:
            if syllable in line:
                if line not in self.wordUsed:
                    self.worldList.append(line)
        self.checkMode()   
        pass

    def setMilestone(self, data):
        milestone = data[0]      
        if milestone["name"] == "round":
            # Start game
            self.helpOther = True
            self.milestone = milestone
            self.gameStartedAt = datetime.now()
            self.gameEndedAt = None
            self.currentPrompt = data[0]["syllable"].lower()
            states = self.milestone["playerStatesByPeerId"]           
            try:
                boucleState = 0
                for peerId in states:
                    self.players[boucleState] = str(self.playersByPeerId[int(peerId)]["profile"]["nickname"])
                    self.playersByPeerId[int(peerId)]["lives"] = states[peerId]["lives"]
                    self.playersByPeerId[int(peerId)]["word"] = states[peerId]["word"]
                    self.playersByPeerId[int(peerId)]["wasWordValidated"] = states[peerId]["wasWordValidated"]
                    self.playersByPeerId[int(peerId)]["bonusLetters"] = states[peerId]["bonusLetters"]
                    boucleState = boucleState +1
            except:
                print("erreur")
            if data[0]["currentPlayerPeerId"] == self.myPeerId:          
                self.foundSyllable(data[0]["syllable"].lower())
        else:
            # End game
            self.gameEndedAt = datetime.now()
            self.players = []
            self.playersByPeerId = {}
            self.wordUsed = []
            self.suicid = False
            if self.autoJoin:
                sleep(random.uniform(1.000,2.500))
                self.gameSocket.emit("joinRound")
        pass

    def addPlayer(self, data):
        player = data[0]
        self.players.append(player)
        self.playersByPeerId[player["profile"]["peerId"]] = player

    def removePlayer(self, data):
        player = self.playersByPeerId.get(data[0], None)
        if player != None:
            del self.playersByPeerId[data[0]]
            self.players.remove(player)

    def setStartTime(self, data):
        # print("setStartTime", data)
        pass

    def nextTurn(self, data):  
        self.helpOther = False
        self.currentPrompt = data[1].lower()
        if self.suicid:
            self.gameSocket.emit("setWord", "💥", True);
        else:
            self.currentPrompt = data[1].lower()
            if data[0] == self.myPeerId: 
                #my turn 
                self.foundSyllable(data[1].lower()) 
            else:         
                if (self.help):
                    threadHelpingOther = threading.Thread(target=self.helpOthers)
                    threadHelpingOther.start()

    def joinRound(self):
        self.gameSocket.emit("joinRound")

    def leaveRound(self):
        self.gameSocket.emit("leaveRound")

    def kicked(self, data):
        print(u"kicked from room %s for reason: %s" % (self.room, str(data[0])))

    def disconnect(self):
        self.roomSocket.emit("forceQuit")
        self.gameSocket.close()
        self.roomSocket.close()

    def __repr__(self):
        return u"<Bot [%s] - %s (%s)>" % (self.room, self.nickname, self.userToken)


# websocket.enableTrace(True)
def start_bot(room, name, debug, number):
    if room != "":
        for i in range(number):
            b = Bot(room, name, debug)
            b.toggleChat()

#for room in listRoomCodes:
#    start_bot(room, "Happy birthday Oknn", False, 1)
#    sleep(3)
#print("all bot are connected")

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def changeConnectedText(self):
        if len(listBots) > 1:
            self.labelConnected['text'] = str(len(listBots)) + " bots connectés"
        elif len(listBots) == 1:
            self.labelConnected['text'] = str(len(listBots)) + " bot connecté"
        else:
           self.labelConnected['text'] = "1 bot connecté"

    def __init__(self):
        super().__init__()

        # Load config file
        nickname = config_txt[0]
        dic = config_txt[1]
        apikey = config_txt[2]
        version = config_txt[3]
        beforeNickname, sepNickname, afterNickname = nickname.partition('nickname:')
        self.configNickname = afterNickname
        beforeDic, sepDic, afterDic = dic.partition('dic:')
        self.configDic = afterDic
        global dicLocation
        dicLocation = self.configDic
        beforeAPIKey, sepAPIKey, afterAPIKey = apikey.partition('api_key:')
        self.configAPIKey = afterAPIKey

        #Other parameters
        self.changedBot = False
        self.currentBotSelected = None
        self.textSwitchMode = tkinter.StringVar()
        self.textSwitchMode.set("Humain")
        self.title("BombParty Bot V2")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed   

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(6, minsize=42)
        self.frame_left.grid_rowconfigure(7, minsize=42) 
        self.frame_left.grid_rowconfigure(8, minsize=42) 
        self.frame_left.grid_rowconfigure(9, minsize=42)
        self.frame_left.grid_rowconfigure(10, minsize=42)
        self.frame_left.grid_rowconfigure(11, minsize=42)

        self.labelConnected = customtkinter.CTkLabel(master=self.frame_left,
                                              text="1 bot connecté",
                                              font=("Roboto Medium", -16))  # font name and size in px
        self.labelConnected.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

        self.room = customtkinter.CTkEntry(master=self.frame_left,
                                            width=120,
                                            placeholder_text="Room XXXX")
        self.room.grid(row=2, column=0, columnspan=2, pady=0, padx=10, sticky="we")

        self.nickname = customtkinter.CTkEntry(master=self.frame_left,
                                            width=120)
        self.nickname.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="we")
        self.nickname.insert(END, self.configNickname)

        self.numberOfBots = customtkinter.CTkSlider(master=self.frame_left,
                                                from_=1,
                                                to=12,
                                                number_of_steps=11,
                                                command=self.updateSlider)
        self.numberOfBots.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="we")



        self.rejoindre = customtkinter.CTkButton(master=self.frame_left,
                                                text="Rejoindre",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=lambda: [start_bot(self.room.get(), self.nickname.get(), False, int(self.numberOfBots.get())), self.updateValue()])
        self.rejoindre.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

        self.deconnecter = customtkinter.CTkButton(master=self.frame_left,
                                                text="Deconnecter",
                                                fg_color=("#80404b", "#d43550"),  # <- custom tuple-color
                                                command=lambda: [start_bot(self.room.get(), self.nickname.get(), False, int(self.numberOfBots.get())), self.deconnexion()])
        self.deconnecter.grid(row=12, column=0, columnspan=2, pady=10, padx=10)


        # ============ frame_right ============

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=10, padx=20, sticky="nsew")

        # ============ Chat / config ============
        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        self.tchat = Text(self.frame_info,height=15,width=41,bd =0, bg ="#383838", fg="#FFFFFF", font=("Arial", 10))
        self.tchat.place(x=10, y=0)
        self.tchat.configure(cursor="arrow", state="disabled")
        self.entryMsg = customtkinter.CTkEntry(master=self.frame_right,
                                                     width=320,
                                                     placeholder_text="Envoyer un message...")
        self.entryMsg.grid(row=4, column=0,columnspan = 2,padx=20, sticky="w")
        self.entryMsg.bind("<Return>", self.on_enter_pressed)
        self.labelConfig = customtkinter.CTkLabel(self.frame_right,
                                                        text="-----CONFIGURATIONS-----",
                                                        font=("Arial", 20))
        self.labelConfig.grid(row=5, column=0, columnspan=2, padx=10, sticky="S")


        self.entryDicFile = customtkinter.CTkEntry(master=self.frame_right,
                                                   width=280,
                                                   placeholder_text="Aucun dictionnaire sélectionner")
        self.entryDicFile.grid(row=6, column=0,sticky="e")
        self.openDic = customtkinter.CTkButton(master=self.frame_right,
                                               text="🔍 ",
                                               width=20,
                                               command = self.getDicFile)
        self.openDic.grid(row=6, column=1, padx=5,sticky="w")


        self.entryAPI = customtkinter.CTkEntry(master=self.frame_right,
                                               placeholder_text="Clée d'API OpenAI",
                                               width=280)
        self.entryAPI.grid(row=7, column=0,sticky="e")
        self.okAPI = customtkinter.CTkButton(master=self.frame_right,
                                               text="OK",
                                               width=20,
                                               command = self.getOpenAIKey)
        self.okAPI.grid(row=7, column=1, padx=5,sticky="w")

        

        # ============ frame_right ============

        self.var_radio = tkinter.IntVar(value=0)

        self.labelOption = customtkinter.CTkLabel(self.frame_right,
                                                        text="OPTIONS",
                                                        font=("Arial", 20))
        self.labelOption.grid(row=0, column=2,pady=10, sticky = "w")

        self.autojoinSwitch = customtkinter.CTkSwitch(self.frame_right,
                                                        text="Autojoin",
                                                        command= lambda: self.updateSwitchState(self.autojoinSwitch))
        self.autojoinSwitch.grid(row=1, column=2, columnspan=1, padx=10, sticky="w")

        self.modeSwitch = customtkinter.CTkSwitch(self.frame_right,
                                                        textvariable=self.textSwitchMode,
                                                        command= lambda: self.updateSwitchState(self.modeSwitch))
        self.modeSwitch.grid(row=2, column=2, columnspan=1, padx=10, sticky="w")

        self.birthdaySwitch = customtkinter.CTkSwitch(self.frame_right,
                                                        text="Anniversaire",
                                                        command= lambda: self.updateSwitchState(self.birthdaySwitch))
        self.birthdaySwitch.grid(row=3, column=2, columnspan=1, padx=10, sticky="w")

        self.suicidSwitch = customtkinter.CTkSwitch(self.frame_right,
                                                        text="Suicide",
                                                        command= lambda: self.updateSwitchState(self.suicidSwitch))
        self.suicidSwitch.grid(row=4, column=2, columnspan=1, pady=15, padx=10, sticky="w")

        self.AISwitch = customtkinter.CTkSwitch(self.frame_right,
                                                        text="AI",
                                                        command= lambda: self.updateSwitchState(self.AISwitch))
        self.AISwitch.grid(row=5, column=2, columnspan=1, pady=15, padx=10, sticky="w")

        self.aideSwitch = customtkinter.CTkSwitch(self.frame_right,
                                                        text="Aide",
                                                        command= lambda: self.updateSwitchState(self.aideSwitch))
        self.aideSwitch.grid(row=6, column=2, columnspan=1, pady=15, padx=10, sticky="w")

        self.chatCommandSwitch = customtkinter.CTkSwitch(self.frame_right,
                                                        text="$ Commandes",
                                                        command= lambda: self.updateSwitchState(self.chatCommandSwitch))
        self.chatCommandSwitch.grid(row=7, column=2, columnspan=1, pady=15, padx=10, sticky="w")


        # set default values
        self.autojoinSwitch.configure(state="disabled")
        self.modeSwitch.configure(state="disabled")
        self.birthdaySwitch.configure(state="disabled")
        self.suicidSwitch.configure(state="disabled")
        self.AISwitch.configure(state="disabled")
        self.aideSwitch.configure(state="disabled")
        self.chatCommandSwitch.configure(state="disabled")
        self.deconnecter.configure(state="disabled")
        self.entryDicFile.configure(state="disabled", cursor="arrow")
        self.autojoinSwitch.deselect()
        self.numberOfBots.set(1.0)
        self.listRadioButtons = []
        self.entryMsg.configure(state=tkinter.DISABLED)
        self.loadDicFile()
        self.loadAPIKey()


    def loadAPIKey(self):
        if self.configAPIKey != "":
            openai.api_key = self.configAPIKey
            self.entryAPI.delete(0, END)
            self.entryAPI.insert(0,self.configAPIKey)


    def getOpenAIKey(self):
        if self.configAPIKey != self.entryAPI.get():
            config_txt[2] = "api_key:" + self.entryAPI.get()
            write_file(configFileLocation,config_txt)
        if self.currentBotSelected != None:
            openai.api_key = self.entryAPI.get()
            self.getSwitchStateCurrentBot()
            self.AISwitch.configure(state="normal")
            self.updateSwitchState(self.AISwitch)   
            
                

    def loadDicFile(self):
        if path.exists(self.configDic):
            self.entryDicFile.configure(state="normal")
            self.entryDicFile.delete(0,END)
            self.entryDicFile.insert(0,os.path.basename(self.configDic))
            self.entryDicFile.configure(state="disabled", cursor="arrow")
            global dic_bp
            dic_bp = read_lst_words(self.configDic, [])

    def getDicFile(self):
            self.filename = askopenfilename()
            self.entryDicFile.configure(state="normal")
            self.entryDicFile.delete(0,END)
            self.entryDicFile.insert(0,os.path.basename(self.filename))
            self.entryDicFile.configure(state="disabled", cursor="arrow")
            global dic_bp
            global dicLocation
            dicLocation = self.filename
            dic_bp = read_lst_words(self.filename, [])

            if self.configDic != self.filename:
                config_txt[1] = "dic:" + self.filename
                write_file(configFileLocation,config_txt)


    def on_enter_pressed(self, event):
        msgToAppend = self.entryMsg.get()
        for bot in listBots:
            if bot.id == self.var_radio.get():
                bot.roomSocket.emit("chat",msgToAppend)
        self.entryMsg.delete(0, END)
        self.entryMsg.insert(0,"")


    def getValueSlider(self):
        return str(self.currentSliderValue)

    def button_event(self):
        print("Button pressed")

    def on_closing(self, event=0):
        self.destroy()

    def updateSlider(self, event):
        if int(self.numberOfBots.get()) > 1:
            self.rejoindre.configure(text= "Rejoindre x" + str(int(self.numberOfBots.get())))
        else:
            self.rejoindre.configure(text= "Rejoindre")


    def decoBan(self, room):
        botToDelete = None
        for bot in listBots:
            if bot.room == room:
                botToDelete = bot
        roomCodesConnected.remove(botToDelete.room)
        botToDelete.disconnect()
        listBots.remove(botToDelete) 
        for radioBtn in self.listRadioButtons:            
            radioBtn.destroy()
        self.listRadioButtons = []
        self.updateValue()

    def deconnexion(self):
        botToDelete = None
        for bot in listBots:
            if bot.id == self.var_radio.get():
                botToDelete = bot
        roomCodesConnected.remove(botToDelete.room)
        botToDelete.disconnect()
        listBots.remove(botToDelete) 
        for radioBtn in self.listRadioButtons:            
            radioBtn.destroy()
        self.listRadioButtons = []
        self.updateValue()

    def updateTchat(self, listMsg):
        tchat = ""
        for msg in list(listMsg.queue):
            tchat = tchat + msg   + "\n\n"
        self.tchat.configure(cursor="arrow", state="normal")
        self.tchat.delete('1.0', END)
        self.tchat.insert(END,tchat+"\n")
        self.tchat.configure(cursor="arrow", state="disabled")
        self.tchat.see(tkinter.END)

    def changeTchat(self):
        for bot in listBots:
            if bot.id == self.var_radio.get():
                self.updateTchat(bot.tchatMessage)

    def getSwitchStateCurrentBot(self):
        
        for bot in listBots:
            if bot.id == self.var_radio.get():
                self.currentBotSelected = bot

        if self.currentBotSelected != None:
            self.changedBot = False
            self.autojoinSwitch.deselect()
            self.modeSwitch.deselect()
            self.birthdaySwitch.deselect()
            self.suicidSwitch.deselect()
            self.AISwitch.deselect()
            self.aideSwitch.deselect()
            self.chatCommandSwitch.deselect()
            if self.currentBotSelected.autoJoin:
                self.autojoinSwitch.select()
            if self.currentBotSelected.mode == "instant":
                self.modeSwitch.select()
            if self.currentBotSelected.birthday:
                self.birthdaySwitch.select()
            if self.currentBotSelected.suicid:
                self.suicidSwitch.select()
            if self.currentBotSelected.aiChat and openai.api_key != "":
                self.AISwitch.select()
            if self.currentBotSelected.help:
                self.aideSwitch.select()
            if self.currentBotSelected.chatCommand:
                self.chatCommandSwitch.select()

            self.changedBot = True

      
    def updateSwitchState(self, switch):    
        if self.changedBot:
            if len(listBots) > 0:
                if switch == self.autojoinSwitch:
                    if switch.get() == 1:
                        self.currentBotSelected.autoJoin = True                
                        if hasattr(self.currentBotSelected, 'gameSocket'):
                            self.currentBotSelected.gameSocket.emit("joinRound")
                    else:
                        self.currentBotSelected.autoJoin = False
                        if hasattr(self.currentBotSelected, 'gameSocket'):
                            self.currentBotSelected.leaveRound()
                elif switch == self.modeSwitch:
                    if switch.get() == 1:
                        self.currentBotSelected.mode = "instant"
                        self.textSwitchMode.set("Bot")
                    else:
                        self.currentBotSelected.mode = "human"
                        self.textSwitchMode.set("Humain")
                elif switch == self.birthdaySwitch:
                    if switch.get() == 1:
                        self.currentBotSelected.birthday = True
                    else:
                        self.currentBotSelected.birthday = False
                elif switch == self.suicidSwitch:
                    if switch.get() == 1:
                        self.currentBotSelected.suicid = True
                    else:
                        self.currentBotSelected.suicid = False
                elif switch == self.AISwitch:
                    if switch.get() == 1 and openai.api_key != "":
                        self.currentBotSelected.aiChat = True
                    else:
                        self.currentBotSelected.aiChat = False
                elif switch == self.aideSwitch:
                    if switch.get() == 1:
                        self.currentBotSelected.help = True
                    else:
                        self.currentBotSelected.help = False
                elif switch == self.chatCommandSwitch:
                    if switch.get() == 1:
                        self.currentBotSelected.chatCommand = True
                    else:
                        self.currentBotSelected.chatCommand = False

    def enableAllSwitchs(self):
        self.autojoinSwitch.configure(state="normal")
        self.modeSwitch.configure(state="normal")
        self.birthdaySwitch.configure(state="normal")
        self.suicidSwitch.configure(state="normal")
        self.modeSwitch.configure(state="normal")
        if openai.api_key != "":
            self.AISwitch.configure(state="normal")
        self.aideSwitch.configure(state="normal")
        self.chatCommandSwitch.configure(state="normal")
        self.deconnecter.configure(state="normal")


    def disableAllSwitchs(self):
        self.autojoinSwitch.configure(state="disabled")
        self.modeSwitch.configure(state="disabled")
        self.birthdaySwitch.configure(state="disabled")
        self.suicidSwitch.configure(state="disabled")
        self.modeSwitch.configure(state="disabled")
        self.AISwitch.configure(state="disabled")
        self.aideSwitch.configure(state="disabled")
        self.chatCommandSwitch.configure(state="disabled")
        self.deconnecter.configure(state="disabled")

    def updateValue(self):
        #update config file

        if self.configNickname != self.nickname.get():
            config_txt[0] = "nickname:" + self.nickname.get()
            write_file(configFileLocation,config_txt)

        #Label connected
        if len(listBots) > 1:
            self.labelConnected['text'] = str(len(listBots)) + " bots connectés"
            self.entryMsg.configure(state=tkinter.NORMAL)
        elif len(listBots) == 1:
            self.labelConnected['text'] = str(len(listBots)) + " bot connecté"
            self.entryMsg.configure(state=tkinter.NORMAL)
            self.enableAllSwitchs()
        else:
            self.rejoindre.configure(state = "normal")
            self.labelConnected['text'] = "1 Bot connecté"
            self.entryMsg.configure(state=tkinter.DISABLED)
            self.disableAllSwitchs()
            self.tchat.configure(cursor="arrow", state="normal")
            self.tchat.delete('1.0', END)
            self.tchat.configure(cursor="arrow", state="disabled")

        #Room input
        self.room.delete(0, END)
        self.room.insert(0,"")

        #Slider number of bots
        self.numberOfBots.set(1.0)           
        self.updateRadioButton()

        #init switchs
        self.getSwitchStateCurrentBot()

    def updateRadioButton(self):
        row = 6
        if len(self.listRadioButtons) > 0:
            for test in self.listRadioButtons:
                test.destroy()
            self.listRadioButtons = []

        for bot in listBots:
            self.radio_button = customtkinter.CTkRadioButton(master=self.frame_left,
                                                             text=bot.room + " - " + bot.nickname + " - (x" +str(int(self.numberOfBots.get())) + ")" ,
                                                             variable=self.var_radio,
                                                             command= lambda: [self.changeTchat(),self.getSwitchStateCurrentBot()],
                                                             value=bot.id)
            self.radio_button.grid(row=row, column=0, columnspan=1, pady=10, padx=10, sticky="w")
            row = row + 1
            self.listRadioButtons.append(self.radio_button)
            self.var_radio.set(listBots[0].id)

        self.currentBotSelected = None
        
        for bot in listBots:
            if bot.id == self.var_radio.get():
                self.currentBotSelected = bot


if __name__ == "__main__":
    app = App()
    app.mainloop()


#🐤 💥 ﷽ 🛠 🎂
