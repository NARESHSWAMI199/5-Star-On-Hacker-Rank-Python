import java.util.*;
class Reverse {
    public static void main(String arg[]){
        System.out.println("enter your value which you want reverse : ");
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        int rev = 0 , remainder;
        while (a != 0){
            remainder = a % 10;
            rev = rev * 10 + remainder;
            a = a/10;
        }
        System.out.println(a);
    }
}