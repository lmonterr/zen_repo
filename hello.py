"""import myname
name = myname.get_name()
print("hello world {}".format(name))"""

import pymongo
import pprint
from IPython.display import clear_output

from pymongo import MongoClient
client = MongoClient("mongodb+srv://lmonterr:holamundo2021@cluster0.do2wc.mongodb.net/Cluster0?retryWrites=true&w=majority")
print(client.mflix)

pipeline = [
    {
        "$match": {
            "language": {"language": "Korean, English"}}}
]

filter = {"language": "Korean, English","rating":"UNRATED"}
clear_output()

answer = list(client.Cluster0.movies_initial.find(filter))
print("cantidad len(answer)",len(answer))
pprint.pprint(answer)



