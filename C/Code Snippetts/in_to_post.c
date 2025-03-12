#include<stdio.h>
#include<ctype.h>


int isp(char ch){
	switch(ch){
		case '^': return 6;
		case '/':
		case '*': return 5;
		case '+':
		case '-': return 3;
		case '$': return 0;
		case '(': return 1;
		default: return -1;
	}
}


int icp(char ch){
	switch(ch){
		case '^': return 7;
		case '/':
		case '*': return 4;
		case '+':
		case '-': return 2;
		default: return -1;
	}
}


void infix_to_postfix(char in[], char post[]){
	int j = 0, top = -1;
	char stk[20];
	stk[++top] = '$';
	for(int i = 0; in[i] != '\0'; i++){
		if(isdigit(in[i]))
			post[j++] = in[i];
		else if(in[i] == '(')
			stk[++top] = '(';
		else if(in[i] == ')'){
			while(stk[top] != '(')
				post[j++] = stk[top--];
			top--;
		}
		else{
			if(isp(stk[top]) < icp(in[i]))
				stk[++top] = in[i];
			else{
				while(isp(stk[top]) >= icp(in[i]))
					post[j++] = stk[top--];
				stk[++top] = in[i];
			}
		}
	}
	while(stk[top] != '$')
		post[j++] = stk[top--];
	post[j] = '\0';
}


int main(){
	char infix[20], postfix[20];
	printf("ENTER AN INFIX EXPRESSION: ");
	scanf("%[^\n]%*c", infix);
	infix_to_postfix(infix, postfix);
	printf("POSTFIX OF THE GIVEN EXPRESSION: %s\n", postfix);
	return 0;
}