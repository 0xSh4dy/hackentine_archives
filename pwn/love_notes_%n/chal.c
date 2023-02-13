#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

__attribute__((constructor))
void setup(){
  setvbuf(stdout,NULL,2,0);
  setvbuf(stderr,NULL,2,0);
  setvbuf(stdin,NULL,2,0);
}

int main(int argc, char const *argv[]){
    char flag[50];
    char secret[100];
    int fd = open("flag",O_RDONLY);
    read(fd,flag,50);
    printf("I have heard that you have a crush on someone.\nTrust me you can tell me his/her name.\nI will keep it a secret.\n");
    fgets(secret,100,stdin);
    printf("Now everyone will know your crush.\n\n");
    printf(secret);
    return 0;
}
