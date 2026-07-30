 

# Идеально отображается в браузере и копируется в код
matrix_without_cycles= [
    [0, 1, 1, 0],  # Из вершины 0 ведут стрелки в 1 и 2
    [0, 0, 0, 1],  # Из вершины 1 ведет стрелка в 3
    [0, 0, 0, 1],  # Из вершины 2 ведет стрелка в 3
    [0, 0, 0, 0]   # Из вершины 3 стрелок нет (тупик/сток)
]

# Матрица смежности с циклом 0-1-3-0
matrix_with_cycle = [
    (0, 1, 1, 0),  # 0 -> 1, 0 -> 2
    (0, 0, 0, 1),  # 1 -> 3
    (0, 0, 0, 1),  # 2 -> 3
    (1, 0, 0, 0)   # 3 -> 0 (ЗАМЫКАЮЩЕЕ РЕБРО ЦИКЛА)
]


# better in breadth
matrix =matrix_with_cycle
#matrix =matrix_without_cycles



w_register = [0,0,0, 0] #list still we can change it for array of ints
w_head = 0
w_tail =1

w_visited = [True,False,False, False] #list still we can change it for array of ints
real_edges= 0
i = 0

#without cycles just one pass



while (w_head  <  w_tail):
    i= w_register[w_head]
    print(f"now we are on {w_register[w_head]} row")
    w_head += 1
    for j in range(len(matrix[i])):
        if(matrix[i][j] > 0 and not w_visited[j] ):

            w_register[w_tail] = j
            w_tail += 1
            w_visited[j]=True
            real_edges += 1
            print(f"tail {w_tail} head {w_head} register {w_register}")
        elif(matrix[i][j] > 0 and  w_visited[j] ):
            print(f"The edge {j} already exist skipping")
            real_edges += 1
        else:
            pass


if(len(w_visited) < real_edges):
    print(f"the graph has cycles, there are  {real_edges} vs {w_visited}")
else:
    print(f"the graph has no  cycles, there are  {real_edges} vs {w_visited}")


    


        
        
           
        

            
