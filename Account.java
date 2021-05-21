package May_0521;

public class Account {
	private String accountId;
	private int pwd;
	private String name;
	private int balance=0;
	
	public Account(String accountId, int pwd, String name, int balance) {
		/* super(); */
		this.accountId = accountId;
		this.pwd = pwd;
		this.name = name;
		this.balance = balance;
	}

	public String getAccountId() {
		return accountId;
	}

	public void setAccountId(String accountId) {
		this.accountId = accountId;
	}

	public int getPwd() {
		return pwd;
	}

	public void setPwd(int pwd) {
		this.pwd = pwd;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getBalance() {
		return balance;
	}

	public void setBalance(int balance) {
		this.balance = balance;
	}
	
	public String toString() {
		return "Account [acoountid=" + accountId + ", pwd=" + pwd 
				+ ", name=" + name + ", balance=" + balance + "]";
	}
	

}
