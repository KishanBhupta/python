
#include<stdio.h>
#include<conio.h>
int tos=-1;
int choice , newElement , stacksize;
int stack[5];
int main()
{
    while(choice != 5)
    {
        printf("\n 1.Create a stack \n 2. Push Element \n 3. Pop Element \n 4. Display Delement  \n 5. Exit ");
        choice = printf("Enter a choice :");
        scanf("%d" ,&choice);
        
        if (choice == 1)
        {
            printf("Enter a size of stack :");
            scanf("%d",&stacksize);
            stack[stacksize];
            printf("Stack is Create !!");
        }
        else if (choice == 2)
        {
            printf("Enter a  new element :");
            scanf("%d",&newElement);
            push(newElement);
            display();
        }
        
        else if (choice == 3)
        {
            pop();
            display();
        }
        
        else if (choice == 4)
        {
            display();
        }
        
        else if (choice == 5)
        {
            break;
        }
        
        else 
        {
            printf("Please Enter a abouve option !!");
        }

    }
}


int push(int ele)
{
    if(tos > stacksize)
        printf("\nStack is full");
    else
    {
        tos++;
        stack[tos]=ele;
    }

}

int display()
{
    int i;
    if(tos<0)
        printf("\nstack is empty");
    else
    {
        for(i=tos;i>=0;i--)
            printf("\nElement at position %d is %d",i,stack[i]);
    }
}


int pop()
{
    if(tos<0)
        printf("\nStack is empty");
    else
    {
        printf("\nelement deleted");
        tos--;
    }

}