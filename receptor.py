

  import socket
  import numpy as np #esta biblioteca tem funcao que converte string em array


    def rdt_rcv(rcvpkt):
      if rdt_rcv(rcvpkt) && notcorruptrcvpkt) && has_seq0(rcvpkt):
          extract(rcvpkt, data)
          deliver_data(data)
          sndpkt = make_pkt(ACK,0,checksum)
          udt_send(sndpkt)
          oncethru = 1


  def nao_corrupto(rcvpkt):
    
    message = rcvpkt.rsplit(None,1)[-2][1:]
    print "pacote não corrupto"
    checksum_esperado = rcvpkt.rsplit(None,1)[-1]
    
    if (checksum_esperado == ip_checksum(message)):
      return True
        
    print "recebeu um dado corrompido"

  #aqui rcebe um nack e envia o pacote que esta errado
  
    while True:
      #AGORA VAI ESPERAR O ACK OU NACK
      rcvpkt = rdt_rcv()  
      is_corrupt = 	checksum_esperado(rcvpkt)
      is_ack = rcvpkt[2]== True;
      is_nack = rcvpkt[2]== False;
      
      if is_corrupt or is_nack : 
        udt_send(rcvplt) #reenvia o pacote corrompido
      if not is_corrupt and is_ack: 
          break 

    
  seq = 0
  while 1:
      rcvpkt, address = recv_sock.recvfrom(3030)
      if (nao_corrupto(rcvpkt)):
          rdt_send("ACK", seq)
          if (has_seq(rcvpkt, seq)):
              print "Message recebida: "
              print " " + rcvpkt.rsplit(None,1)[-2][1:]
        
              seq = 1 - seq     
          else:
              rdt_send("ACK",1-seq)

  send_sock.close()
  recv_sock.close()
  sys.exit() 








