from os import environ

def chk_true_or_false(m):
  if m == 'True':
    return True  
  else:
    return False

TORRENT = chk_true_or_false(environ.get('TORRENT', ''))


API_ID = int(environ.get('API_ID', '283839'))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
SEND_CHANNEL = int(environ.get('SEND_CHANNEL', ''))
