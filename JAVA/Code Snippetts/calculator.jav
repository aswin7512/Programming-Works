import java.lang.*;
import java.util.Scanner;
class calculator{
    public static int calculate(int a, char op, int b){
        switch(op){
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a * b;
            case '/': return a / b;
            case '%': return a % b;
            default : return 0;
        }
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("ENTER A NUMBER: ");
        int a = sc.nextInt();
        System.out.print("ENTER AN OPERATOR: ");
        char op = sc.next().charAt(0);
        System.out.print("ENTER A NUMBER:");
        int b = sc.nextInt();
        int result = calculate(a, op, b);
        System.out.printf("%d %c %d = %d", a, op, b, result);
    }
}