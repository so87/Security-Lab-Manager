echo create volume for storage
docker volume create --name postgresql -d local
docker volume create --name postgresql-data -d local

echo opening firewall
netsh advfirewall firewall add rule name="Open for docker http" protocol=TCP dir=in localport=8080 action=allow
netsh advfirewall firewall add rule name="Open for docker https" protocol=TCP dir=in localport=8443 action=allow

echo starting containers
docker-compose up -d --build
