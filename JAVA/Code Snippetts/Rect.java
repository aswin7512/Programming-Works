//program to create class rectangle and print area
import java.util.*;


class Rectangle{
    int l, b;
    public Rectangle(int l, int b){
        this.l = l;
        this.b = b;
    }


    public int area(){
        return this.l * this.b;
    }
    
}


public class Rect{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("ENTER LENGTH AND BREADTH: ");
        Rectangle r = new Rectangle(sc.nextInt(), sc.nextInt());
        int a = r.area();
        System.out.println("AREA: "+ a);
        sc.close();
    }
}