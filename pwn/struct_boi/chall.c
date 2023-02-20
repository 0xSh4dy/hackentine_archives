#include<stdio.h>

__attribute__((constructor))
void ignoreMe(){
    setvbuf(stdout,NULL,2,0);
    setvbuf(stdin,NULL,2,0);
    setvbuf(stderr,NULL,2,0);
}

struct chunk{
    size_t chunk_prev_size;
    size_t chunk_size;
    struct chunk* fd;
    struct chunk* bk;
};

typedef struct chunk* chunkptr;


int main(){
    char buff[40];
    puts("Hi there!");
    fgets(buff,40,stdin);
    chunkptr ptr = (chunkptr)buff;
    if(ptr->fd == 0xcafebabe && ptr->bk == 0xdeadbeef){
        system("cat flag.txt");
    }
}