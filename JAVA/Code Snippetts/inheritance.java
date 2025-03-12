//PROGRAM TO IMPLEMENT INHERITANCE
import java.util.*;
class Employee{
	String name, address;
	int age, phno;
	double salary;
	Employee(String name, int age, int phno, String address, double salary){
		this.name = name;
		this.age = age;
		this.phno = phno;
		this.address = address;
		this.salary = salary;
	}
	
	
	void print_salary(){
		System.out.println("Salary: " + this.salary);
	}
}


class Manager extends Employee{
	String dept;
	Manager(String name, String address, String dept, int age, int phno, double salary){
		super(name, age, phno, address, salary);
		this.dept = dept;
	}
}


class Officer extends Employee{
	String spec;
	Officer(String name, String address, String spec, int age, int phno, double salary){
		super(name, age, phno, address, salary);
		this.spec = spec;
	}
}


public class inheritance{
	public static void main(String[] args){
		Manager m1 = new Manager("Aswin", "Haripad", "CSE", 22, 1234567890, 5000.25);
		Officer o1 = new Officer("Techy", "Nooranad", "Programming", 19, 1357911123, 500000.25);
		m1.print_salary();
		o1.print_salary();
	}
}
