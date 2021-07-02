![](img.jpg)
# Convert CSV to Excel using Python (example included)

## In the next section, you’ll see how to apply this template in practice.

## Steps to Convert a CSV to Excel using Python
## Step 1: Install the Pandas package
## If you haven’t already done so, [install the Pandas package.](https://datatofish.com/install-package-python-using-pip/)

**You can use the following command to install the Pandas package (under Windows):**
```
pip install pandas
pip install openpyxl
```
## Step 2: Capture the path where the CSV file is stored

**Next, capture the path where the CSV file is stored on your computer.**

**Here is an example of a path where a CSV file is stored:**
```
C:\Users\Ron\Desktop\Test\test.csv
```
**Where ‘Test’ is the current CSV file name, and ‘csv’ is the file extension.**
## Step 3: Specify the path where the new Excel file will be stored
**Now, you’ll need to specify the path where the new Excel file will be stored. For example:**
```
C:\Users\Ron\Desktop\Test\Test.xlsx
```
**Where ‘test’ is the new file name, and ‘xlsx’ is the Excel file extension.**
## Step 4: Convert the CSV to Excel using Python
**For this final step, you’ll need to use the following template to perform the conversion:**
```
import pandas as pd

read_file = pd.read_csv (r' give the location where the CSV file is stored\File name.csv')
read_file.to_excel (r'give the location to store the Excel file\File name.xlsx', index = None, header=True)
```
# Example
## Before the Execution
![](Before.png)
<hr>

## After the Execution
![](After.png)

