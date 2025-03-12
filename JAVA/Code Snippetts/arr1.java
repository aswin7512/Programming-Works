//program to print an array
import java.lang.System;
public class arr1{
    public static void main(String[] args){
        int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        System.out.print("ARRAY: ");
        for(int i : arr)
            System.out.printf("%d, ", i);
    }
}