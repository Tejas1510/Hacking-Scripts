#include "mainwindow.h"
#include "ui_mainwindow.h"
#include<QString>
#include<QMessageBox>
#include<QFile>
#include<iostream>
using namespace std;
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    //Adding Item to the combo box with suitable Icon
   ui->comboBox->addItem(QIcon(":/src/Img/India.png"),"India");
   ui->comboBox->addItem(QIcon(":/src/Img/Nepal.jpg"),"Nepal");
   ui->comboBox->addItem(QIcon(":/src/Img/bangladesh.png"),"Bangladesh");
   ui->comboBox->addItem(QIcon(":/src/Img/Austriala.png"),"Austriala");
   ui->comboBox->addItem(QIcon(":/src/Img/england.png"),"England");
   ui->comboBox->addItem(QIcon(":/src/Img/Russia.jpg"),"Russia");
   ui->comboBox->addItem(QIcon(":/src/Img/America.png"),"America");
   ui->comboBox->addItem(QIcon(":/src/Img/switzerland.png"),"Switzerland");

}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_2_clicked()
{
    exit(0);
}


void MainWindow::on_pushButton_clicked()
{
    // using int datatype to store index
    int j=0,k=0;
//taking data of lineEdit Widget in QString(datatype used to store string in Qt)
QString firstname= ui->lineEdit->text();
QString lastname= ui->lineEdit_2->text();
QString email=ui->lineEdit_3->text();
QString password=ui->lineEdit_4->text();
//checking whether every line edit and radio button have some value contain or not
if(firstname.size()==0||lastname.size()==0||email.size()==0||password.size()==0||(ui->radioButton->isChecked()==0 && ui->radioButton_2->isChecked()==0)||(ui->radioButton_3->isChecked()==0&&ui->radioButton_4->isChecked()==0))
    QMessageBox::warning(this,"Invalid","Few Information are missing Kindly Provide Them.");
// if data are enter then check whether the email address is correct or not
else{
/* finding @ in the email to read the left character after @ and compare it with domain name file or if @ not found
or the j+1 data == size of email that means Email is Invalid because it didn't contain @*/
    while(email[j]!='@'&&email.size()-1>j){
    j++;
}
if(j+1==email.size()&&email[j]!='@')
    QMessageBox::warning(this,"Alert","Invalid Email Adress \n Hint: Check whether you email contain @");
else{
// create a Qchar domain to contain data of the next index data after @
j++;
QChar domain[20];
while(j<email.size())
{
   domain[k]=email[j];
   j++;
   k++;
}
// now converting QChar domain into QString to compare both the string the user written domain and 2 the store domain in file
QString email_text(domain);
// opening file by providing the location or path
QFile file("E:/Qt in c++/Projects in Qt/Sign_up_app/domain_name.txt");
if(!file.open(QFile::ReadOnly | QFile::Text))
    QMessageBox::warning(this,"Error","File not Found");
else
{

    QString store_data;
    QTextStream in(&file);
    // till end of file didn't came run the loop
    while(!in.atEnd())
    {
       // read every line one by one and then store it in store_data and compare it
        store_data=in.readLine();
        // if compare successful then Accept  and exit else so invalid email address
        if(QString::compare(email_text,store_data,Qt::CaseInsensitive)==0){
            QMessageBox::information(this,"Accept","Sign Up successfully");
        exit(0);
        }
    }
    QMessageBox::warning(this,"Alert","Invalid Email Address \n Hint: Recheck the domain name");
}
}
}
}

