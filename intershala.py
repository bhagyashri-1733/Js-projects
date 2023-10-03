#include <stdio.h>

int main() {
    int n,m,y,rem,rev=0,temp;
    printf("enter the numbers:");
    scanf("%d ",&n);
    printf("enter the numbers:");
    scanf("%d ",&m);
    y=n+m;
    temp=y;
    while(y!=0)
    {
        rem=y%10;
        rev=rev*10+rem;
        y=y/10;
    }
    if(temp==rev){
        printf("palindrome");
    }
    else{
        printf("not palindrome");
    }
     
    return 0;
}
