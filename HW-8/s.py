from collections import deque, defaultdict

def find_spy(n, trust):
  trust_connections, trustee_conections = create_connectons(trust)
  spy = -1
  for person in range(1, n + 1):
    if person not in trust_connections and len(trustee_conections[person]) == n - 1:
      if spy != -1:
        return -1
      spy = person
  return spy
  
def create_connectons(trust):
  connections = defaultdict(list)
  connections_2 = defaultdict(list)

  for person, trustee in trust:
    connections[person].append(trustee)
    connections_2[trustee].append(person)

  return connections, connections_2

#print(find_spy(2, [(1,2)]))
#print(find_spy(3, [(1,3),(2,3)]))
#print(find_spy(3, [(1,3),(2,3),(3,1)]))
#print(find_spy(3, [(1,2),(2,3)]))
#print(find_spy(4, [(1,3),(1,4),(2,3),(2,4),(4,3)]))