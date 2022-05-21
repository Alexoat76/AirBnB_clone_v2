#!/usr/bin/env bash
# shellcheck disable=SC2154

# File:   0-setup_web_static.sh
# Author: Alex Orland Arévalo Tribaldos
# email:  <3915@holbertonschool.com>

# Script using bash to Sets up webservers for deployment: (Run script on both servers)

sudo apt-get update
sudo service nginx stop
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data
sudo sed -i '53i \\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
