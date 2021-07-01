import java.util.Scanner;

public class SumFor2 {
    public static void main(String[] args){
    Scanner scan = new Scanner(System.in);

    System.out.println("1부터 n까지의 합 구하기2");
    System.out.print("n의 값 : ");
    int n = scan.nextInt();

    int sum = (n+1) * (n/2);

    if(n%2 != 0) sum += (n+1)/2;

    System.out.println("1부터 " + n + "까지의 합은 " + sum + "입니다.");
    }
}
