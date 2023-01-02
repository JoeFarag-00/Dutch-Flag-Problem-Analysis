from timeit import default_timer as timer
import big_o
def QuickSort(Algo_List):
    def partition(Algo_List, low, high):
        pivot = Algo_List[high]
        i = low - 1
        for j in range(low, high):
            if Algo_List[j] <= pivot:
                i = i + 1
                (Algo_List[i], Algo_List[j]) = (Algo_List[j], Algo_List[i])
        (Algo_List[i + 1], Algo_List[high]) = (Algo_List[high], Algo_List[i + 1])
        return i + 1
    
    def Sort_Part(Algo_List, low, high):
        if low < high:
            pi = partition(Algo_List, low, high)
            Sort_Part(Algo_List, low, pi - 1)
            Sort_Part(Algo_List, pi + 1, high)
        
    size = len(Algo_List)
    Sort_Part(Algo_List, 0, size - 1)
    print("Quick-Sorted List: ", Algo_List)
    
def InsertionSort(Algo_List):
    for i in range(len(Algo_List)):
        temp = Algo_List[i]
        j = i - 1
        while j >= 0 and temp < Algo_List[j]:
            Algo_List[j + 1] = Algo_List[j]
            j -= 1
            Algo_List[j + 1] = temp
    print("Insertion Sorted: ",Algo_List)


User_List_Input = input("Enter List Vars: ")
Algo_List = User_List_Input.split(" ")
for i in range(len(Algo_List)):
    Algo_List[i] = int(Algo_List[i])

print("\n")

User_Algo_Input = input("Enter Algorithim type: ")

if(User_Algo_Input == '1'):
    start = timer()
    QuickSort(Algo_List)
    end = timer()
    print("Execution Time: ", end - start)
    
    
elif User_Algo_Input == '2':
    start = timer()
    InsertionSort(Algo_List)
    end = timer()
    print("Execution Time: ", end - start)
