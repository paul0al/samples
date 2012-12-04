package sample;

import lombok.Data;
import lombok.NonNull;

@Data
public class User {
	@NonNull private String username;
	private String password;
	private String firstName;
	private String lastName;
	private Address address;
	
	public void debug() {
		System.out.println("Hi");
	}
}
