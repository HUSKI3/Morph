# Morph
### A simple and free MMO server written in Python

Morph is a simple utility for hosting a socket.io MMO server. What it can offer:

- Custom instances
- Custom characters
- Account system
- GUI for managing instances
- Easily creatable systems (Crafting, Looting and more)

### How to get started:
> Make sure to install [poetry](https://python-poetry.org/), this will handle all the dependencies.

Below is a small and easy to use example of a Morph instance:
```python
from Morph import server as morph

# Create our server instance
server = morph()
server.app.debug = False

# Set up the server
server._setup()

# Make it so that every user needs to provide a unique ID
server.require(connect_type = 'id')

# Run the server!
server._run()
```
