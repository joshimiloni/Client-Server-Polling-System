import socket,pickle,csv
from threading import Thread

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print 'Got connection from', client_address
        addresses[client] = client_address
        handle_client(client)


def handle_client(client): 
        while True:
            try:
                data_string=client.recv(100)
                data_array=pickle.loads(data_string)
                name=data_array[0]
                email=data_array[1]
                response=data_array[2]
                with open('responses.txt','a') as f:
                        f.write(name)
                        f.write(' , ')
                        f.write(email)
                        f.write(' , ')
                        f.write(response)
                        f.write('\n')
                        response=int(response)
                        if response==1:
                                with open('countNPL.txt','r') as m:
                                        h=m.readline(10)
                                        oponecount=int(h)+1
                                        m.close()
                                with open('countNPL.txt','w') as g:
                                        oponecount=str(oponecount)
                                        g.write(oponecount)
                                        g.close()
                        elif response==2:
                                with open('countMCC.txt','r') as n:
                                        j=n.readline(10)
                                        optwocount=int(j)+1
                                        n.close()
                                with open('countMCC.txt','w') as i:
                                        optwocount=str(optwocount)
                                        i.write(optwocount)
                                        i.close()
                        else:
                                with open('countDDB.txt','r') as o:
                                        l=o.readline(10)
                                        opthreecount=int(l)+1
                                        o.close()
                                with open('countDDB.txt','w') as k:
                                        opthreecount=str(opthreecount)
                                        k.write(opthreecount)
                                        k.close()
                txt_file = r"responses.txt"
                csv_file = r"responses.csv"
                in_txt = csv.reader(open(txt_file, "rb"), delimiter = ',')
                out_csv = csv.writer(open(csv_file, 'wb'))
                out_csv.writerows(in_txt)
                file_oponecount=open('countNPL.txt','r')
                file_optwocount=open('countMCC.txt','r')
                file_opthreecount=open('countDDB.txt','r')
                print 'Number of NPL lovers: ',file_oponecount.read()
                print 'Number of MCC lovers: ',file_optwocount.read()
                print 'Number of DDB lovers: ',file_opthreecount.read()
            except Exception as e:
                quit()
clients = {}
addresses = {}

HOST = socket.gethostname()
PORT = 6667
ADDR = (HOST, PORT)

SERVER = socket.socket()
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
