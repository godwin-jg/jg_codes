/**
 * Except
 */
public class Except {

    public static void main(String[] args) {
        try {
            int x = 2/0;
        } catch (IndexOutOfBoundsException e) {
            System.out.println(e);
        }catch(ArithmeticException e){
            System.out.println(e);
        }
    }
    
}