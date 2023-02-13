#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

__attribute__((constructor))
void setup(){
  setvbuf(stdout,NULL,2,0);
  setvbuf(stderr,NULL,2,0);
  setvbuf(stdin,NULL,2,0);
}

void init_gadget(){
    __asm__(
        ".intel_syntax noprefix;"
        "pop rdi;"
        "ret;"
        "pop rsi;"
        "pop r15;"
        "ret;"
        ".att_syntax;"
    );
}

void win(int a,int b){
    if(a==0xdeadbeef && b == 0xcafebebe){
        printf("Here you go.\n");
        execl("/bin/sh",0,0);
    }
}

int main(){
    char res[] = "Kek";
    char result[] = "Well this was all a scam";
    printf("Heard you have recently broken up.\n\nAre you up for some fun time :)\n\nEnter your name here to enroll\n\n");
    char buf[80];
    gets(buf);
    return 0;
}
