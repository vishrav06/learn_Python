def locate_cards(cards, query):
    pos = 0
    for val in cards:
        if val == query:
            return pos
        else:
            pos+=1
        
    return -1


# test = {'input': {'cards' : [13, 11, 8, 6, 4, 1], 'query' : 8}, 'output' : 2}
test = {'input' : {"cards" : [], 'query' : 4}, 'output' : -1}
     
b = locate_cards(**test['input']) == test['output']
print (b)