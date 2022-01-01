from tkinter import *
from tkinter import messagebox
import json
import matplotlib.pyplot as plt


tk = Tk()

window = tk
window.geometry("300x400")
window.title("Gui for guys")

lbl = Label(window, text ="Hello")
lbl.grid(row = 3, column = 2)

#but = Button(window, text = "Press", width  = 10, command = func)
#but.grid(row = 1, column = 4)

txt = StringVar()
ent = Entry(window, width = 10, textvariable = txt)
ent.grid(row = 1, column = 1)

with open("data/A1.json", 'r') as f:
    data = json.loads(f.read())


d =  {
      "pos": "35.18753053591606,32.10378225882353,0.0",
      "id": 0
    }

with open("data/A1.json", 'w') as f:
    json.dump(d, f, indent = 0)
    json.dump(d, f, indent = 1)

Edges = [x for x in data['Edges']]
for y in Edges:
    pass
    # print(y['src'], y['w'], y['dest'])
Nodes = [x for x in data['Nodes']]
# Nodes = []
# for x in data['Nodes']:
#     Nodes.append(x)
#Pos = [x for y in Nodes for x in y['pos']]
X = []
Y = []
for y in Nodes:
    pass
    # print(y['pos'], y['pos'].split(','))
    d = y['pos'].split(',')
    X.append(float(d[0]))
    Y.append(float(d[1]))
    print(y['id'])

# print("------- X ----------------")
# print(X)
# print("------- X ----------------")
# print("------- Y ----------------")
# print(Y)
# print("------- Y ----------------")
#
# print(Edges)
# print(Nodes)

plt.plot(X, Y, 'ro')
plt.show()

window.mainloop()

d = {}
d['2'] = "Hello"
# print(d)