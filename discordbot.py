###SOME OF THINGS ARE DELETED CAUSE OF PRIVACY
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

#######################

#######################

greetings=['hello','hey','hlo','heya']
for word in bad_words:
    if word.isupper():
        bad_words.append(word.lower())

starter_words = [
    "Gaali Mat De",
    "Tere me Sudhdhata hein ki nai",
    "E Deva Gaali nai Dene ka Baba"
]

if 'responding' not in db.keys():
    db['responding']=True

def get_quote():
    ##########################################
    json_data = json.loads(response.text)
    quote=json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

def update_words(bad_message):
    if 'words' in db.keys():
        words=db['words']
        words.append(bad_message)
        db['words']=words
    else:
        db['words']=[bad_message]

def delete_bad(index):
    words=db['words']
    if len(words)>index:
        del words[index]
        db['words']= words

#########
async def on_ready():
    print('E Raju Me AA Gaya {0.user}'.format(client))

############
async def on_message(message):
    if message.author == client.user:
        return
    
    msg=message.content
    reply=message.channel.send

    if any(word in msg.casefold() for word in greetings):
        await reply('Bol na re Baba')

    if msg.startswith('$sunao'):
        quote =get_quote()
        await reply('YE ENGLISH ME HEIN MUJHE SAMAJH NAHI AAYA TUHI PADHLE \n {} \n KHUSH HOJA'.format(quote))
    bads=bad_words

    if db['responding']:
        options=starter_words
        if 'words'in db.keys():
            bads +=db['words']
        
        if any(word in msg.casefold() for word in ####):
            del words[index]
            await reply(random.choice(options))
    
    if msg.startswith('$newgaali'):
        bad_word=msg.split("$newgaali ",1)[1]
        update_words(bad_word)
        await reply('DONE bachcha')

    # if msg.startswith('$del'):
    #     good_words=[]
    #     if 'words' in db.keys():
    #         index=int(msg.split('$del',1)[1])
    #         delete_bad(index)
    #         good_words=db['words']
    #     await reply(good_words)

    if msg.startswith("$list"):
        bad_word=[]
        if 'words' in db.keys():
            bad_word=db['words']
        await reply(bad_word)

    if msg.startswith('$responding'):
        value = msg.split('$responding ',1)[1]

        if value.lower() == 'true':
            db['responding']=True
            await reply('Me Bolunga')
        
        
        elif value.lower() == 'false':
            db['responding']=False
            await reply('Me Nahi Bolunga')
keep_alive()
client.run(os.getenv('TOKEN'))
