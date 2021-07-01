import java.util.Scanner;

public class SumFor1 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int n = 7;
        int sum = 0;

        for(int i=1; i<=n; i++) {
            if (i != 1) System.out.print("+");
            sum += i;
            System.out.print(i);
            }
            System.out.println("=" + sum);
            }
    }
