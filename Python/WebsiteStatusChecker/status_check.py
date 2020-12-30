from requests import get

#Enter url of the website you want to check
url = 'https://www.python.abc/'
try:

    response = get(url)
    status = response.status_code
    if(status == 200):
        print('The website ',url,' is up and running')
    elif(status>=400):
        print('The website ',url,' returned error code',status,' and is down')
    elif(status>=500):
        print('The website ',url,' returned error code',status,' and is down')
except:
    print('The website ',url ,'is not available')

#If the response status code is 200 ,that means the website is running ,if not so that means the website is not available