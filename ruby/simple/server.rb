require 'webrick'

# Set up the server configuration
server = WEBrick::HTTPServer.new(Port: 8000)

# Define a simple response to any request
server.mount_proc '/' do |req, res|
  res.body = 'Hello, World!'
end

# Start the server
server.start