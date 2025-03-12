//program to implement binary search
import java.util.Scanner;
import java.lang.System;
public class binarysearch{
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
        int f = 0, r = n-1, mid;
        boolean found = false;
        mid = (f + r)/2;
        System.out.print("ENTER KEY TO SEARCH: ");
        int key = sc.nextInt();
        while(r >= f){
            if (arr[mid] == key){
                found = true;
                break;
            }
            else if(arr[mid] < key){
                f = mid+1;
            }
            else
                r = mid-1;
            mid = (f + r)/2;
        }
        if(found){
            System.out.printf("%d FOUND", key);
        }
        else{
            System.out.printf("%d NOT FOUND", key);
        }
        sc.close();
    }
}