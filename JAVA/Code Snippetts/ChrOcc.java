//program to find the no. of occurences of a character in a string
import java.util.*;
public class ChrOcc{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("ENTER A STRING: ");
        String s = sc.nextLine();
        System.out.print("ENTER CHARACTER TO SEARCH: ");
        char key = sc.next().charAt(0);
        int oc = 0;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == key)
                oc++;
        }
        System.out.println("NO. OF \"" + key + "\" IN \"" + s + "\": " + oc);
        sc.close();
    }
}