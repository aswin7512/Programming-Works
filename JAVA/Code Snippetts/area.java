//program to implement methord overloading
import java.util.*;


class AreaShape{
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


public class area{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        AreaShape s = new AreaShape();
        System.out.print("ENTER RADIUS: ");
        float cir = s.area(sc.nextFloat());
        System.out.print("ENTER BASE AND HEIGHT OF THE TRIANGLE: ");
        float tri = s.area(sc.nextFloat(), sc.nextFloat());
        System.out.print("ENTER LENGTH AND BREADTH OF RECTANGLE: ");
        int rec = s.area(sc.nextInt(), sc.nextInt());
        System.out.printf("AREA OF CIRCLE: %.2f\n", cir);
        System.out.printf("AREA OF TRIANGLE: %.2f\n", tri);
        System.out.printf("AREA OF RECTANGLE: %d\n", rec);
        sc.close();
    }
}