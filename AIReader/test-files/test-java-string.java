import java.util.*;

public class StringOperations {
    
    public static boolean isPalindrome(String str){
        for (int i=0; i<=str.length()/2; i++){
            int n=str.length();
            if (str.charAt(i)!= str.charAt(n-1-i)){
                return false;
            }
        }
        return true;
    }
    
    public static String compress(String str){
        String newstr="";
        for (int i=0; i<str.length(); i++){
            Integer count=1;
            while(i<str.length()-1 && str.charAt(i)==str.charAt(i+1)){
                count++;
                i++;
            }
            newstr +=str.charAt(i);
            if(count>1){
                newstr +=count.toString();
            }
        }
        return newstr;
    }
    
    public static void main(String[] args) {
        String str="madam";
        System.out.println(isPalindrome(str));
        
        String str2="aaabbcdddddfffff";
        System.out.println(compress(str2));
    }
}
