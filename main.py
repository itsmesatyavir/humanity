import aiohttp
import asyncio

BANNER = """
\033[1;33m=====================================\033[0m
\033[1;33m           F O R E S T A R M Y           \033[0m
\033[1;36m   Join Telegram: t.me/forestarmy   \033[0m
\033[1;33m=====================================\033[0m
"""

async def claim_tokens(address):
    url = 'https://faucet.testnet.humanity.org/api/claim'
    
    payload = {'address': address}
    headers = {
        'Content-Type': 'application/json',
        'Referrer-Policy': 'strict-origin-when-cross-origin',
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=headers) as response:
                print(f"\033[1;36mAddress: {address}\033[0m")
                print("Response Status:", response.status)
                response_data = await response.json()
                print(f"\033[1;32mResponse Data: {response_data}\033[0m")
    except aiohttp.ClientError as error:
        print(f"\033[1;31mError for {address}: {str(error)}\033[0m")

async def auto_claim():
    print(BANNER)
    try:
        with open('wallets.txt', 'r') as file:
            wallets = [line.strip() for line in file if line.strip()]
        
        while True:
            for wallet in wallets:
                await claim_tokens(wallet)
                await asyncio.sleep(10)  # Wait 10 seconds between each request
            await asyncio.sleep(60)  # Wait 60 seconds before starting a new round
    except FileNotFoundError:
        print("\033[1;31mError: wallets.txt not found.\033[0m")

# Run the auto-claim function
asyncio.run(auto_claim())
