#include <stdio.h>
#include <unistd.h>

__attribute__((constructor))
void setup(){
  setvbuf(stdout,NULL,2,0);
  setvbuf(stderr,NULL,2,0);
  setvbuf(stdin,NULL,2,0);
}

struct Simplestruct{
    char buf[40];
    int a;
} input_struct;


int main(int argc, char const *argv[]){
    printf("Can you guess who loves you the most\n\n\n");
    gets(input_struct.buf);
    if(input_struct.a){
        printf("You found love\n\n");
        execl("/bin/sh",0,0);
    }
    else{
        printf("Lol. Nobody loves you :)\n\n");
    }
    return 0;
}
