# Remove the black pixels which are not connected to the edges with other black pixels  or them selves , 0 -> white pixel , 1 -> black pixel

'''       0 1 2 3 4 5 m

    0    [1,0,0,0,0,0]                   
    1    [0,1,0,1,1,1]
    2    [0,0,1,0,1,0]
    3    [1,1,0,0,1,0]
    4    [1,0,1,1,0,0]
    5    [1,0,0,0,0,1]
    n

    (n,m)

        [1,0,0,0,0,0]
        [0,0,0,1,1,1]
        [0,0,0,0,1,0]
        [1,1,0,0,1,0]
        [1,0,0,0,0,0]
        [1,0,0,0,0,1]
'''

def path_search(edge, edges ):
    e1 = edge[0]
    e2 = edge[1]
    
    if e1 + 1 <= 5 and img[e1 + 1][e2] == 1 and img[e1+ 1][e2] not in edges :
        edges.add([e1 + 1,e2])
        path_search([e1+1,e2],edges)

    if e2 + 1 <= 5 and img[e1  ][e2 + 1] == 1 and img[e1 ][ e2 + 1] not in edges :
        edges.add([e1 ,e2 + 1])
        path_search([e1 ,e2 + 1],edges)

    if e1 - 1 >= 0 and img[e1 - 1 ][e2  ] == 1 and img[e1 - 1 ][e2 ] not in edges  :
        edges.append([e1 - 1,e2 ])
        path_search([e1 - 1 ,e2 ],edges)

    if e2 -1 >= 0 and img[e1 ][e2 - 1 ] == 1 and img[e1 ][e2 - 1] not in edges  :
        edges.append([e1,e2 - 1])
        path_search([e1 ,e2 - 1],edges)

    else :
        edges
        return
    
def remove_islands(img):
    edges = []
    for i in range(len(img)):
        for j in range(len(img)):
            if (img[i][j]  == 1) and (i == 0 or  i==5 or j == 0 or j == 5):
                edges.append([i,j])
    print(edges)
    
    # for i in edges:    
    path_search([3,0],edges )   
    print (edges)
        
img = [ [1,0,0,0,0,0],                   
        [0,1,0,1,1,1],
        [0,0,1,0,1,0],
        [1,1,0,0,1,0],
        [1,0,1,1,0,0],
        [1,0,0,0,0,1],
]

remove_islands(img)