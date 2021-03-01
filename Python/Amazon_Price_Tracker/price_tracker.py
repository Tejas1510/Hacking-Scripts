try:
    import requests
    from bs4 import BeautifulSoup
    import smtplib
    import re

except ImportError:
    print('Some modules are not installed! ')
    print("try\t\tpip install requests bs4 smtplib")

global URL


# enable "allow less secured apps" on your gmail for recieving emails
def send_mail(URL, sender_email, password, recievers_email, Price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # The client sends this command to the SMTP server to identify itself and initiate the SMTP conversation.
    server.ehlo()
    server.starttls()  # encrypts the connnection

    server.login(sender_email, password)
    subject = 'Price fell down!'
    body = 'Check the amazon link ' + URL
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(sender_email, recievers_email, msg)

    print('email has been sent')
    server.quit()


def information(soup, URL, sender_email, password, recievers_email, Price):

    title = soup.find(id="productTitle").getText().strip()
    print("\nProduct\t:\n\t", title, "\n")
    # price1 = soup.find(id="priceblock_ourprice").getText()
    price = soup.find(id="priceblock_ourprice").get_text().replace(
        ',', '').replace('₹', '').replace(' ', '').strip()
    print("Current price\t:\t", price)
    # print(price)
    # using regex to convert into float so we can compare with expected price
    #
    print("Price you expect\t:\t", Price)
    if (float(price) < float(Price)):
        print("YEAH price has fallen!! email will be sent")
        send_mail(URL, sender_email, password, recievers_email, Price)
    else:
        print("seems like you have to wait -) ")


def entry():
    # URL = "https://www.amazon.in/ASUS-i9-10980HK-Graphics-Windows-G532LWS-HF079T/dp/B08HX42DGG/ref=sr_1_1?crid=MM0GWK65DAA4&dchild=1&keywords=asus+rog+32gb+ram+laptop&qid=1609939236&sprefix=rog+32gb+ram+%2Caps%2C494&sr=8-1"

    URL = input("[+] paste the url of the amazon product\t>>\t").strip()
    Headers = input(
        "\n[+]just type --my user agent -- in your browser and paste the result \nexampe\n'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36\t>>\t"
    ).strip()
    headers = {"User-Agent": Headers}
    Price1 = input("[+] price you expect\t>>\t").strip()
    sender_email = input(
        "\n[+] An email will be sent from this  account(enable allow secured apps on your account)\t>>\t"
    ).strip()
    password = input("\n[+] your password\t>>\t").strip()
    recievers_email = input(
        "\n[+]  email will be recievedd on this account\t>>\t").strip()
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    Price = Price1.replace(',', '').replace(' ', '').strip()

    # print(soup.prettify)
    try:
        print(
            "# enable --allow less secured apps-- on your gmail if you want to recieve a email"
        )
        information(soup, URL, sender_email, password, recievers_email, Price)
    except AttributeError:
        print("product info not found")


if __name__ == "__main__":
    entry()
