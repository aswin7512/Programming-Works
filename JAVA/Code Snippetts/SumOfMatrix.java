//program to print the sum of 2 matrices
import java.util.*;
public class SumOfMatrix{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("ENTER NO. OF ROWS: ");
        int m = sc.nextInt();
        System.out.print("ENTER NO. OF COLUMNS: ");
        int n = sc.nextInt();
        int mat1[][] = new int[m][n], mat2[][] = new int[m][n], matr[][] = new int[m][n];

        System.out.println("\nENTER ELEMENTS OF MATRIX 1");
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                System.out.printf("ENTER A%d%d: ", i+1, j+1);
                mat1[i][j] = sc.nextInt();
            }
        }

        System.out.println("\nENTER ELEMENTS OF MATRIX 2");
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                System.out.printf("ENTER B%d%d: ", i+1, j+1);
                mat2[i][j] = sc.nextInt();
            }
        }
        sc.close();
        
        System.out.println("SUM IS IS");
        for(int i = 0;i < m; i++){
            for(int j = 0; j < n; j++){
                matr[i][j] = mat1[i][j] + mat2[i][j];
                System.out.printf("%3d", matr[i][j]);
            }
            System.out.println();
        }
    }
}