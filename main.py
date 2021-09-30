from Morph import server as morph
from Morph.tools.forge import character
from Morph.tools.designer import GUI

# Create our server instance
server = morph()
server.app.debug = False

# Run setup for our server, passing io is mandatory
server._setup()

# Here we can define our desired character
char = character(
  ['name','class','type','xp','lvl','act_quest','inv']
)

# To get the dictionary for a character 
# (Using a non-class server object cause don't want ugly objects in output)
morph._log('Character class',char.all_pretty)

# Connect type let's us choose how a client can connect to the socket
# before authenticating
server.require(connect_type = 'id')
# Access type let's us choose the way the client can authenticate
server.require(access_type = 'token')

# Game is now required to send data in the following format
server.require(user_type = char._type)

# Here we can create a mini flask server to show us the data about our Morph server
# Fake user count as I have no way to test it yet!
server.users = 20
ourgui = GUI(server)
ourgui.open_gui()

# Custom function
# Grab the users connected on our custom event
@server.io.on('aaa')
def aaa(data):
  print(server.users)

# Run the server!
server._run()