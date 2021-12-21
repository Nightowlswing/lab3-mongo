rs.initiate(
    {
        "_id": "my-cfg-set", 
        "configsvr": true,
        "protocolVersion": 1, 
        "members": [
            {
                "_id": 0,
                "host": "cfg-1:27017",
                "priority": 2
            },
            {
                "_id": 1,
                "host": "cfg-2:27017"
            },
            {
                "_id": 2,
                "host": "cfg-3:27017"
            }
        ]
    }
);