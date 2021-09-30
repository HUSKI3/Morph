from flask import Flask, request, session, jsonify, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_cors import CORS, cross_origin
import logging

class server:

  def __init__(self):
    self.app = Flask('app')
    self.app.debug=True
    self.app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'
    self.log = logging.getLogger('werkzeug')
    self.log.setLevel(logging.ERROR)
    self.app.logger.disabled = True
    self.log.disabled = True
    self.io = SocketIO()
    self._caller()

    self.users = []
    self._requirements = {}
  
  def _setup(self):
    CORS(self.app, resources={r"/*": {"origins": "*"}})
    self.io.init_app(self.app,cors_allowed_origins="*", async_mode='eventlet')
    server._log('Setup complete...')
    
  def _log(*args):
    print('[Server]'," ".join(map(str,args)))
  
  def _run(self):
    self.io.run(app=self.app,host='0.0.0.0', port=8080)

  def _caller(self):
    @self.io.on('connected')
    def connected(user):
      self.users.append(user)
      if self.has_required('connect_type',user):
        sid = user['id']
        server._log(f'User { sid } connected to shard')
      else:
        server._log('A user tried to connect to shard, failed to pass connection type!')
        self.io.emit('error',{'msg':'A user tried to connect to shard, failed to pass connection type!'})
  
  def require(self, user_type=None, access_type=None, connect_type=None, client_type=None):
    if user_type:
      server._log('Now requiring user to be of type:',user_type)
      self._requirements['user_type'] = user_type
    if connect_type:
      server._log('Now requiring connection to be of type:',connect_type)
      self._requirements['connect_type'] = connect_type
    if access_type:
      server._log('Now requiring access to be of type:',access_type)
      self._requirements['access_type'] = access_type
  
  def has_required(self, type_of, data):
    if self._requirements[type_of] in data:
      return True
    else:
      return False

class handler:

  def __init__(self, type=None):
    if type:
      print('Created handler of type',type)
    else:
      raise "Failed to create handler, none or incorrect type set!"