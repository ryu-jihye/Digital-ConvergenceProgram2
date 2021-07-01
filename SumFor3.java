public class SumFor3 {

    public static int sumof(int a, int b){
        int sum = 0;
        int temp;

        if(a>b) {
            temp = a;
            a = b;
            b = temp;
        }

        for(int i=a; i<=b; i++) {
            sum += i;
        }
        
        return sum;
    }
}
