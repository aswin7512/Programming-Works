class Employee{
	String name, address;          //attribute
	int age, phone_no;
	float salary;
	Employee(String name, int age, int phone_no, String address, float salary){     //constructor
		this.name = name;
		this.age = age;
		this.phone_no = phone_no;
		this.address = address;
		this.salary = salary;
	}


	void print_salary(){              //methord
		System.out.println("Salary of " + this.name + ": " + this.salary);
	}
}


class Manager extends Employee{
	String dept;
	Manager(String name, int age, int phone_no, String address, String dept){
		this.dept = dept;
		super(name, age, phone_no, address, this.cal_sal());
	}
	
	float cal_sal(){
		 return 20000f;
	}
}


class Officer extends Employee{
	
}

