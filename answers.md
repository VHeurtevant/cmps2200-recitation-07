# CMPS 2200 Recitation 10## Answers

**Name:** Viv Heurtevant


Place all written answers from `recitation-07.md` here for easier grading.



- **2)** We will visit n nodes and m edges in the worst case of this code, and the operations are constant, so the work is O(n+m)

- **4)** The worst case is only one call because we are using an undirected graph, and it will suffice to choose any node due to this undirected property. If we have the set return the same as the graph, then it must be true that it is connected, otherwise it is not. In reality, the worst case would depend on how much work is done in the call to reachable. 

- **5)** Because the work depends on reachable and the checks done after in the function are constant, the work is the same: O(n+m)

- **7)** An adjacency matrix of size mxm would require a heavier amount of work. To see all the neighbors of some node i, we would have to scan the entire row it is on which would be O(m). Therefore, scanning every row would take O(m^2) work.
