from collections import deque

def BFS(graph):
    search_queue = deque()
    search_queue += graph["you"]
    searched = set()
    
    while search_queue:
        person = search_queue.popleft()
        
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    
    return False

def person_is_seller(name):
    return name[-1] == 'm'

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anju", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anju"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print(BFS(graph))