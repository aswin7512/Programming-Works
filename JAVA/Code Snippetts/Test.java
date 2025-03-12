public class Test{
    public void finalize(){
        System.out.println("MEMORY IS RELEASED");
    }
    public static void main(String[] args){
        Test t = new Test();
        t.finalize();
        t = null;
        System.gc();
    }
}