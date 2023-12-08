#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

sudo apt -y update;
sudo apt install -y nginx;

sleep 5;

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

if [ -f /data/web_static/current ]
then
	rm /data/web_static/current;
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current
else
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current
fi

sudo chown -hR ubuntu:ubuntu /data/

echo "<h1 style=\"color: green;\">Test deploy script</h1>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

new_line="location /hbnb_static {"
new_string="\t$new_line\n\t\talias /data/web_static/current/;\n\t}"
file="/etc/nginx/sites-enabled/default"
if ! grep -Pxq "\t$new_line" $file
then
        sudo sed -i "54i\\$new_string" $file;
fi
sudo service nginx restart
