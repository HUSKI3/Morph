from init import server

# Create our server instance
server = server()
# Create io
io = server.io
# Run setup for our server, passing io is mandatory
server._setup(io)
# Run the server!
server._run(io, app=server.app)