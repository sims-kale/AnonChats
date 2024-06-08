import random
from db.user_ips import matchUsername, add_record, UserExists

nicknames = ["Maverick","Spiderman","GodFather","Jack Sparrow","Taklu Haiwan","Willy Wonka",
    "Wakanda","Archi","Sanjay Raut","Sawala Kumbhar(Swarg Return)","Lala",
    "Smith","Dighyaa","Tappu","Kombada", "Dagdu","Praju","Fandry",
    "Kubdya Khavis","Kavtya Mahakal","Tatya Vinchu","Kirkire","Inamdar Bhusnale","Durga Mavshi",
    "Lalu Prasad","Babu Kalia","Hatori","Chutaki","Nobita","Shijuka","Yeda Pakya", "Manya Surve",
    "Chotta Chetan","Bapu ji","Silencer","Salmon Bhoi","Russi","Vik_as","Ghulya","Shinde","Dr. Salunke","Daya Tappu ke papa Gada",
    "ACP Pradyuman","Basanti","Gabber","Baga","Bhide","Popatlal","Hercules","Mari","Mahesh Dalle","Binod","Lalit",
    "Dhongi Baba","Vyakii","Kanhole che Papad","Paplet","Surmai","Monya","Tyala Gad","Hyala Gad","Jay Veeru","Nattu Kaka",
    "Chalu Pandey","Bajirao Singham","Dhanjay Mane","Katakirrr","Sundar","Veronica","Mastani","Jethalal Champaklal Gada","Pinku","Alexa","siri", "Jhilmil",
    "Kashibai","Thala","Goli","Ronaldo", "Mighty Guy", "Naruto", "Kakashi Sensei", "Shinigami", "Reyuk", "Peppa Pig", "Popeye", 
    "Hakamaru", "Scoop Ninja", "Hey You", "Who am I?", "LOLMaster", "DizzyDuck", "Kanchan Kombdi","Mendoza Don","Ram Kadam", "Light Yagami","Jiva Kanhole", "Shiva Kanhole"
    ]

def getUsername(websocket):
    ip_address = websocket.remote_address[0]
    print(websocket.remote_address)
    nickname = matchUsername(ip_address)
    if nickname is None:
        unnumber = random.randint(0,100)
        nickname = nicknames[unnumber]
        if UserExists(nickname):
            return getUsername(websocket)
        
        add_record(nickname, ip_address)        
  
    return nickname
