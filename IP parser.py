import requests
from bs4 import BeautifulSoup

def get_public_ip():
    
    response = requests.get('https://checkip.amazonaws.com/')

    soup = BeautifulSoup(response.text, 'html.parser')

    ip_address = soup.get_text().strip() if soup else None

    return ip_address

def main():
    
    public_ip = get_public_ip()

    if public_ip:
        print("Your public IP address is:", public_ip)
    else:
        print("Failed to retrieve public IP address.")

if __name__ == "__main__":
    main()

