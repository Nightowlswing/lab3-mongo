sh.addShard("my-mongo-set/mongo-1:27017,mongo-2:27017,mongo-3:27017");
sh.enableSharding('taxi');
sh.shardCollection('taxi.rides', {start_latitude: "hashed"});