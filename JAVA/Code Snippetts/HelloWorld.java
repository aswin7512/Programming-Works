import java.lang.System;
import java.util.Scanner;
class HelloWorld{
    public static void main(String[] args){
        int n;
        Scanner sc = new Scanner(System.in);
        System.out.print("ENTER A NUMBER: ");
        n = sc.nextInt();
        sc.close();
        if(n % 2 == 0){
            System.out.println("NUMBER IS EVEN");
        }
        else{
            System.out.println("NUMBER IS ODD");
        }
    }
}