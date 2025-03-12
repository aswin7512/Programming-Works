#include<stdio.h>


int isp(char ch){
	int p;
	switch(ch){
		case '^': p = 6;
			break;
		case '/':
		case '*': p = 5;
			break;
		case '+':
		case '-': p = 3;
			break;
		case '$': p = 0;
			break;
		case '(': p = 1;
			break;
		default: p = -1;
	}
	return p;
}


int icp(char ch){
	int p;
	switch(ch){
		case '^': p = 7;
			break;
		case '/':
		case '*': p = 4;
			break;
		case '+':
		case '-': p = 2;
			break;
		default: p = -1;
	}
}


infix_to_postfix(char in[], char post[]){
	int j = 0, stk[20], top = -1;
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
			else
				while(isp(stk[top]) < icp(in[i]))
					post[j++] = stk[top--];
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
	return 0;
}
