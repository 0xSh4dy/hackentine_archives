#include<stdio.h>
#include<stdlib.h>

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

void win(){
    puts("You win, the shell is yours!");
    system("/bin/sh");
}
typedef struct chunk* chunkptr;


int main(){
    char* ptr1 = (char*)malloc(0x14);
    char* ptr2 = (char*)malloc(0x26);
    puts("Wanna say something?");
    gets(ptr1);
    chunkptr ptr = (chunkptr)(ptr2-0x10);
    printf("%ld",malloc_usable_size((void*)ptr2));
    if( ptr->fd == 0xcafebabe && ptr->bk == 0xdeadbeef){
        win();
    }
}