import java.util.*;
import javax.swing.*;
import java.awt.*;
import java.applet.*;
public class Guessing_Game_Human_vs_CPU
{
    static int computerGuess(int lower,int upper,int randnum,int count)
    {
        int guess=(lower+upper)/2;
        if(guess==randnum)
        return count;
        
        if(guess<randnum){
            count++;
            return computerGuess(guess,upper,randnum,count);
          } 
        
        if(guess>randnum){
            count++;
            return computerGuess(lower,guess,randnum,count);
        } 
        return -1;
   }
   
   public static void main(String[] args)
   { 
      int ch=0;  
      while(ch==0)
      {
        int randnum=(int)(Math.random()*100+1);
        int chances=10;
        while(chances>0)  
        {       
         
            String s1=JOptionPane.showInputDialog("Guesss A Number between 1 to 100:");
            int guess=Integer.parseInt(s1);
            if(guess==randnum){
                JOptionPane.showMessageDialog(null,"Congrats you guessed the number !!","GAME JUDGE",JOptionPane.PLAIN_MESSAGE);
                break;
            }
            else if(guess>randnum){
                JOptionPane.showMessageDialog(null,"Your guess is higher than the number.\nGuess Again!!","GAME JUDGE",JOptionPane.PLAIN_MESSAGE);
            }
            else{
                JOptionPane.showMessageDialog(null,"Your guess is lower than the number. \nGuess Again!!","GAME JUDGE",JOptionPane.PLAIN_MESSAGE);
            }
            chances--;
        }

        if(chances!=0){ 
         JOptionPane.showMessageDialog(null,"You guessed the Number in "+(10-chances)+" attempts.\nYou scored "+(chances*10)+" points.","GAME JUDGE",JOptionPane.PLAIN_MESSAGE);
           }
         else{
         JOptionPane.showMessageDialog(null,"You were not able to guess the number in 10 attempts.\nYou scored 0 points.\nBetter Luck next Time","GAME JUDGE",JOptionPane.PLAIN_MESSAGE);
        }
        
        int steps=computerGuess(0,100,randnum,0);
        JOptionPane.showMessageDialog(null,"Computer solved it in "+steps+" attempts.","GAME JUDGE",JOptionPane.PLAIN_MESSAGE);
        
        if((10-chances)<steps)
          JOptionPane.showMessageDialog(null,"You Beat the Computer","GAME JUDGE",JOptionPane.PLAIN_MESSAGE);
          else if((10-chances)>steps)
          JOptionPane.showMessageDialog(null,"You Lost to the Computer","GAME JUDGE",JOptionPane.PLAIN_MESSAGE);
          else
          JOptionPane.showMessageDialog(null,"The Game is a Tie","GAME JUDGE",JOptionPane.PLAIN_MESSAGE);
          
       int s=JOptionPane.showConfirmDialog(null,"Do You want to TRY AGAIN:", "Swing Tester",JOptionPane.YES_NO_OPTION,JOptionPane.QUESTION_MESSAGE);
       ch=s;
      }
      JOptionPane.showMessageDialog(null,"      !!----Thank You for Playing----!!","GAME JUDGE",JOptionPane.PLAIN_MESSAGE);
    
   }
}
