//program to find the product of 2 matrices
import java.util.*;
public class ProductOfMatrix{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("ENTER NO. OF ROWS(MATRIX 1): ");
        int m1 = sc.nextInt();
        System.out.print("ENTER NO. OF COLUMNS(MATRIX 2): ");
        int n1 = sc.nextInt();
        System.out.print("ENTER NO. OF ROWS(MATRIX 2): ");
        int m2 = sc.nextInt();
        System.out.print("ENTER NO. OF COLUMNS(MATRIX 2): ");
        int n2 = sc.nextInt();
        if(n1 == m2){
            int mat1[][] = new int[m1][n1], mat2[][] = new int[m2][n2], matr[][] = new int[m1][n2];

            System.out.println("\nENTER ELEMENTS OF MATRIX 1");
            for(int i = 0; i < m1; i++){
                for(int j = 0; j < n1; j++){
                    System.out.printf("ENTER A%d%d: ", i+1, j+1);
                    mat1[i][j] = sc.nextInt();
                }
            }

            System.out.println("\nENTER ELEMENTS OF MATRIX 2");
            for(int i = 0; i < m2; i++){
                for(int j = 0; j < n2; j++){
                    System.out.printf("ENTER B%d%d: ", i+1, j+1);
                    mat2[i][j] = sc.nextInt();
                }
            }
            sc.close();
            
            System.out.println("PRODUCT IS");
            for(int i = 0; i < m1; i++){
                for(int j = 0; j < n2; j++){
                    matr[i][j] = 0;
                    for(int k = 0; k < n1; k++){
                        matr[i][j] += mat1[i][k]*mat2[k][j];
                    }
                    System.out.printf("%4d", matr[i][j]);
                }
                System.out.println();
            }
        }
        else
            System.out.println("MATRIX MULTIPLICATION NOT POSSIBLE!!!\n");
    }
}