#include <stdio.h>
#include <unistd.h>

__attribute__((constructor))
void setup(){
  setvbuf(stdout,NULL,2,0);
  setvbuf(stderr,NULL,2,0);
  setvbuf(stdin,NULL,2,0);
}

void vuln(){
    char buf[40];
    printf("Have you figured out why you were single this valentine\n\n\n");
    read(0,buf,0x40);
}

void win(){
    execl("/bin/sh",0,0);
}

int main(){
    vuln();
    printf("Well you havent yet figured it out\n\n\n");
    return 0;
}
