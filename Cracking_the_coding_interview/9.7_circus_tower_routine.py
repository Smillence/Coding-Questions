'''
9.7
A circus is designing a tower routine consisting of people standing atop one another's shoulders. For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her. Given the heights and weights of each person in the circus, write a method to compute the largest possible number of people in such a tower.

EXAMPLE:
Input (ht, wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)
Output: The longest tower is length 6 and includes from top to bottom: (56, 90) (60,95) (65,100) (68,110) (70,150) (75,190)


'''



# clarification quesitons:
# can people have same weights or hiehgts? (no)
# at least one people in the list? (yes)

#(height,weight)
def search(people):
    people.sort(key=lambda x:x[0])
    
    max_head = 0
    max_length = 0
    new_head = 0
    cur = 0
    while cur<len(people)-1:
               
        if people[cur][1]<people[cur+1][1]:
            cur +=1
        else:
            if cur - new_head + 1 > max_length:
                max_length = cur - new_head + 1
                max_head = new_head
                
            new_head = cur+1
            cur +=1
    if cur - new_head + 1 > max_length:  
        max_length = cur - new_head + 1
        max_head = new_head
        
    return people[max_head:max_head+max_length]
        
        
    
     
        
import random    
    
if __name__ == '__main__': 
    people = [
        (65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)
    ]
    print search(people)
    people = [
        (65, 100), (70, 150), (56, 90), (75, 90), (60, 95), (68, 110)
    ]
    print search(people)
    people = [
        (65, 94), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)
    ]
    print search(people)