#!/usr/bin/env bash
# Scripting setting up web servers for the deployment of web_static

# Updating and installing Nginx if not already installed
sudo apt-get update -y
sudo apt-get install nginx -y

# Creating the required directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Creating a fake HTML file
echo "<html>
  <head>
    </head>
      <body>
          Holberton School
	    </body>
	    </html>" | sudo tee /data/web_static/releases/test/index.html

	    # Creating the symbolic linkor recreating it if it already exists
	    sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

	    # Giving ownership of the /data/ folder to ubuntu user and group
	    sudo chown -R ubuntu:ubuntu /data/

	    # Updating Nginx configuration to serve the content
	    sudo sed -i '/server_name _;/a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

	    # Restarting Nginx to apply the changes
	    sudo service nginx restart

	    # Exit successfully
	    exit 0

