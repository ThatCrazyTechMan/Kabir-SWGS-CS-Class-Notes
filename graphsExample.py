A = {'B':4, 'C':5, "E":7}
B = {'A':4, "E":2}
C = {"A":5, "D":1}
D = {"C":1}
E = {"A":7,"B":2}
graph1 = {'A':{'B':4, 'C':5, "E":7},'B':{'A':4, "E":2}}
graph = [A,B,C,D,E]
print(A['B'])
travelfrom = "A"
travelto = "B"
print(graph1[travelfrom][travelto])