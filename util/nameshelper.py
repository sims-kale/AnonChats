import random
from db.user_ips import matchUsername, add_record, UserExists

nicknames = ["Maverick","Spiderman","Jerry","GodFather","Jack Sparrow","Taklu Haiwan","Willy Wonka",
    "Wakanda","Archi","Tylor","Sanjay Raut","Sawala Kumbhar(Swarg Return)","Lala","Maleficent","Evelyn Salt",
    "Smith","Dighyaa","Erin Brockovich","Tessract","Tappu","Kombada", "Dagdu","Praju","Fandry","Danny Ocean",
    "Kubdya Khavis","Kavtya Mahakale","Tatya Vinchu","Jack Dawson","Kirkire","Inamdar Bhusnale","Durga Mavshi",
    "Lalu Prasad","Babu Kalia","Chota Bheem","Hatori","Chutaki","Nobita","Shijuka","Yeda Pakya", "Manya Surve",
    "Chotta Chetan","Bapu ji","Silencer","Salmon Bhoi","Russi","Vik_as","Ghulya","Shinde","Dr. Salunke","Daya Bhabi",
    "ACP Pradyuman","Basanti","Gabber","Baga","Bhide","Popatlal","Hercules","Mari","Mahesh Dalle","Binod","Lalit",
    "Dhongi Baba","Vyakii","Kanohale che Papad","Paplet","Surmai","Monya","TyalaGad","HyalaGad","Vijay","Jay Veeru","Nattu Kaka",
    "Chulbul Pandey","Bajirao Singham","Dhanjay Mane","Katakirrr","Sundar","Veronica","Mastani","Jethalal","Piku","Alex","Jhilmil",
    "Kashibai","Thala","Goli","Ronaldo", "Mighty Guy", "Naruto", "Kakashi Sensei", "Shinigami", "Reyuk", "Peppa Pig", "Poopy", 
    "Hakamaru", "Scoop Ninja", "Hey You", "Who am I?", "LOLMaster", "DizzyDuck"]

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