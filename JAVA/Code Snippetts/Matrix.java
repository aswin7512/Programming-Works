//program to input a matrix and print it
import java.util.*;
public class Matrix{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("ENTER NO. OF ROWS: ");
        int m = sc.nextInt();
        System.out.print("ENTER NO. OF COLUMNS: ");
        int n = sc.nextInt();
        System.out.println("ENTER ELEMENTS OF THE MATRIX: ");
        int mat[][] = new int[m][n];
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                System.out.printf("ENTER A%d%d: ", i+1, j+1);
                mat[i][j] = sc.nextInt();
            }
        }
        System.out.println("MATRIX ENTERED IS");
        for(int i[]: mat){
            for(int j: i){
                System.out.printf("%3d", j);
            }
            System.out.println();
        }
        sc.close();
    }
}