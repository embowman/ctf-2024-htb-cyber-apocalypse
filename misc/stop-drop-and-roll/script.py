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

scenarios_dict = {
    'GORGE': b"STOP",
    'PHREAK': b"DROP",
    'FIRE': b"ROLL"
}

def send_data(scenarios_list):
    actions_list = [scenarios_dict.get(i) for i in scenarios_list]
    try:
        s.send(b"-".join(actions_list) + b"\n")
        print(f"send {b'-'.join(actions_list).decode()}")
    except TimeoutError:
        return
    
for i in range(14):
    msg, send_signal = recv_data()
    print(f"recv {msg}")

    if send_signal:
        s.send(b"y\n")
        print(f"send y")

while True:
    try:
        msg, send_signal = recv_data()
        print(f"recv {msg}")

        if "PHREAK" in msg or "GORGE" in msg or "FIRE" in msg:
            scenarios_list = msg.split(", ")

        if not send_signal:
            continue
        
        send_data(scenarios_list)
    except:
        break

s.close()