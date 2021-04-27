import socket

transmissor = ('localhost', 2020)
receptor = ('localhost', 3030)

socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #abre socket
socketUDP.bind(transmissor) #da o bind numa porta

next_seq_num = 0 //rdt_send altera esta variavel
#implementação do checksum:
def calculate_checksum(sndpkt):
   soma = 0 
   for valor in sndpkt:
      soma += valor
    return soma 

  def verify_checksum(rcv_pkt): #para verificar se está corrompido
    soma = 0 
    for valor in sndpkt :
       soma += valor 
    return soma == 0xFFF


#recebe como paramentro os dados que vão ser enviados#função chamada pela aplicação
#a unica preocupção aqui é enviar dados, quem chama o rdt send nao precisa saber o que é numero de seuqencia, nem ack nem checksum etc. NADA, APENAS VAI ENVIAR DADOS.
#rdt send vai ter a implementação damaquina de estado

def rdt_send(data): #data = n elementos de 16  bits
    sndpkt = [] #receber um vetor, dentro dele vai colocar
    sndpkt.append(next_seq_num) 
    sndpkt.append(0) #inclui um novo elemento no final do vetor, aumentando a capacidade do mesmo, aqui da append no num de seq inicial
    sndpkt.append(0) #relativo ao checksum
    sndpkt.extend(data) #pega todos os elemntos do vetor e da um append
    sndpkt[1] = calculate_checksum(sndpkt) 
    udt_send(sndpkt) #aqui faz a tramsmissao, envia dados recebidos da aplicação, junto da seq e do ckecksum


  while True:
    #AGORA VAI ESPERAR O ACK OU NACK
     rcvpkt = rdt_rcv() #msg de controle dizenddo se o pacote anterior é reconhecido ou n 
     is_corrupt = verify_checksum(rcvpkt)
     is_ack = rcvpkt[2]== True;
     is_nack = rcvpkt[2]== False;
     
     if is_corrupt or is_nack : 
       udt_send(sndpkt) #reenvia 
     if not is_corrupt and is_ack: 
        break

   if next_seq_num == 0:
     next_seq_num =1
   if next_seq_num == 1:
      next_seq_num = 0
   next_seq_num = 1

def udt_send(packet) :
   socketUDP.sendto(packet, receptor) #envia para o end ip do receptor 
   #a maquina começa em esperar chamdo de cima(0), para sair daqui, alguem tem que chamar o rdt_send;

   #o que fazer quando alguem chamar o rdt_send passando os dados como paramentro? temos que construir um pacote com o número de seuqencia 0, os dados e o checksum
def rdt_rcv(): 
   while True: packet, remetente = socketUDP.recvfrom(10000) # aqui vvai retorna ro pacote e o remetente 
    if remetente != receptor : #vai descartar messnagens que nao seam especidficas do meu receptor 
      return packet

    