d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d3 = dict(d1) 
d3.update(d2) 

for i, j in d1.items():

    for a, b in d2.items():

        if i == a:

            d3[i]=(j+b)

print(d3)