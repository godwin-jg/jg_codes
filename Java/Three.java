import java.math.BigInteger;
import java.util.*;
// import math;
class Main{
    public static void main(String[] args){
       /*  Scanner sc = new Scanner(System.in);
        ArrayList<BigInteger> l = new ArrayList<>(Arrays.asList(BigInteger.ZERO,BigInteger.ONE)); 
        int fiboLastDigit = 0;
        int n = 51;
        for(int i=2;i<=n;i++){
            l.add(l.get(i-2).add(l.get(i-1)));
        }
        System.out.println(l.get(n).mod(BigInteger.TEN)); */
        BigInteger base = BigInteger.valueOf(28);
        BigInteger exponent = BigInteger.valueOf(102);
        BigInteger mod = BigInteger.valueOf(221);

        BigInteger result = base.modPow(exponent, mod);
        System.out.println(result);
    }
}