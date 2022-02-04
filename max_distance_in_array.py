#given a list of non-negative integers ,find the maximum distance j-i , where A[i]<=A[j]
#array[4,2,8,1,0,7] =>A[4]=0 A[3]=8 i=4 j=3 j-i=3-4=-1  sort[0,1,2,4,7,8] 
#[(4,0),(2,1),(8,2),(1,3),(0,4),(7,5)]
#sorted_array[(0,4),(1,3),(2,1),(4,0),(7,5)(8,2)]
#minimum_index_number=4
#find maximum j-i
#https://www.interviewbit.com/problems/max-distance/

def maximumDistance(A):
    numbers=[]
    for i,num in enumerate(A):
        numbers.append((num,i))
    numbers.sort()
    max_gap=0
    minimum_index_number=numbers[0][1]
    for element in numbers:
        index_number=element[1]
        if index_number<=minimum_index_number:
            minimum_index_number=index_number
        else:
            max_gap=max(max_gap, index_number-minimum_index_number)
    return max_gap
A=[3,5,4,2]
print(maximumDistance(A))
