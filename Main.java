package May_0521;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;



public class Main {
	
	//DB연결
	
	String url = "jdbc:oracle:thin:@localhost:1521:xe";
	String did = "scott";
	String dpw = "tiger";
	
	public static Connection getConnectivity
	(String url, String dbId, String dbPwd) {
		Connection conn = null;
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			conn = DriverManager.getConnection(url, dbId, dbPwd);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return conn;
	}
	
	
	//계좌 정보 DB입력 메소드
	public static void addAccount(Connection conn, PreparedStatement pstmt, Account acc) {
		/*private String accountId; private int pwd;
		  private String name; private int balance=0;*/
		String sql = "insert into account values(?,?,?,?)";
		int result = 0;
		
		try {
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, acc.getAccountId());
			pstmt.setInt(2, acc.getPwd());
			pstmt.setString(3, acc.getName());
			pstmt.setInt(4, acc.getBalance());
			result = pstmt.executeUpdate();
		
		} catch(Exception e) {
			e.printStackTrace();
		}
		System.out.print("계좌 정보 저장 완료");
	}
	
	//입금
	public static void deposit(Connection conn,PreparedStatement pstmt, ResultSet rs ,String accountId, int money) {
		String sql = null;
		int balance = 0;
		try {
		//조회하기
		sql = "select balance from account where accountId=?";
		pstmt = conn.prepareStatement(sql);
		pstmt.setString(1, accountId);
		rs = pstmt.executeQuery();
		rs.next();
		balance = rs.getInt(1);
		
		//수정하기
		sql = "update account set balance=? where accountId=?";
		pstmt = conn.prepareStatement(sql);
		pstmt.setInt(1, balance+money);
		pstmt.setString(2, accountId);
		pstmt.execute();
		}catch(Exception e) {
		e.printStackTrace();
		}System.out.println("입금이 완료되었습니다.");

		}


		public static boolean isCorrect(Connection conn, PreparedStatement pstmt, ResultSet rs,
		String accountId, int pwd) {
		String sql = "select * from account ";
		boolean result = true;
		try {
		pstmt = conn.prepareStatement(sql);
		rs = pstmt.executeQuery();
		while(rs.next()) {
		if(accountId.equals(rs.getString(1))&&pwd!=rs.getInt(2)) {
		System.out.println("비밀번호가 일치하지 않습니다.");
		result = false;
		}else if(accountId.equals(rs.getString(1))&&pwd==rs.getInt(2)) {
		result = true;
				}	
			}
		}catch(Exception e) {	
		e.printStackTrace();
		}
		return result;
		}

		//출금
		public static void withdraw(Connection conn,PreparedStatement pstmt,ResultSet rs , String accountId, int money) {
		String sql = null;
		int balance = 0;
		try {
	
		//조회하기
		sql = "select balance from account where accountId=?";
		pstmt = conn.prepareStatement(sql);
		pstmt.setString(1, accountId);
		rs = pstmt.executeQuery();
		rs.next();
		balance = rs.getInt(1);

		if(balance >= money) {
		sql = "update account set balance=? where accountId=?";
		pstmt = conn.prepareStatement(sql);
		pstmt.setInt(1, balance-money);
		pstmt.setString(2, accountId);
		pstmt.execute();
		System.out.println("출금이 완료되었습니다.");
		}else {

		System.out.println("잔액이 충분하지 않습니다.");

		}
		}catch (Exception e) {
		e.printStackTrace();
		}
		}
		
		//전달
		public static void tranfer(Connection conn,PreparedStatement pstmt, ResultSet rs,
		String accountId, String target ,int money) {
		String sql = null;
		int balance = 0;
		int targetBalance;
		try {
		sql = "select balance from account where accountId=?";
		pstmt = conn.prepareStatement(sql);
		pstmt.setString(1, accountId);
		rs = pstmt.executeQuery();
		rs.next();
		balance = rs.getInt(1);

		if(balance >= money) {
		sql = "select balance from account where accountId=?";
		pstmt = conn.prepareStatement(sql);
		pstmt.setString(1, target);
		rs = pstmt.executeQuery();
		rs.next();
		targetBalance = rs.getInt(1);

		//잔액 추가
		sql = "update account set balance=? where accountId=?";
		pstmt = conn.prepareStatement(sql);
		pstmt.setInt(1, targetBalance+money);
		pstmt.setString(2, target);
		pstmt.execute();

		//잔액 빠짐
		sql = "update account set balance=? where accountId=?";
		pstmt = conn.prepareStatement(sql);
		pstmt.setInt(1, balance-money);
		pstmt.setString(2, accountId);
		pstmt.execute();
		}else {
		System.out.println("잔액이 부족합니다.");
		}
		}catch (Exception e) {
		e.printStackTrace();
		}
		}

		//계좌 금액 조회
		public static int checkBalance(Connection conn, PreparedStatement pstmt, ResultSet rs, String accountId) {
		String sql = null;
		int balance = 0;
		try {
		sql = "select balance from account where accountId=?";
		pstmt = conn.prepareStatement(sql);
		pstmt.setString(1, accountId);
		rs = pstmt.executeQuery();
		rs.next();
		balance = rs.getInt(1);
		}catch (Exception e) {
		e.printStackTrace();
		}
		return balance;
		}

		public static List<Account> getAllAccount(Connection conn, PreparedStatement pstmt, ResultSet rs){
		List<Account> aList = new ArrayList<Account>();
		String sql = "select * from account";
		try {
		pstmt = conn.prepareStatement(sql);
		rs = pstmt.executeQuery();
		while(rs.next()) {
		aList.add(new Account(rs.getString("accountId"), rs.getInt("pwd"),
		  rs.getString("name"), rs.getInt("balance")));
		}
		}catch(Exception e) {
		e.printStackTrace();
		}
		return aList;
		}

		public static void main(String[] args) {
		String url = "jdbc:oracle:thin:@localhost:1521:xe";
		String dbId = "scott";
		String dbPwd = "tiger";

		Scanner scan = new Scanner(System.in);
		int select;
		String accountId = null;;
		ResultSet rs = null;
		PreparedStatement pstmt = null;
		Connection conn = getConnectivity(url, dbId, dbPwd);
		List<Account> aList = null;

		Loop:
		while(true) {
		System.out.println("---------------------------------------------------------------------");
		System.out.println("1.계좌개설 | 2.입금 | 3.출금 | 4.송금 | 5.잔액조회 | 6.전체계좌조회 | 7.프로그램 종료|");
		System.out.println("---------------------------------------------------------------------");
		System.out.print("메뉴를 선택하세요 >>");
		select = scan.nextInt();

		switch(select) {

		case 1://계좌 추가
		System.out.print("계좌번호, 비밀번호, 이름, 최초 입금액을 입력하세요 >> ");
		Account acc = new Account(scan.next(), scan.nextInt(), scan.next(), scan.nextInt());
		addAccount(conn, pstmt, acc);
		break;

		case 2://입금
		System.out.print("계좌번호와 입금액을 입력하세요 >> ");
		deposit(conn, pstmt, rs, scan.next(), scan.nextInt());
		break;

		case 3://출금
		System.out.print("계좌번호와, 비밀번호, 출금액을 입력하세요 >> ");
		accountId = scan.next();
		if(isCorrect(conn, pstmt, rs, accountId, scan.nextInt())) {
		withdraw(conn, pstmt, rs, accountId, scan.nextInt());
		}
		break;

		case 4://송금
		System.out.print("계좌번호, 비밀번호, 송금받을 계좌번호, 송금액을 입력하세요 >> ");
		accountId = scan.next();
		if(isCorrect(conn, pstmt, rs, accountId,scan. nextInt())) {
		tranfer(conn, pstmt, rs, accountId, scan.next(), scan.nextInt());
		}
		break;

		case 5://잔액조회
		System.out.print("계좌번호와 비밀번호를 입력하세요 >> ");
		accountId = scan.next();
		if(isCorrect(conn, pstmt, rs, accountId,scan. nextInt())) {
		int balance = checkBalance(conn, pstmt, rs, accountId);
		System.out.println(accountId + "의 잔액은" + balance +"원 입니다.");
		}
		break;

		case 6://전체 계좌정보 조회
		aList = getAllAccount(conn, pstmt, rs);
		for(Account a : aList) {
		System.out.println(a.toString());
		}
		break;

		case 7://종료
		break Loop;
				}
		
			}

		}
	}
