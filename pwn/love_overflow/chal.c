#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

__attribute__((constructor))
void setup(){
  setvbuf(stdout,NULL,2,0);
  setvbuf(stderr,NULL,2,0);
  setvbuf(stdin,NULL,2,0);
}

char buf[48] = {'a'};
int rolf = 0x69;
int kek = 0x1337;

int main(int argc, char const *argv[]){
    printf("Did you manage to score this valentine?\n\n");
    gets(buf);
    if(kek == 0xdeadbeef && rolf == 0xcafebabe){
        char flag[100];
        int fd = open("flag",O_RDONLY);
        read(fd,flag,100);
        printf("%s\n",flag);
    }
    else{
        printf("LMAO \n\n\n");
    }
    return 0;
}
