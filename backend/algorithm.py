from treap import treap as Treap

class Node:
    predecessor = None
    tentative_g = None
    def __heuristic__(handle1, handle2):
        print("Not implemented!")
        #todo: Propinquity analysis
        #todo: last 200 tweets fetchen
        #      similiarity check using fasttext
    def heuristic():
        print("Not implemented!")
        #todo

    def __getFriends__():
        #todo

    def successors():
        #todo
    
list_open = Treap() #Prioritätenwarteschlange
list_closed = []

def astar(handle1, handle2):
    list_open = Treap() #Prioritätenwarteschlange
    list_closed = []

    # Initialisierung der Open List, die Closed List ist noch leer
    # (die Priorität bzw. der f-Wert des Startknotens ist unerheblich)
    list_open.insert(xx, 0) #Todo node

    # diese Schleife wird durchlaufen bis entweder
    # - die optimale Lösung gefunden wurde oder
    # - feststeht, dass keine Lösung existiert
    while not list_open.empty():
        # Knoten mit dem geringsten f-Wert aus der Open List entfernen
        currentNode = list_open.remove_min() #todo check for return

        # Der aktuelle Knoten soll durch nachfolgende Funktionen
        # nicht weiter untersucht werden, damit keine Zyklen entstehen
        list_closed.append(currentNode)

        # Wurde das Ziel gefunden?
        if currentNode == zielknoten:
            return list_closed

        # Wenn das Ziel noch nicht gefunden wurde: Nachfolgeknoten
        # des aktuellen Knotens auf die Open List setzen
        expandNode(currentNode)
    
    # die Open List ist leer, es existiert kein Pfad zum Ziel
    return None

# überprüft alle Nachfolgeknoten und fügt sie der Open List hinzu, wenn entweder
# - der Nachfolgeknoten zum ersten Mal gefunden wird oder
# - ein besserer Weg zu diesem Knoten gefunden wird
def expandNode(currentNode):
    for #successor of currentNode:
        # wenn der Nachfolgeknoten bereits auf der Closed List ist – tue nichts
        if successor in list_closed:
            continue

        # g-Wert für den neuen Weg berechnen: g-Wert des Vorgängers plus
        # die Kosten der gerade benutzten Kante
        tentative_g = currentNode.tentative_g + 1 #c(currentNode, successor)
        # wenn der Nachfolgeknoten bereits auf der Open List ist,
        # aber der neue Weg nicht besser ist als der alte – tue nichts
        if successor in list_open.items and tentative_g >= successor.tentative_g:
            continue

        # Vorgängerzeiger setzen und g Wert merken
        successor.predecessor = currentNode
        successor.tentative_g = tentative_g
        # f-Wert des Knotens in der Open List aktualisieren
        # bzw. Knoten mit f-Wert in die Open List einfügen
        f := tentative_g + successor.heuristic()
        if successor in openlist.items:
            #idea: openlist.decreaseKey(successor, f)
            list_open.remove(successor)
            list_open.insert(successor, f)
        else
            list_open.insert(successor, f)