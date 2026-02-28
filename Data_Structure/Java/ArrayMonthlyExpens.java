
import java.util.ArrayList;

public class ArrayMonthlyExpens {
    public static void main(String[] args) {
        ArrayList<Integer> monthlyExpens = new ArrayList<>();
        monthlyExpens.add(2200);
        monthlyExpens.add(2350);
        monthlyExpens.add(2600);
        monthlyExpens.add(2310);
        monthlyExpens.add(2190);

        System.out.println("Monthly Expens in each month:");
        for(int i =0;i<monthlyExpens.size();i++){
            System.out.println(i+1+" "+ monthlyExpens.get(i)+" $");
        }

        System.out.println("Here 1.Jan\t2.Feb\t3.March\t4.April\t5.May");
        System.err.println("In February, how many dollars were spent extra compared to January?");
        int ExtraInFeb = monthlyExpens.get(1)-monthlyExpens.get(0);
        System.err.println(ExtraInFeb);
        System.out.println();
        System.out.println("Find out your first 3 months' expenses:");
        int QuarterExpens=0;
        for(int i =0;i<3;i++){
            QuarterExpens+=monthlyExpens.get(i);
        }
        System.out.println(QuarterExpens);
        System.out.println();
        System.out.println("Did you spend exactly 2000 in any month?");
        boolean result =  false;
        for(int i =0;i<monthlyExpens.size();i++){
            if(monthlyExpens.get(i)==2000){
                System.out.println("Yes, in month " + (i + 1));
                result = true;
                break;
            }
        }
        if(!result){
            System.out.println("No");
        }
        System.out.println();
        System.out.println("June month has finished and your expense is $1980. Adding it to the list.");
        monthlyExpens.add(1980);
        System.out.println("Updated Expens "+monthlyExpens);
        System.out.println();
        System.out.println("You returned an item bought in April and got a refund of $200. Making corrections.");
        monthlyExpens.set(3, monthlyExpens.get(3)-200);
        System.out.println("Updated Expens: "+monthlyExpens);

    }
}
