abstract class Shape{
	abstract void no_of_sides();
}


class Rectangle extends Shape{
	void no_of_sides(){
		System.out.println("NO OF SIDES: 4");
	}
}


class Triangle extends Shape{
	void no_of_sides(){
		System.out.println("NO OF SIDES: 3");
	}
}


class Hexagon extends Shape{
	void no_of_sides(){
		System.out.println("NO OF SIDES: 6");
	}
}


public class abst{
	public static void main(String[] args){
		Triangle t1 = new Triangle();
		Rectangle r1 = new Rectangle();
		Hexagon h1 = new Hexagon();
		t1.no_of_sides();
		r1.no_of_sides();
		h1.no_of_sides();
	}
}
