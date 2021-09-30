from Morph import handler, server
import json

class character:

  _handler = handler(type='char')
  
  def __init__(self,keys):
    self._keys = keys
    self._type = 'char'
    self.all = dict.fromkeys(self._keys, None)
    self.all_pretty = json.dumps(self.all, indent=4, sort_keys=True)