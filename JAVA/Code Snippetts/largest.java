// program to find largest element of an array
import java.util.Scanner;
import java.lang.System;
public class largest{
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
        int l = arr[0];
        for(int i : arr){
            if(i > l)
                l = i;
        }
        System.out.printf("LARGEST ELEMENT: %d", l);
        sc.close();
    }
}