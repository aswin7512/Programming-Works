//program to print the transpose of a matrix
import java.util.*;
public class Transpose{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("ENTER NO. OF ROWS: ");
        int m = sc.nextInt();
        System.out.print("ENTER NO. OF COLUMNS: ");
        int n = sc.nextInt();
        int mat[][] = new int[m][n], matt[][] = new int[n][m];
        System.out.println("ENTER ELEMENTS OF THE MATRIX: ");
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                System.out.printf("ENTER A%d%d: ", i+1, j+1);
                mat[i][j] = sc.nextInt();
            }
        }
        sc.close();
        System.out.println("TRANSPOSE IS");
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                matt[i][j] = mat[j][i];
                System.out.printf("%3d", matt[i][j]);
            }
            System.out.println();
        }
    }
}