#Simple python code to push and pop operation in a priority queue or min-heap
#It is an arrey implimentation of heap (complete binary tree) i.e. i-th term in the array has left child at 2*i+1, right child at 2*i+2 index of the array





def min_heap_push(heap, node):
  heap.append(node)
  if len(heap) != 1:
    current_index = len(heap) - 1
    current_node = heap[current_index]
    parent_index = int(current_index/2)
    parent_node = heap[parent_index]
    while current_node < parent_node:      #Makes the parent lower value than the current node by replacing
      heap[parent_index] = current_node
      heap[current_index] = parent_node
      current_index = parent_index
      current_node = heap[current_index]
      if current_index != 0:
        parent_index = int(current_index/2)
        parent_node = heap[parent_index]
      else:
        break
    return heap
  else:
    return heap
    
    
    
    
    
    
def min_heap_pop(heap):
    poped = heap[0]
    current_index = 0
    current_node = heap[len(heap)-1]
    heap = heap[:len(heap)-1]
    heap[0] = current_node
    while True:                           #recursively update the min heap
      #print(heap)

      if 2*current_index + 1 < len(heap):    
        child_index_1 = 2*current_index + 1
        child_1 = heap[child_index_1]    #create left child

        if 2*current_index + 2 < len(heap):    #create right child if exists, may not exist as it is complete binary tree
          child_index_2 = 2*current_index + 2
          child_2 = heap[child_index_2]        

          if child_1 < child_2:    #if right child exist then make their minimum as the child to compare with the current node else simply make the left child as comparing child
            child = child_1
            child_index = child_index_1
          else:
            child = child_2
            child_index = child_index_2
        else:
            child = child_1
            child_index = child_index_1
        if child < current_node:
          temp = child
          temp_index = current_index
          heap[child_index] = current_node
          current_index = child_index
          heap[temp_index] = temp
        else:
          break
      else:
        break

    return heap, poped
    
    
    
    
    
    
    
if __name__ == '__main__':
        #Push in a heap from a given list to create a heap
	heap = []
	List = [7, 2, 18, 20, 17, 9, 11, 12, 18, 22, 5, 1]
	for i in range(len(List)):
	  heap = min_heap_push(heap, List[i])
	  print(heap)
	  
	#Pop all the elements from the heap
	count = 0
	initial_heap_length = len(heap)
	print("\n Should return the values in increasing order as it is a min heap \n")
	while count < initial_heap_length - 1:
	  heap, poped = min_heap_pop(heap)
	  print(poped)
	  count += 1  
