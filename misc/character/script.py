import socket

HOST = ""
PORT = 0

input_list = [str(i).encode() for i in range(104)]
output_list = list()

for i in input_list:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.recv(65)

        s.sendall(i)
        s.shutdown(socket.SHUT_WR)

        c = s.recv(33)
        d = c.decode()
        f = d.split("\n")
        output_list.append(f[0][-1])

print("".join(output_list))