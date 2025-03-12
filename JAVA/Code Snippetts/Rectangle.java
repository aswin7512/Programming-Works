
import java.util.*;


class Rectangle{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("ENTER LENGTH: ");
        int l = sc.nextInt();
        System.out.print("ENTER BREADTH: ");
        int b = sc.nextInt();
        Rectan r = new Rectan(l, b);
        int a = r.area();
        System.out.println("AREA: "+ a);
        sc.close();
    }
}


class Rectan{
    int l, b;
    public Rectan(int l, int b){
        this.l = l;
        this.b = b;
    }


    public int area(){
        return this.l * this.b;
    }
    
}