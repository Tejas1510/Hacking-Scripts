// namespace included
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Speech;
using System.Speech.Synthesis;
using System.Globalization;

namespace Text_to_Speech
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // button5_Click= Open Button
        private void button5_Click(object sender, EventArgs e)
        {
            // creating open file dialog box 
            OpenFileDialog filedialog= new OpenFileDialog();
            if (filedialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                // opening file
                if (File.Exists(filedialog.FileName))
                {
                    // reading file and adding it to the richTextBox1 present in the GUI
                    richTextBox1.Text= File.ReadAllText(filedialog.FileName);
                }
            }
        }
        // when form load this function will run
        SpeechSynthesizer speechSynthesizerObj;
        private void Form1_Load(object sender, EventArgs e)
        {
            speechSynthesizerObj = new SpeechSynthesizer();
            comboBox1.SelectedItem = "Male";
            listBox1.SelectedItem = "-1";
          /*  button1.Enabled = false;
            button2.Enabled = false;
            button3.Enabled = false;
            speechSynthesizerObj.SpeakCompleted += new EventHandler<SpeakCompletedEventArgs>(SpeakCompleted);*/
          foreach(var voice in speechSynthesizerObj.GetInstalledVoices())
            {
                comboBox2.Items.Add(voice.VoiceInfo.Name);
            }
        }
        // button4_Click = Speak 
        private void button4_Click(object sender, EventArgs e)
        {
            speechSynthesizerObj.Dispose();
            speechSynthesizerObj = new SpeechSynthesizer();
            if (comboBox1.SelectedItem.ToString() == "Male")
                speechSynthesizerObj.SelectVoiceByHints(VoiceGender.Male);
            else
                speechSynthesizerObj.SelectVoiceByHints(VoiceGender.Female);
            if (listBox1.SelectedItem.ToString() == "-1")
                speechSynthesizerObj.Rate = -1;
            else if (listBox1.SelectedItem.ToString() == "-2")
                speechSynthesizerObj.Rate = -2;
            else if (listBox1.SelectedItem.ToString() == "-3")
                speechSynthesizerObj.Rate = -3;
            else if (listBox1.SelectedItem.ToString() == "-4")
                speechSynthesizerObj.Rate = -4;
            else if (listBox1.SelectedItem.ToString() == "-5")
                speechSynthesizerObj.Rate = -5;
            else if (listBox1.SelectedItem.ToString() == "-6")
                speechSynthesizerObj.Rate = -6;
            else if (listBox1.SelectedItem.ToString() == "-7")
                speechSynthesizerObj.Rate = -7;
            else if (listBox1.SelectedItem.ToString() == "-8")
                speechSynthesizerObj.Rate = -8;
            else if (listBox1.SelectedItem.ToString() == "-9")
                speechSynthesizerObj.Rate = -9;
            else if (listBox1.SelectedItem.ToString() == "-10")
                speechSynthesizerObj.Rate = -10;
            if (richTextBox1.Text!="")
            {
                speechSynthesizerObj.SelectVoice(comboBox2.Text);
                speechSynthesizerObj.SpeakAsync(richTextBox1.Text);
               /* button1.Enabled = true;
                button2.Enabled = true;
                button5.Enabled = false;
                listBox1.Enabled = false;
                button4.Enabled = false;
                comboBox1.Enabled = false;*/
            }
        }
        // button2_Click = Pause
        private void button2_Click(object sender, EventArgs e)
        {
            if(speechSynthesizerObj.State== SynthesizerState.Speaking)
            {
                speechSynthesizerObj.Pause();
            /*    button2.Enabled = false;
                button3.Enabled = true; */
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if(speechSynthesizerObj.State == SynthesizerState.Paused)
            {
                speechSynthesizerObj.Resume();
              /*  button3.Enabled = false;
                button2.Enabled = true;*/
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (speechSynthesizerObj != null)
            {
                speechSynthesizerObj.Dispose();
           /*     button1.Enabled = false;
                button2.Enabled = false;
                button3.Enabled = false;
                button4.Enabled = true;
                button5.Enabled = true;
                listBox1.Enabled = true;
                comboBox1.Enabled = true;*/
            }
        }
    }
}
