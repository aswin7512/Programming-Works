public class hello {
    public static void main(String[] aStrings) {
        Sample s1 = new Sample();
        Sample s2 = new Sample();

        s1.a = 10;
        s2.a = 20;
        s1.b = 30;
        s2.b = 40;

        s1.display();
        s2.display();
    }
}
