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


public class Sam{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("ENTER LENGTH: ");
        int l = sc.nextInt();
        System.out.print("ENTER BREADTH: ");
        int b = sc.nextInt();
        Rectangle r = new Rectangle(l, b);
        int a = r.area();
        System.out.println("AREA: "+ a);
        sc.close();
    }
}