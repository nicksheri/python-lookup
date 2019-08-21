import ssl
import time
import urllib.request, json 
import click

@click.command()
@click.option('--macaddr', help='MacAdress to lookup', required=True)

def main(macaddr):
    """
    Program  output the Company Name associated with that MAC address in some useful way to the
    user at the command line

    Usage: python look_up.py --macaddr 44:38:39:ff:ef:57
    """
    
    
    context = ssl._create_unverified_context()
    
    api_key = "at_3UvoF20pjcm9GyxZkICUpQFkvuRBz"

    with urllib.request.urlopen(f'https://api.macaddress.io/v1?apiKey={api_key}&output=json&search={macaddr}', context=context) as url:
        data = json.loads(url.read().decode())
        print(data['vendorDetails']['companyName'])
    
if __name__ == '__main__':
    main()