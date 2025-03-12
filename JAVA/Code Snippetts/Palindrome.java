//program to check whether a string is palindrome or not
import java.util.*;
public class Palindrome{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("ENTER STRING: ");
        String s = sc.nextLine();
        boolean pal = true;
        for(int i = 0, j = s.length()-1; i < (s.length()/2)+1; i++, j--){
            if (s.charAt(i) != s.charAt(j)){
                pal = false;
                break;
            }
        }
        if(pal)
            System.out.println(s + " IS PALINDROME");
        else
            System.out.println(s + " IS NOT PALINDROME");
        sc.close();
    }
}