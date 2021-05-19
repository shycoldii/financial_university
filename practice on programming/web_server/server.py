import logging
import socket
import configparser
import threading
import time

def get_new_response(conn,MAX,DIRECTORY):
  """
  Функция реализует GET-запрос от клиента и передает данные разного типа
  """
  
  while True:
    logging.info("CONNECTION WITH "+str(conn))
    data = conn.recv(MAX)
    try:
        msg = data.decode().split()[1][1:]
    except:
        msg = ""
    if not msg:
      msg = 'index.html'
    if msg[-1] == '?':
      msg = msg[:-1]
    try:
      exp = msg.split('.')[1]
    except:
      exp = ''
    content = {"css":"text/css","min": "text/css","html":"text/html","png":"image/png",
               "jpeg": "image/jpeg","js": "text/javascript","jpg": "image/jpeg","txt": "text/plain",
               "json":"text/json","ico":"image/x-icon"}
    content_type = ""
    message = ""
    response = "HTTP/1.1 "
    length = 0
    try:
      content_type = content[exp]
      try:
            logging.info(f'{msg} - {addr[0]} - 200 OK')
            file = open(DIRECTORY + msg, "rb")
            message = file.read()
            length = len(message)
            file.close()
            response += "200 OK\r\n"
      except FileNotFoundError:
        response+='404 NOT FOUND\r\n'
        logging.info(f'{msg} - {addr[0]} - 404 NOT FOUND')
    except Exception:
      logging.info(f'{msg} - {addr[0]} - 403 FORBIDDEN')
      response += '403 FORBIDDEN\r\n'
    response+= f"Content-Type:{content_type}\r\n"
    response+=f"Date: {time.ctime()}\r\n"
    response+="Server: Server v0.0.1\r\n"
    response+=f"Content-Length: {length}\r\n"
    response+="Connection: close\r\n"
    response += "\r\n"
    if message:
      msg = response.encode() + message
      conn.send(msg)
    else:
      msg = response.encode()
      conn.send(msg)
    logging.info(f'SENT RESPONSE {response}')
    conn.close()
    return
#================================================
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
config = configparser.ConfigParser()
config.read('config.ini')
HOST = config["Settings"]["HOST"]
PORT = int(config["Settings"]["PORT"])
DIRECTORY = config["Settings"]["DIRECTORY"]
MAX = int(config["Settings"]["MAX"])
sock = socket.socket()
try:
  sock.bind((HOST,PORT))
  print("SERVER IS STARTING ON " + str(PORT))
  logging.info("SERVER IS STARTING ON " + str(PORT))
except:
  sock.bind(("localhost",8080))
  print("SERVER IS STARTING ON 8080")
  logging.info("SERVER IS STARTING ON 8080")
sock.listen()
#================================================

while True:
    conn, addr = sock.accept()
    t1 = threading.Thread(target=get_new_response, args=[conn, MAX,DIRECTORY])
    t1.start()



