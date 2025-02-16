import random
#Stack operations -

#Create an empty list
stack_list = []
#It is for creating the stack_list of 20 elements(length=20)
for i in range(1, 21):
#Each time it iterates, it will append each randomly picked no. in the given range
    rand_numbers=random.randint(1, 11)
    stack_list.append(rand_numbers)
print(f"Stack_list: {stack_list}")

def push_operation(stack_list, num):
#The given no. as input will be pushed/appended in the stack_list.
    stack_list.append(num)
    print(f"Stack_list after the push operation: {stack_list}")

def pop_operation(stack_list):
#It will automatically pop out the last element (S.top) of the stack_list (LIFO); no input required.
    stack_list.pop()
    print(f"Stack_list after the pop() operation: {stack_list}")

def main():
    num=int(input("Enter a number that you want to push into the stack_list: "))
    push_operation(stack_list, num)
    pop_operation(stack_list)
if __name__ == "__main__":
    main()


#Queue operations -

queue_list = []
for i in range(1, 21):
    rand_numbers=random.randint(1, 11)
    queue_list.append(rand_numbers)
print(f"Queue list: {queue_list}")

def enqueue_operation(queue_list, num):
    queue_list.append(num)
    print(f"Queue_list after the enqueue operation: {queue_list}")

def dequeue_operation(queue_list):
#Here, FIFO - so, index of the first element of the queue_list need to be given, so that it can pop out the first element.
    popped_element=queue_list.pop(0)
    print(f"Popped element from the queue: {popped_element}")

def main():
    num = int(input("Enter a number that you want to push into the queue_list: "))
    enqueue_operation(queue_list, num)
    dequeue_operation(queue_list)
if __name__ == "__main__":
    main()
