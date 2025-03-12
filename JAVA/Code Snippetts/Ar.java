//program to implement methord overloading
import java.util.*;
public class Ar{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        Area shape = new Area();
        System.out.print("ENTER RADIUS: ");
        float r = sc.nextFloat();
        float cir = shape.area(r);
        System.out.print("ENTER BASE AND HEIGHT OF THE TRIANGLE: ");
        float tri_b = sc.nextFloat();
        float tri_h = sc.nextFloat();
        float tri = shape.area(tri_b, tri_h);
        System.out.print("ENTER LENGTH AND BREADTH OF RECTANGLE: ");
        int rec_l = sc.nextInt();
        int rec_b = sc.nextInt();
        int rec = shape.area(rec_l, rec_b);
        System.out.printf("AREA OF CIRCLE: %.2f\n", cir);
        System.out.printf("AREA OF TRIANGLE: %.2f\n", tri);
        System.out.printf("AREA OF RECTANGLE: %d\n", rec);
        sc.close();
    }
}


class Area{
    public float area(float r){
        return 22 / 7 * r * r;
    }


    public int area(int l, int b){
        return l * b;
    }


    public float area(float b, float h){
        return b * h / 2;
    }
}