echo type in "start" or "stop" to control the application stack
set /p choice="Enter stop or start: "

if "choice"=="start" (
echo starting docker
docker-compose up -d
)
if "choice"=="stop" (
echo stoping docker
docker-compose down
)
