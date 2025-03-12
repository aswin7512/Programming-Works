import java.util.Scanner;

public class abc {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("ENTER A NUMBER: ");
        int a = s.nextInt();
        int b = s.nextInt();
        System.out.println(a + b);
        s.close();
    }
}