#include<stdio.h>

void printFlag(){
	unsigned int buf[] = {68, 71, 94, 92, 70, 91, 92, 87, 105, 116, 102, 98, 77, 35, 97, 77, 113, 125, 125, 126, 77, 115, 35, 124, 37, 77, 123, 102, 45, 111};
	for(int i=0;i<30;i++){
		putchar(buf[i]^18);
	}
}
int main(){
	printFlag();
    return 0;
}
