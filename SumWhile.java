import java.util.Scanner;

public class SumWhile {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("1부터 n까지의 합을 구하기");
        System.out.println("n의 값 : ");
        int n = scan.nextInt();

        int sum = 0; //합을 저장하는 변수 sum을 0으로 초기화(루프 본문을 수행하는 동안의 합)
        int i = 1; //반복을 제어하기 위한 변수 i를 1로 초기화(다음에 더하는 값, 최종 i값은 n+1(n초과시 반복문이 종료됨))

        while (i <= n) { //i가 n이하면 반복
            sum += i; //sum에 i를 더합니다.
            i++; //i값을 1만큼 증가시킵니다
        }
        System.out.println("1부터 " + n + "까지의 합은 " + sum + "입니다.");
    }
}
