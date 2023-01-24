import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "16008660")

API_HASH = os.environ.get("API_HASH", "a40f901dbfdca8909907caabf840f606")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5816056826:AAHxQ7A1RO39ZHdwOTrSFt920PLPEa3grCE") 

FORCE_SUB = os.environ.get("FORCE_SUB", "@MovieZHubTG") 

DB_NAME = os.environ.get("DB_NAME","Cluster3")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://1:1@cluster0.pzvz3.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/fe1f25948660ccd22d2ef.mp4")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1412592290').split()]

PORT = os.environ.get('PORT', '8080')
