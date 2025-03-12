import java.io.*;
import java.util.*;

public class file_copy{
	public static void main(String[] args){
		try{
			FileReader fr = new FileReader("file1.txt");
			FileWriter fw = new FileWriter("file2.txt");
			for(int i = fr.read(); i != -1; i = fr.read())
				fw.write(i);
			fr.close();
			fw.close();
		}
		catch(Exception e)
			System.out.println("SOME ERROR OCCURED!!!");
	}
}
