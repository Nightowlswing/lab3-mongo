docker-compose up -d
docker cp ./rs-init.js mongo-1:rs-init.js
docker cp ./sh-init.js router:sh-init.js
docker cp ./cfg-init.js cfg-1:cfg-init.js
docker cp ./data router:data

docker exec -it mongo-1 /bin/bash -c "mongo < ./rs-init.js"
docker exec -it cfg-1 /bin/bash -c "mongo < ./cfg-init.js"
sleep 30
docker exec -it router /bin/bash -c "mongo < ./sh-init.js"
docker exec -it router sh -c "mongoimport --port 27017 -d taxi -c rides --type csv --file ./data/data/rides.csv --headerline"
