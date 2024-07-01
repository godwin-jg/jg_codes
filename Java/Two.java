import java.util.*;

public class Two{
public static void doublehash(int hash[],int num){
    int idx = num % 10;
    if(hash[idx]==0){
        hash[idx] = num;
    }
    else{
        int j = 1;
        while(true){
            int idx2 = (idx + j * (7 - (num%7)) )%10;
            if(hash[idx2]==0){
                hash[idx2] = num;
                break;
            }
            else{
                j++;
            }
        }
    }
    
}
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int hash[] = new int[10];
        for(int i=0;i<n;i++){
            doublehash(hash,sc.nextInt());
        }
        for(int i=0;i<10;i++){
            System.out.println(hash[i]);
        }
    }
}
// Element at position 0: 0
// Element at position 1: 741
// Element at position 2: 852
// Element at position 3: 963
// Element at position 4: 357
// Element at position 5: 159
// Element at position 6: 0
// Element at position 7: 147
// Element at position 8: 258
// Element at position 9: 369