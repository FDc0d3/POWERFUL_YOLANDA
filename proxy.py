import httpx

http_proxies = [
	"https://proxyspace.pro/http.txt"
]

file_name = "proxy.txt"
with open(file_name, 'w'):
	for proxies in http_proxies:
		if httpx.get(proxies).status_code == 200:
			print(f"[{httpx.get(proxies).status_code}] GET => {proxies}")
			with open(file_name, 'a') as p:
				p.write(httpx.get(proxies).text)
		else:
			print(f"[{httpx.get(proxies).status_code}] ERROR => {proxies}")
	with open(file_name, 'r') as count:
		print(f"[+] Total {file_name.replace('.txt', '')} Proxies: {len(count.readlines())}")
