

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
matrix =matrix_without_cycles


queue =[]
visited =set()
visited.add(0)
real_edges= 0
i = 0
queue.append(0)
while (queue):
    i = queue.pop(0)
    for j in range(len(matrix[i])):
        if(matrix[i][j] > 0 and not j in visited):
            queue.append(j)
            visited.add(j)
            real_edges += 1
        elif(matrix[i][j] > 0 and  j in visited):
            real_edges += 1
        else:
            pass


if(len(visited) < real_edges):
    print(f"the graph has cycles, there are  {real_edges} vs {visited}")
else:
    print(f"the graph has no  cycles, there are  {real_edges} vs {visited}")


    


        
        
           
        

            
