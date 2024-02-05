#newfile = open("newfile.txt", "w+")

#string = "This is the content that will be written to the text file."

#newfile.write(string)

import json
import os

#check if the file exists and if it is not empty
if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./ages.json", "r+")
    #load as python useful objetc (loads) and read its content
    data = json.loads(old_file.read())
    print("Current age is", data["age"], "------- adding a year.")
    data["age"] = data["age"] + 1
    print("New age is: ", data["age"])
else:
    old_file = open("./ages.json", "w+")
    data = {"name":"Nick", "age": 27}
    print("No file found, setting default age to", data["age"])

old_file.seek(0)
#convert back to a json object
old_file.write(json.dumps(data))