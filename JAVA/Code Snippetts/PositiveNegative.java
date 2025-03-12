import java.util.Scanner;
class PositiveNegative{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("ENTER A NUMBER: ");
        int n = sc.nextInt();

        if (n < 0){
            System.out.printf("%d IS NEGATIVE", n);
        }
        else{
            System.out.printf("%d IS POSITIVE", n);
        }
        sc.close();
    }
}