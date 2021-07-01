class Min4 {
    static int min(int a, int b, int c, int d) {
        int min = a;
        if (b > min)
            min = b;
        if (c > min)
            min = c;
        if (d > min)
            min = d;

        return min; //구한 최댓값을 호춯한 곳으로 반환3
    }    

    public static void main(String[] args) {
        System.out.println("min(4,3,2,1) = " + min(4, 3, 2, 1));
    }
}
