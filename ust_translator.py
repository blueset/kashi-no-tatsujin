import configparser
import json

config = configparser.ConfigParser()
with open('./wonderz/tondemowonderz.ust', "r") as f:
    f.readline()
    f.readline()
    f.readline()
    config.read_file(f)

data = []
i = 0
while f"#{i}" in config:
    lyrics = config[f"#{i}"]['Lyric']
    if lyrics == "R":
        lyrics = " "
    elif lyrics == "-":
        data[-1][1] += int(config[f"#{i}"]['Length'])
        i += 1
        continue
    data.append([lyrics, int(config[f"#{i}"]['Length'])])
    i += 1

print("[")
for char, length in data:
    print(f"  [\"{char}\", {length}],")
print("]")
