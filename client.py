from sys import argv as Arguments
import socket
import time

RS_HOSTNAME = ""
RS_PORT = 0
TS_PORT = 0

# TODO: figure out way to close ts and rs
# TODO: test on ilab
# TODO: add a README


def lookup(hostname, port, hostname_to_find):
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    cs.connect((hostname, port))
    cs.send(hostname_to_find.encode('utf-8'))

    data_from_server = cs.recv(256)

    # clean up the message received
    data_from_server = str(data_from_server.decode('utf-8'))
    print("data after decode: ", data_from_server)
    data_from_server = data_from_server.strip()

    if 'Error' in data_from_server:
        cs.close()
        return data_from_server
    else:
        # split on space
        print(data_from_server)
        data_list = data_from_server.split(' ')
        print(data_list)

        if data_list[2] == 'A':
            cs.close()
            return data_from_server
        else:
            return lookup(data_list[0], TS_PORT, hostname_to_find)


if __name__ == '__main__':
    # check to see if proper number of arguments
    if len(Arguments) != 4:
        print("Client arguments error\n")
        exit()

    RS_HOSTNAME = Arguments[1]

    # check to see if ports are ints
    try:
        RS_PORT = int(Arguments[2])
        TS_PORT = int(Arguments[3])
    except:
        print("Port must be int\n")
        exit()

    resolved_list = []

    with open("PROJI-HNS.txt") as f:
        lines = f.readlines()

        for line in lines:
            # remove escape chars from end of line
            if line[-2:] == '\r\n':
                line = line[: -2]

            response = lookup(RS_HOSTNAME, RS_PORT, line)
            resolved_list.append(response)

    # with open('RESOLVED.txt', 'w') as out_file:
    with open('test.txt', 'w') as out_file:
        for entry in resolved_list:
            out_file.write(entry + '\n')
