#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int age) {
    int answer = age;
    
    scanf("%d", &answer);
    
    printf("2022년 기준 %d살이므로 %d년생입니다.", 2022-answer+1, answer);
    
    return 2022-answer+1;
}