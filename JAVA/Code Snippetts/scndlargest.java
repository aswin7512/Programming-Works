//program to find the second smallest number in an array
import java.util.Scanner;
import java.lang.System;
public class scndlargest{
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
        sc.close();
        int s = Integer.MIN_VALUE, ss = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++){
            if (arr[i] < s){
                ss = s;
                s = arr[i];
            }
            else if (arr[i] < ss && arr[i] != s){
                ss = arr[i];
            }
        }
        if (ss == Integer.MIN_VALUE){
            System.out.println("There is no second largest element.");
        }
        else{
            System.out.println("The second largest element is: " + ss);
        }
    }
}