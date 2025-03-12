//program to input an array and print it
import java.util.Scanner;
import java.lang.System;
public class SumAvg{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); 
        System.out.print("ENTER NO. OF ELEMENTS: ");
        int n = sc.nextInt();
        int arr[] = new int[n];
        System.out.println("ENTER ELEMENTS OF THE ARRAY");
        for(int i = 0; i < n; i++){
            System.out.printf("ENTER ELEMENT %d: ", i+1);
            arr[i] = sc.nextInt();
        }
        int s = 0;
        for(int i : arr)
            s += i;
        int avg = s/arr.length;
        System.out.println("SUM = " + s);
        System.out.println("AVERAGE = " + avg);
        sc.close();
    }
}