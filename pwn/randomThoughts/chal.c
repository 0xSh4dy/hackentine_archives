#include <stdio.h>
#include <math.h>
#include <unistd.h>
#include<stdlib.h>

__attribute__((constructor))
void setup(){
  setvbuf(stdout,NULL,2,0);
  setvbuf(stderr,NULL,2,0);
  setvbuf(stdin,NULL,2,0);
}

void win(){
    system("cat /pwn/flag");
}

int main(int argc, char const *argv[]){
    long long int num = 0;
    long long int counter = 1;
    long long int input;
    for (int i = 0; i < 9; i++){
        int x = rand();
        counter *= 10;
        num += (x%10)*counter;
    }

    
    printf("Missing your EX? Lets call him/her. Please enter his/her number\n\n");
    scanf("%lld",&input);
    if(input==num){
        win();
    }
    else{
        printf("Well you have been blocked\nSed\n\n");
    }
}

