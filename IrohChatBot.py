import random
import tweepy
import math
from tweepy.streaming import StreamListener
from tweepy import Stream
import logging
#from config import create_api
import time
#METHODS
class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        print(status)

def findNewWord (topicList, lines, lengthOfData, wordsAfterChosen):
    wordsAfter(topicList, lines, lengthOfData, wordsAfterChosen)
    wordsBefore
    
def wordsBefore (topicList, lines, lengthOfData): 
    wordsBeforeChosen = []
    for x in range(lengthOfData):
        for y in range(120):
            if len(topicList) > 2:
                if lines[x][y] == topicList[0]:
                    if lines[x][y-1] == topicList[(2)]:
                        #if lines[x][y-1] == topicList[(len(topicList) - 3)]:
                        wordsBeforeChosen.append(lines[x][y-2])
            else:
                if lines[x][y] == topicList[(len(topicList)-1)]:
                    wordsBeforeChosen.append(lines[x][y-1])
    return wordsBeforeChosen
    
def wordsAfter (topicList, lines, lengthOfData, wordsAfterChosen):    
    wordsAfterChosen = []
    for x in range(lengthOfData):
        for y in range(120):
            if len(topicList) > 2:
                if lines[x][y] == topicList[(len(topicList) - 1)]:
                    if lines[x][y-1] == topicList[(len(topicList) - 2)]:
                        #if lines[x][y-1] == topicList[(len(topicList) - 3)]:
                        wordsAfterChosen.append(lines[x][y+1])
            else:
                if lines[x][y] == topicList[(len(topicList)-1)]:
                    wordsAfterChosen.append(lines[x][y+1])
    return wordsAfterChosen
def chooseNewWord(wordsAfterChosen):
    #print("options to choose from")
    #print(wordsAfterChosen)
    validWord = False
    wordAvailable = False
    count = int(0)
    while validWord == False and count < 5:
        if len(wordsAfterChosen) > 0:
        #print()
            selectedWord = random.randint(0,len(wordsAfterChosen)-1)
            if wordsAfterChosen[selectedWord] != "":
                validWord = True
                return wordsAfterChosen[selectedWord]
        else:
            validWord = True
            return False
        count = count + 1
    if count >= 5:
        return False
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

"""def check_mentions(api, keywords, since_id, statement):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")
            
            if not tweet.user.following:
                tweet.user.follow()
            api.update_status(
                status = statement,
                in_reply_to_status_id = tweet.id,
            )
        return new_since_id
        
def main():
    #api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api,["help","support"], since_id)
        logger.info("Waiting...")
        time.sleep(60)



#MAIN METHOD
CONSUMER_KEY = '3HIKiV12uQGSBDPp4ojwtNg44'
CONSUMER_SECRET ='FT9roKQKlrHuIuU9sDcJLm0EuzcZtdeAiMR3hZSyWdYM7aHzvV'
ACCESS_KEY ='1265531723342807044-8qZocWTGxl38G9yApzwlP6mSagHN2R'
ACCESS_SECRET ='c0V8YxP2oHP5H2GIxZICLnFOAUK8JQsz3A3g6IqrbvXSa'
"""




"""auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)"""

#api.update_status("Testing")

linesToConvert = []
wordsAfterChosen = []
wordsBeforeChosen = []
#lines = [[0 for x in range(120)] for y in range(343)]
#print(lines[row][col]
f = open("everyUncleIrohLine.txt", "r")
fline = f.readlines()
stringY = ""
for x in fline: #
    linesToConvert.append(x) 
lines = [["" for x in range(200)] for y in range(len(linesToConvert)+1)]    
lengthOfData = len(linesToConvert)
#print(len(linesToConvert))
#lines[7][5] = 7
#print(lines[7][5])
#builds a list of 70,000 words
#for x in range(0, len(lines)ToConvert):
#    lines[x] = lines[x].replace("\n", "")
string = ""
stringAdd = ""
z = int(0)
for x in range(0, len(linesToConvert)):
    string = linesToConvert[x]
    z = int(0)
    for y in range(0, len(string)):
        if string[y] == " " or string[y] == "\n" or string[y] == "." or string[y] == "!" or string[y] == ",":
            lines[x][z] = stringAdd
            stringAdd = ""
            z = z + 1
        else:
            stringAdd = stringAdd + string[y]
        if string[y] == "." or string[y] == "!" or string[y] == ",":
            lines[x][z] = string[y]
            z = z + 1
#print(lines[3][0])
#for x in range(len(linesToConvert)):
#    print("")
#    for y in range(59):
#        print(lines[x][y], end = " ")

topic  = input("what do you want Iroh to talk about")
topicList = [topic]
statement = topic
a = int(0)
while a < 100:
    wordsAfterChosen = wordsAfter(topicList, lines, lengthOfData, wordsAfterChosen)
    #wordsBeforeChosen = wordsBefore(topicList, lines, lengthOfData)
    topic = str(chooseNewWord(wordsAfterChosen))
    if topic != "":
        topicList.append(topic)
    #print(topicList)
    wordsBeforeChosen = wordsBefore(topicList, lines, lengthOfData)
    topic = str(chooseNewWord(wordsBeforeChosen))
    if topic != "" and topic != topicList[0] and topic != False:
        topicList.insert(0, topic)
    #statement = statement + " " + topic
    a = a+1
print(topicList)
for x in range (0, len(topicList)):
    if topicList[x] != "False":
        print(topicList[x], end=" ")

#listener = StdOutListener()

#stream = Stream(auth, listener)

#stream.filter(track=['@UncleIrohBot'])

#api.update_status(statement)
"""if __name__ == "__main__":
    main()"""

        
