import java.lang.*;
public class garbage_collector{
    public void finalize(){
        System.out.println("Object Memory is released!!!");
    }
    public static void main(String[] args){
        garbage_collector t = new garbage_collector();
        t = null;
        System.gc();
    }
}