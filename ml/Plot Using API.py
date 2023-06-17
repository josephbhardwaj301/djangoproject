import json
import matplotlib.pyplot as plt
import requests

path = "https://gist.githubusercontent.com/josephbhardwaj301/09f4885c373427e40d5999dfb88c8d2a/raw/d4755337ac0d2158aa678ae30d847c765bcc9b88/PLOT.json"
response = requests.get(path)
# print(response)
# print(response.status_code)
# print(response.text)
jsonoutput = json.loads(response.text)
# print(jsonoutput)
# print(type(jsonoutput["x"]), jsonoutput["y"])
x = jsonoutput["x"]
y = jsonoutput["y"]
print(x, y)
plt.plot(x,y)
plt.show()
