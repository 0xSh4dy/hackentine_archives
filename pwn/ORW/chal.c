#include <fcntl.h>
#include <seccomp.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/prctl.h>
#include <unistd.h>
#include <sys/mman.h>
#include <signal.h>


// ---------- just ignore these functions -------------
void alarm_handler() {
    puts("TIME OUT");
    exit(-1);
}

void init() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    signal(SIGALRM, alarm_handler);
    alarm(40);
}
// this function is used just to make sure that you don't do something like execve('/bin/sh',0, NULL)
void banned_execve() {
  scmp_filter_ctx ctx;
  ctx = seccomp_init(SCMP_ACT_ALLOW);
  if (ctx == NULL) {
    exit(0);
  }
  seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execve), 0);
  seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execveat), 0);

  seccomp_load(ctx);
}
// ----------------------------------------------------------


void main(int argc, char *argv[]) {
  char *shellcode = mmap(NULL, 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);   
  void (*sc)();
  
  init();
  
  banned_execve();
  printf("This challenge doesn't allow you to use execve syscall.\n");
  printf("Use open-read-write shellcode to get the flag.\n");
  printf("shellcode: ");
  read(0, shellcode, 0x1000);

  // Here your shellcode gets executed 
  sc = (void *)shellcode;
  sc();
}