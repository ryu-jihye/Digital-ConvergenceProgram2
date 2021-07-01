class Max4m {
    static int max(int a, int b, int c, int d) {
        int max = a;
        if (b > max)
            max = b;
        if (c > max)
            max = c;
        if (d > max)
            max = d;

        return max; //구한 최댓값을 호춯한 곳으로 반환3
    }    

    public static void main(String[] args) {
        System.out.println("max(4,3,2,1) = " + max(4, 3, 2, 1));
    }
}
