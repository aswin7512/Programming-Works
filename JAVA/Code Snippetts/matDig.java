import java.lang.*;
import java.util.*;
public class matDig {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter order of Matrix: ");
        int n = sc.nextInt();
        int mat[][] = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.printf("Enter Element A%d%d: ", i, j);
                mat[i][j] = sc.nextInt();
            }
        }
        System.out.print("Diagonal Elements: ");
        for (int i = 0; i < n; i++) {
            System.out.print(mat[i][i]+", ");
        }
    }
}