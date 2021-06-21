package Scientific_Calculators;

import java.awt.EventQueue;
import javax.swing.JFrame;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import javax.swing.JTextField;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JButton;
import java.awt.Font;
import javax.swing.JLabel;
import javax.swing.JComboBox;
import javax.swing.SwingConstants;
import javax.swing.JPanel;
import javax.swing.border.LineBorder;
import java.awt.Color;
import javax.swing.DefaultComboBoxModel;

public class ScientificCalculator {

	private JFrame frmStandardCalculator;
	private JTextField txtDisplay;
	private JTextField jtxtConverts;
	private JTextField jlblConverts;
	
	double firstnum;
	double secondnum;
	double result;
	String operations;
	String answer;
	
	double[] i = new double[5];
	double Nigerian_Naira = 5.54;
	double US_Dollar = 0.013;
	double Kenyan_Shilling = 1.45;
	double Brazilian_Real = 0.068;
	double Canadian_Dollar = 0.017;
	double Indian_Rupee = 1.00;
	double Philippine_Peso = 0.66;
	double Indonessia_Rupiah = 194.21;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					ScientificCalculator window = new ScientificCalculator();
					window.frmStandardCalculator.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public ScientificCalculator() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmStandardCalculator = new JFrame();
		frmStandardCalculator.setResizable(false);
		frmStandardCalculator.setTitle("Standard Calculator");
		frmStandardCalculator.setBounds(700, 300, 280, 385);
		frmStandardCalculator.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		JMenuBar menuBar = new JMenuBar();
		frmStandardCalculator.setJMenuBar(menuBar);
		
		JMenu mnFile = new JMenu("File");
		menuBar.add(mnFile);
		
		JMenuItem mntmStandard = new JMenuItem("Standard");
		mntmStandard.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				frmStandardCalculator.setTitle("Standard Calculator");
				frmStandardCalculator.setBounds(700, 300, 280, 385);
				txtDisplay.setBounds(10, 11, 243, 37);
				
			}
		});
		mnFile.add(mntmStandard);
		
		JMenuItem mntmCurrencyConverter = new JMenuItem("Currency Converter");
		mntmCurrencyConverter.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				frmStandardCalculator.setTitle("Currency Converter");
				frmStandardCalculator.setBounds(600, 300, 625, 380);
				txtDisplay.setBounds(10, 11, 243, 37);
			}
		});
		mnFile.add(mntmCurrencyConverter);
		
		JMenuItem mntmExit = new JMenuItem("Exit");
		mntmExit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				System.exit(0);
			}
		});
		mnFile.add(mntmExit);
		frmStandardCalculator.getContentPane().setLayout(null);
		
		txtDisplay = new JTextField();
		txtDisplay.setHorizontalAlignment(SwingConstants.RIGHT);
		txtDisplay.setBounds(10, 11, 243, 37);
		frmStandardCalculator.getContentPane().add(txtDisplay);
		txtDisplay.setColumns(10);
		
		JButton button = new JButton("\u00AB");
		button.setFont(new Font("Tahoma", Font.BOLD, 15));
		button.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
                String backspace = null;
				
				if (txtDisplay.getText().length() >0) {
					StringBuilder strB = new StringBuilder(txtDisplay.getText());
					strB.deleteCharAt(txtDisplay.getText().length() -1);
					backspace = strB.toString();
					txtDisplay.setText(backspace);
				}
			}
		});
		button.setBounds(11, 57, 46, 47);
		frmStandardCalculator.getContentPane().add(button);
		
		JButton button_1 = new JButton("\u0152");
		button_1.setFont(new Font("Tahoma", Font.PLAIN, 11));
		button_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				txtDisplay.setText(null);
			}
		});
		button_1.setBounds(59, 57, 46, 47);
		frmStandardCalculator.getContentPane().add(button_1);
		
		JButton button_2 = new JButton("C");
		button_2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				txtDisplay.setText(null);
			}
		});
		button_2.setFont(new Font("Tahoma", Font.BOLD, 11));
		button_2.setBounds(108, 57, 46, 47);
		frmStandardCalculator.getContentPane().add(button_2);
		
		JButton btnPlusMinus = new JButton("\u00B1");
		btnPlusMinus.setFont(new Font("Tahoma", Font.BOLD, 11));
		btnPlusMinus.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				double ops = Double.parseDouble(String.valueOf(txtDisplay.getText()));
				ops = ops * (-1);
				txtDisplay.setText(String.valueOf(ops));	
			}
		});
		btnPlusMinus.setBounds(156, 57, 46, 47);
		frmStandardCalculator.getContentPane().add(btnPlusMinus);
		
		JButton btnSqrt = new JButton("\u221A");
		btnSqrt.setFont(new Font("Tahoma", Font.BOLD, 11));
		btnSqrt.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				double ops = Double.parseDouble(String.valueOf(txtDisplay.getText()));
				ops = Math.sqrt(ops);
				txtDisplay.setText(String.valueOf(ops));
			}
		});
		btnSqrt.setBounds(205, 57, 46, 47);
		frmStandardCalculator.getContentPane().add(btnSqrt);
		
		JButton btn7 = new JButton("7");
		btn7.setFont(new Font("Tahoma", Font.BOLD, 11));
		btn7.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				String iNum = txtDisplay.getText() +btn7.getText();
				txtDisplay.setText(iNum);
			}
		});
		btn7.setBounds(11, 105, 46, 47);
		frmStandardCalculator.getContentPane().add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				String iNum = txtDisplay.getText() +btn8.getText();
				txtDisplay.setText(iNum);
			}
		});
		btn8.setFont(new Font("Tahoma", Font.BOLD, 11));
		btn8.setBounds(59, 105, 46, 47);
		frmStandardCalculator.getContentPane().add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				String iNum = txtDisplay.getText() +btn9.getText();
				txtDisplay.setText(iNum);
			}
		});
		btn9.setFont(new Font("Tahoma", Font.BOLD, 11));
		btn9.setBounds(108, 105, 46, 47);
		frmStandardCalculator.getContentPane().add(btn9);
		
		JButton btnDiv = new JButton("/");
		btnDiv.setFont(new Font("Tahoma", Font.BOLD, 11));
		btnDiv.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				firstnum = Double.parseDouble(txtDisplay.getText());
				 txtDisplay.setText("");
				 operations = "/";
			}
		});
		btnDiv.setBounds(156, 105, 46, 47);
		frmStandardCalculator.getContentPane().add(btnDiv);
		
		JButton btnRMod = new JButton("%");
		btnRMod.setFont(new Font("Tahoma", Font.PLAIN, 11));
		btnRMod.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				firstnum = Double.parseDouble(txtDisplay.getText());
				 txtDisplay.setText("");
				 operations = "%";
			}
		});
		btnRMod.setBounds(205, 105, 46, 47);
		frmStandardCalculator.getContentPane().add(btnRMod);
		
		JButton btn4 = new JButton("4");
		btn4.setFont(new Font("Tahoma", Font.BOLD, 11));
		btn4.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				String iNum = txtDisplay.getText() +btn4.getText();
				txtDisplay.setText(iNum);
			}
		});
		btn4.setBounds(11, 153, 46, 47);
		frmStandardCalculator.getContentPane().add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				String iNum = txtDisplay.getText() +btn5.getText();
				txtDisplay.setText(iNum);
			}
		});
		btn5.setFont(new Font("Tahoma", Font.BOLD, 11));
		btn5.setBounds(58, 153, 46, 47);
		frmStandardCalculator.getContentPane().add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				String iNum = txtDisplay.getText() +btn6.getText();
				txtDisplay.setText(iNum);
			}
		});
		btn6.setFont(new Font("Tahoma", Font.BOLD, 11));
		btn6.setBounds(107, 153, 46, 47);
		frmStandardCalculator.getContentPane().add(btn6);
		
		JButton btnMul = new JButton("*");
		btnMul.setFont(new Font("Tahoma", Font.BOLD, 11));
		btnMul.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				firstnum = Double.parseDouble(txtDisplay.getText());
				 txtDisplay.setText("");
				 operations = "*";	
			}
		});
		btnMul.setBounds(156, 153, 46, 47);
		frmStandardCalculator.getContentPane().add(btnMul);
		
		JButton btnx2 = new JButton("X^2");
		btnx2.setFont(new Font("Tahoma", Font.PLAIN, 6));
		btnx2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				double ops = Double.parseDouble(String.valueOf(txtDisplay.getText()));
				ops = (ops * ops);
				txtDisplay.setText(String.valueOf(ops));	
				
			}
		});
		btnx2.setBounds(205, 153, 46, 47);
		frmStandardCalculator.getContentPane().add(btnx2);
		
		JButton btn1 = new JButton("1");
		btn1.setFont(new Font("Tahoma", Font.BOLD, 11));
		btn1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			
				String iNum = txtDisplay.getText() +btn1.getText();
				txtDisplay.setText(iNum);
			}
		});
		btn1.setBounds(11, 202, 46, 47);
		frmStandardCalculator.getContentPane().add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				String iNum = txtDisplay.getText() +btn2.getText();
				txtDisplay.setText(iNum);
			}
		});
		btn2.setFont(new Font("Tahoma", Font.BOLD, 11));
		btn2.setBounds(58, 202, 46, 47);
		frmStandardCalculator.getContentPane().add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				String iNum = txtDisplay.getText() +btn3.getText();
				txtDisplay.setText(iNum);
			}
		});
		btn3.setFont(new Font("Tahoma", Font.BOLD, 11));
		btn3.setBounds(107, 202, 46, 47);
		frmStandardCalculator.getContentPane().add(btn3);
		
		JButton btnMinus = new JButton("-");
		btnMinus.setFont(new Font("Tahoma", Font.BOLD, 15));
		btnMinus.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			
				firstnum = Double.parseDouble(txtDisplay.getText());
				 txtDisplay.setText("");
				 operations = "-";
			}
		});
		btnMinus.setBounds(156, 202, 46, 47);
		frmStandardCalculator.getContentPane().add(btnMinus);
		
		JButton btn0 = new JButton("0");
		btn0.setFont(new Font("Tahoma", Font.BOLD, 11));
		btn0.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				String iNum = txtDisplay.getText() +btn0.getText();
				txtDisplay.setText(iNum);
			}
		});
		btn0.setBounds(10, 252, 94, 47);
		frmStandardCalculator.getContentPane().add(btn0);
		
		JButton btnEquals = new JButton("=");
		btnEquals.setFont(new Font("Tahoma", Font.BOLD, 11));
		btnEquals.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				
				String answer;
				secondnum = Double.parseDouble(txtDisplay.getText());
				if (operations == "+")
				{
					result = firstnum + secondnum;
					answer = String.format("%.2f",result);
					txtDisplay.setText(answer);
					
				}
				
				else if (operations == "-")
				{
					result = firstnum - secondnum;
					answer = String.format("%.2f",result);
					txtDisplay.setText(answer);
					
				}
				
				else if (operations == "*")
				{
					result = firstnum * secondnum;
					answer = String.format("%.2f",result);
					txtDisplay.setText(answer);
					
				}
				
				else if (operations == "/")
				{
					result = firstnum / secondnum;
					answer = String.format("%.2f",result);
					txtDisplay.setText(answer);
					
				}	
				
			}
		});
		btnEquals.setBounds(205, 202, 46, 97);
		frmStandardCalculator.getContentPane().add(btnEquals);
		
		JButton btnDot = new JButton(".");
		btnDot.setFont(new Font("Tahoma", Font.BOLD, 11));
		btnDot.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				if(! txtDisplay.getText().contains("."))
				{
					txtDisplay.setText(txtDisplay.getText() + btnDot.getText());
				}
			}
		});
		btnDot.setBounds(108, 252, 46, 47);
		frmStandardCalculator.getContentPane().add(btnDot);
		
		JButton btnPlus = new JButton("+");
		btnPlus.setFont(new Font("Tahoma", Font.BOLD, 11));
		btnPlus.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				firstnum = Double.parseDouble(txtDisplay.getText());
				 txtDisplay.setText("");
				 operations = "+";
			}
		});
		btnPlus.setBounds(156, 252, 46, 47);
		frmStandardCalculator.getContentPane().add(btnPlus);
		
		JLabel lblNewLabel = new JLabel("Convert Indian Currency To");
		lblNewLabel.setFont(new Font("Comic Sans MS", Font.BOLD | Font.ITALIC, 21));
		lblNewLabel.setBounds(296, 22, 298, 37);
		frmStandardCalculator.getContentPane().add(lblNewLabel);
		
		JComboBox jcmbCurrencys = new JComboBox();
		jcmbCurrencys.setFont(new Font("Comic Sans MS", Font.BOLD | Font.ITALIC, 14));
		jcmbCurrencys.setModel(new DefaultComboBoxModel(new String[] {"-Select One Option-", "India", "USA", "Nigeria", "Kenyan", "Canada", "Brazil", "Indonessia", "Philippine"}));
		jcmbCurrencys.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		jcmbCurrencys.setBounds(345, 70, 176, 34);
		frmStandardCalculator.getContentPane().add(jcmbCurrencys);
		
		jtxtConverts = new JTextField();
		jtxtConverts.setHorizontalAlignment(SwingConstants.RIGHT);
		jtxtConverts.setBounds(345, 115, 176, 47);
		frmStandardCalculator.getContentPane().add(jtxtConverts);
		jtxtConverts.setColumns(10);
		
		jlblConverts = new JTextField();
		jlblConverts.setHorizontalAlignment(SwingConstants.RIGHT);
		jlblConverts.setEditable(false);
		jlblConverts.setBounds(345, 181, 176, 47);
		frmStandardCalculator.getContentPane().add(jlblConverts);
		jlblConverts.setColumns(10);
		
		JButton btnConverts = new JButton("Convert");
		btnConverts.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				double Indian_Rupees = Double.parseDouble(jtxtConverts.getText());
				if (jcmbCurrencys.getSelectedItem().equals("Nigeria"))
				{
					String cConvert1 = String.format("N %.2f", Indian_Rupees * Nigerian_Naira);
					jlblConverts.setText(cConvert1);
								
				}
				
				if (jcmbCurrencys.getSelectedItem().equals("USA"))
				{
					String cConvert1 = String.format("$ %.2f", Indian_Rupees * US_Dollar);
					jlblConverts.setText(cConvert1);
								
				}
				
				if (jcmbCurrencys.getSelectedItem().equals("Kenyan"))
				{
					String cConvert2 = String.format("KS %.2f", Indian_Rupees * Kenyan_Shilling);
					jlblConverts.setText(cConvert2);
								
				} 
				
				if (jcmbCurrencys.getSelectedItem().equals("Canada"))
				{
					String cConvert4 = String.format("C$ %.2f", Indian_Rupees * Canadian_Dollar);
					jlblConverts.setText(cConvert4);
								
				} 
				
				if (jcmbCurrencys.getSelectedItem().equals("Brazil"))
				{
					String cConvert5 = String.format("Brz %.2f", Indian_Rupees * Brazilian_Real);
					jlblConverts.setText(cConvert5);
								
				} 
				
				if (jcmbCurrencys.getSelectedItem().equals("India"))
				{
					String cConvert6 = String.format("INR %.2f", Indian_Rupees * Indian_Rupee);
					jlblConverts.setText(cConvert6);
								
				} 
				
				if (jcmbCurrencys.getSelectedItem().equals("Philippine"))
				{
					String cConvert7 = String.format("PHP %.2f", Indian_Rupees * Philippine_Peso);
					jlblConverts.setText(cConvert7);
				
				}  
				
				if (jcmbCurrencys.getSelectedItem().equals("Indonessia"))
				{
					String cConvert8 = String.format("IDR %.2f", Indian_Rupees * Indonessia_Rupiah);
					jlblConverts.setText(cConvert8);
								
				} 

			}
		});
		btnConverts.setFont(new Font("Comic Sans MS", Font.BOLD | Font.ITALIC, 15));
		btnConverts.setBounds(326, 253, 104, 34);
		frmStandardCalculator.getContentPane().add(btnConverts);
		
		
		JButton btnClear = new JButton("Clear");
		btnClear.setFont(new Font("Comic Sans MS", Font.BOLD | Font.ITALIC, 15));
		btnClear.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				jtxtConverts.setText(null);
				jlblConverts.setText(null);
				jcmbCurrencys.setSelectedItem(" -Select One Option-");
				}
		});
		btnClear.setBounds(435, 253, 104, 34);
		frmStandardCalculator.getContentPane().add(btnClear);
		
		JPanel panel = new JPanel();
		panel.setBorder(new LineBorder(new Color(0, 0, 255), 7));
		panel.setBounds(276, 11, 318, 288);
		frmStandardCalculator.getContentPane().add(panel);
	}
}
