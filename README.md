# Magnolia denudata

玉兰花，起源于中国，初春开花，先开花而后长叶

Jack Ma will tell you which kind of green teas are popular in China!

Step0: in config.py, you can change the key word(for example: you can change "绿茶" to "红茶"), or change the database name and the collection name. 

Step1: use taobao_tea_mongo.py to get all the selling information about green tea in TaoBao, then store them in local MongoDB.

Step2: use get_la_lo.py to drag all the location information in mongo then change them into 'longitude','latitude',and finally write them into .CSV file, which is the recognisable format on the CARTO.
