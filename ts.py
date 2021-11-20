import socket
from sys import argv as Arguments
from dns_table import Table, Entry


def start(dns_table, port):
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[TS]: Server socket created\n")
    except socket.error as err:
        print("[TS]: socket open error: {}\n".format(err))
        exit()

    server_binding = ('', port)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[TS]: host is: {}\n".format(host))
    print("[TS]: port is: {}\n".format(port))

    while True:
        csockid, addr = ss.accept()
        print("[TS]: Got a connection request from a client at {}\n".format(addr))

        data_from_client = csockid.recv(256)

        # clean up the message received
        msg_from_client = str(data_from_client.decode('utf-8'))
        msg_from_client = msg_from_client.strip()
        if msg_from_client[-1] == '\n':
            msg_from_client = msg_from_client[: -1]

        print("[TS]: Message: {}\n".format(msg_from_client))

        record_found = dns_table.lookup(msg_from_client)

        if record_found is None:
            print("[TS]: Record not found in DNS table\n")

            msg = "{} - Error:HOST NOT FOUND".format(msg_from_client)
            print("[TS]: Sending '{}' to client\n".format(msg))
            csockid.send(msg.encode('utf-8'))
        else:
            print("[TS]: Record found in DNS table\n")

            msg = record_found.to_string()
            print("[TS]: Sending '{}' to client\n".format(msg))
            csockid.send(msg.encode('utf-8'))

    ss.close()
    print("[TS]: Closed\n")
    exit()


if __name__ == '__main__':
    # check to see if proper number of arguments
    if len(Arguments) != 2:
        print("TS arguments error\n")
        exit()

    # check to see if port is int
    try:
        port = int(Arguments[1])
    except:
        print("Port must be int\n")
        exit()

    # initialize dns table object
    dns_table = Table()

    with open("PROJI-DNSRS.txt") as f:
        lines = f.readlines()

        for line in lines:
            # remove escape chars from end of line
            line = line[: -2]

            # split on space
            input_list = line.split(' ')

            # create entry object
            curr_entry = Entry(input_list[0], input_list[1], input_list[2])

            # add entry to dns_table object
            dns_table.add(curr_entry)

    start(dns_table, port)
