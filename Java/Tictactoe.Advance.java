package in.Tictactoe.Karan;

import java.awt.Color;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.UIManager;

/**
 *
 * @author karan
 */
public class TictactoeGame implements ActionListener
{
    JFrame jf;
    JButton jb1 , jb2 , jb3 , jb4 , jb5 , jb6 , jb7 , jb8 , jb9;
    int count=0;
    String str=""; 
    boolean win=false;
    Color color1;
            
    
     TictactoeGame()
    {
      /*  try
        {
            UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsLookAndFeel");
        }
        catch(Exception e)
                {
                    System.out.println(e);
                }*/
        jf=new JFrame("TicTacToe Game by Karan Gupta ");
        jf.setSize(500,500);
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jf.setLayout(new GridLayout(3, 3));
        
        jb1=new JButton();
        jb1.addActionListener(this);
        jf.add(jb1);
        
         jb2=new JButton();
          jb2.addActionListener(this);
        jf.add(jb2);
        
         jb3=new JButton();
          jb3.addActionListener(this);
        jf.add(jb3);
        
         jb4=new JButton();
          jb4.addActionListener(this);
        jf.add(jb4);
        
         jb5=new JButton();
          jb5.addActionListener(this);
        jf.add(jb5);
        
         jb6=new JButton();
          jb6.addActionListener(this);
        jf.add(jb6);
        
         jb7=new JButton();
          jb7.addActionListener(this);
        jf.add(jb7);
        
         jb8=new JButton();
          jb8.addActionListener(this);
        jf.add(jb8);
        
         jb9=new JButton();
          jb9.addActionListener(this);
        jf.add(jb9);
        
        
        
        
        
        
        jf.setVisible(true);
          
        
    }
   
    public static void main(String[] args)
    {
        new TictactoeGame();
        
    }

    @Override
    public void actionPerformed(ActionEvent e) 
    {
       // throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
       count=count+1;
       if(count%2==0)
       {
           str="o";
           color1=Color.red;
       }
       else
       {
           str="x";
           color1=Color.yellow;
           
       }
        
         if(e.getSource()==jb1)
         {
             jb1.setBackground(color1);
             jb1.setFont(new Font("Arial" , 1,  60));
          jb1.setText(str);
          jb1.setEnabled(false);
          
        }
          if(e.getSource()==jb2)
         {
             jb2.setBackground(color1);
          jb2.setFont(new Font("Arial" , 1,  60));
          jb2.setText(str);
          jb2.setEnabled(false);
        }
           if(e.getSource()==jb3)
         {
             jb3.setBackground(color1);
          jb3.setFont(new Font("Arial" , 1,  60));
          jb3.setText(str);
          jb3.setEnabled(false);
        }
            if(e.getSource()==jb4)
         {
             jb4.setBackground(color1);
          jb4.setFont(new Font("Arial" , 1,  60));
          jb4.setText(str);
          jb4.setEnabled(false);
        }
             if(e.getSource()==jb5)
         {
             jb5.setBackground(color1);
          jb5.setFont(new Font("Arial" , 1,  60));
          jb5.setText(str);
        jb5.setEnabled(false);
         }
              if(e.getSource()==jb6)
         {
             jb6.setBackground(color1);
          jb6.setFont(new Font("Arial" , 1,  60));
          jb6.setText(str);
        jb6.setEnabled(false);
         }
               if(e.getSource()==jb7)
         {
             jb7.setBackground(color1);
          jb7.setFont(new Font("Arial" , 1,  60));
          jb7.setText(str);
        jb7.setEnabled(false);
         }
                if(e.getSource()==jb8)
         {
             jb8.setBackground(color1);
          jb8.setFont(new Font("Arial" , 1,  60));
          jb8.setText(str);
        jb8.setEnabled(false);
         }
                 if(e.getSource()==jb9)
         {
             jb9.setBackground(color1);
          jb9.setFont(new Font("Arial" , 1,  60));
          jb9.setText(str);
        jb9.setEnabled(false); // false lgane se ab sirf ek bar hi click hoga 
         }
         winningPossibilities();
         whoWins();
         
                
 
    }
    void winningPossibilities()
    {
        //here we use trasitive law a==b b==c c==a
        
          //horizontal win process
        if(jb1.getText()==jb2.getText() &&  jb2.getText()==jb3.getText() && jb1.getText() != "")
        {
            //System.out.println(str+" wins");
            //JOptionPane.showMessageDialog(jf,  str+" wins");
            win=true;
        }
        else if(jb4.getText()==jb5.getText() &&  jb5.getText()==jb6.getText() && jb4.getText() != "")
        {
        //JOptionPane.showMessageDialog(jf,  str+" wins");
        win=true;
        }
        else if(jb7.getText()==jb8.getText() &&  jb8.getText()==jb9.getText() && jb7.getText() != "")
        {
            //JOptionPane.showMessageDialog(jf,  str+" wins");
          win=true;
        }
        //vertical win
        else if(jb1.getText()==jb4.getText() &&  jb4.getText()==jb7.getText() && jb7.getText() != "")
        {
            //JOptionPane.showMessageDialog(jf,  str+" wins");
          win=true;
        }
        else if(jb2.getText()==jb5.getText() &&  jb5.getText()==jb8.getText() && jb8.getText() != "")
        {
            //JOptionPane.showMessageDialog(jf,  str+" wins");
          win=true;
        }
        else if(jb3.getText()==jb6.getText() &&  jb6.getText()==jb9.getText() && jb9.getText() != "")
        {
            //JOptionPane.showMessageDialog(jf,  str+" wins");
          win=true;
        }
         //daigonal win 
        else if(jb3.getText()==jb5.getText() &&  jb5.getText()==jb7.getText() && jb7.getText() != "")
        {
           // JOptionPane.showMessageDialog(jf,  str+" wins");
         win=true;
        }
        else if(jb1.getText()==jb5.getText() &&  jb5.getText()==jb9.getText() && jb9.getText() != "")
        {
            //JOptionPane.showMessageDialog(jf,  str+" wins");
        win=true;
        }
         //game draw
        else
        {
           // JOptionPane.showMessageDialog(jf,  "Game Draw");
        win=false;
        }
    }
    void whoWins()
    {
        if(win==true)
        {
            JOptionPane.showMessageDialog(jf, str+" wins");
            restartGame();
        }
        else if(win==false && count==0)
        {
            JOptionPane.showMessageDialog(jf, "Game Draw");
            restartGame();
        }
    }
    void restartGame()
    {
        int i=JOptionPane.showConfirmDialog(jf, "Restart Game");
        if(i==0)
        {
            jb1.setText("");
              jb2.setText("");
              jb3.setText("");
              jb4.setText("");
              jb5.setText("");
              jb6.setText("");
              jb7.setText("");
              jb8.setText("");
              jb9.setText("");
              
              jb1.setBackground(null);
                jb2.setBackground(null);
                  jb3.setBackground(null);
                    jb4.setBackground(null);
                      jb5 .setBackground(null);
                        jb6 .setBackground(null);
                          jb7.setBackground(null);
                            jb8.setBackground(null);
                              jb9.setBackground(null);
                             
                  
              
              
           /*   jb1.setEnabled(true);
                jb2.setEnabled(true);
                  jb3.setEnabled(true);
                    jb4.setEnabled(true);
                      jb5.setEnabled(true);
                        jb6.setEnabled(true);
                          jb7.setEnabled(true);
                            jb8.setEnabled(true);
                              jb9.setEnabled(true);*/
              btnSetEnable(true);
                            
                              str="";
                              count=0;
                              win=false;
                              
        }
        else if(i==1)
        {
            System.exit(0); //it shut down the jvm and game is close
        }
        else
        {
          /*  jb1.setEnabled(false);
                jb2.setEnabled(false);
                  jb3.setEnabled(false);
                    jb4.setEnabled(false);
                      jb5.setEnabled(false);
                        jb6.setEnabled(false);
                          jb7.setEnabled(false);
                            jb8.setEnabled(false);
                              jb9.setEnabled(false);*/
            btnSetEnable(false);
        }
       
    }
    void btnSetEnable(boolean b)
    {
        jb1.setEnabled(b);
        jb2.setEnabled(b);
        jb3.setEnabled(b);
                    jb4.setEnabled(b);
                      jb5.setEnabled(b);
                        jb6.setEnabled(b);
                          jb7.setEnabled(b);
                            jb8.setEnabled(b);
                              jb9.setEnabled(b);
    }
}
