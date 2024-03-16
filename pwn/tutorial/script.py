import socket

HOST = ""
PORT = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.settimeout(0.3)

def recv_data():
    buffer = b""
    while True:
        try:
            received = s.recv(1)
                
        except TimeoutError:
            return buffer.decode(), True

        if received == b"\n":
            return buffer.decode(), False
        
        buffer += received

ans_list = [
    b"y\n",
    b"2147483647\n",
    b"-2147483648\n",
    b"-2\n",
    b"Integer Overflow\n",
    b"-2147483648\n",
    b"1337\n"
]

while True:
    msg, send_signal = recv_data()
    print(f"recv {msg}")
    if "HTB{" in msg:
        s.close()
        break

    if send_signal:
        ans = ans_list.pop(0)
        s.send(ans)
        print(f"send {ans.decode()}")