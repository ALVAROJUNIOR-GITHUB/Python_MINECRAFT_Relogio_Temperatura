 
import time
import sys

from mcpi.minecraft import Minecraft
from datetime import datetime
from w1thermsensor import W1ThermSensor

mc = Minecraft.create()

sensor = W1ThermSensor()



#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#         POSICAO DO PLAYER
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
mc.player.setTilePos(14.5,37.0,25.5)


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#         POSICAO DA TEMPERATURA
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
T_1 = 0 # POSICAO INICIAL DA TEMPERATURA
T_2 = 0
T_3 = 0
GR  = 0 # POSICAO INICIAL SIMBOLO GRAU
CE  = 0 # POSICAO INICIAL SIMBOLO CELSIUS
PD  = 0 # POSICAO DO PONTO DECIMAL

tempMIN     = 100
tempMAX     = 0
temperature = 0
#............................................


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#         POSICAO DA HORA
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
H_1 = 0 # POSICAO INICIAL DA HORA
H_2 = 0
M_1 = 0 # POSICAO INICIAL DO MINUTO
M_2 = 0
S_1 = 0 # POSICAO INICIAL DO SEGUNDO
S_2 = 0
#............................................


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#         POSICAO DA DATA
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Di_1 = 0 # POSICAO INICIAL DO DIA
Di_2 = 0
Me_1 = 0 # POSICAO INICIAL DO MES
Me_2 = 0
An_1 = 0 # POSICAO INICIAL DO ANO
An_2 = 0
#............................................



MATERIAL = 0



#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#
#                         H O R A
#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

AH = 27 # ALTURA DA HORA

#-------------------------------
# 1o NUMERO HORAS
mc.setBlock(H_1 + 0, AH - 0, 0, 103)
mc.setBlock(H_1 + 0, AH - 1, 0, 103)
mc.setBlock(H_1 + 0, AH - 2, 0, 103)
mc.setBlock(H_1 + 0, AH - 3, 0, 103)
mc.setBlock(H_1 + 0, AH - 4, 0, 103)

mc.setBlock(H_1 + 1, AH - 0, 0, 103)
mc.setBlock(H_1 + 1, AH - 1, 0,   0)
mc.setBlock(H_1 + 1, AH - 2, 0,   0)
mc.setBlock(H_1 + 1, AH - 3, 0,   0)
mc.setBlock(H_1 + 1, AH - 4, 0, 103)

mc.setBlock(H_1 + 2, AH - 0, 0, 103)
mc.setBlock(H_1 + 2, AH - 1, 0, 103)
mc.setBlock(H_1 + 2, AH - 2, 0, 103)
mc.setBlock(H_1 + 2, AH - 3, 0, 103)
mc.setBlock(H_1 + 2, AH - 4, 0, 103)

# 2o NUMERO HORAS
mc.setBlock(H_2 + 4, AH - 0, 0, 103)
mc.setBlock(H_2 + 4, AH - 1, 0, 103)
mc.setBlock(H_2 + 4, AH - 2, 0, 103)
mc.setBlock(H_2 + 4, AH - 3, 0, 103)
mc.setBlock(H_2 + 4, AH - 4, 0, 103)

mc.setBlock(H_2 + 5, AH - 0, 0, 103)
mc.setBlock(H_2 + 5, AH - 1, 0,   0)
mc.setBlock(H_2 + 5, AH - 2, 0,   0)
mc.setBlock(H_2 + 5, AH - 3, 0,   0)
mc.setBlock(H_2 + 5, AH - 4, 0, 103)

mc.setBlock(H_2 + 6, AH - 0, 0, 103)
mc.setBlock(H_2 + 6, AH - 1, 0, 103)
mc.setBlock(H_2 + 6, AH - 2, 0, 103)
mc.setBlock(H_2 + 6, AH - 3, 0, 103)
mc.setBlock(H_2 + 6, AH - 4, 0, 103)
#-------------------------------


# 1o NUMERO MINUTOS
mc.setBlock(M_1 + 10, AH - 0, 0, 103)
mc.setBlock(M_1 + 10, AH - 1, 0, 103)
mc.setBlock(M_1 + 10, AH - 2, 0, 103)
mc.setBlock(M_1 + 10, AH - 3, 0, 103)
mc.setBlock(M_1 + 10, AH - 4, 0, 103)

mc.setBlock(M_1 + 11, AH - 0, 0, 103)
mc.setBlock(M_1 + 11, AH - 1, 0,   0)
mc.setBlock(M_1 + 11, AH - 2, 0,   0)
mc.setBlock(M_1 + 11, AH - 3, 0,   0)
mc.setBlock(M_1 + 11, AH - 4, 0, 103)

mc.setBlock(M_1 + 12, AH - 0, 0, 103)
mc.setBlock(M_1 + 12, AH - 1, 0, 103)
mc.setBlock(M_1 + 12, AH - 2, 0, 103)
mc.setBlock(M_1 + 12, AH - 3, 0, 103)
mc.setBlock(M_1 + 12, AH - 4, 0, 103)

# 2o NUMERO MINUTOS
mc.setBlock(M_2 + 14, AH - 0, 0, 103)
mc.setBlock(M_2 + 14, AH - 1, 0, 103)
mc.setBlock(M_2 + 14, AH - 2, 0, 103)
mc.setBlock(M_2 + 14, AH - 3, 0, 103)
mc.setBlock(M_2 + 14, AH - 4, 0, 103)

mc.setBlock(M_2 + 15, AH - 0, 0, 103)
mc.setBlock(M_2 + 15, AH - 1, 0,   0)
mc.setBlock(M_2 + 15, AH - 2, 0,   0)
mc.setBlock(M_2 + 15, AH - 3, 0,   0)
mc.setBlock(M_2 + 15, AH - 4, 0, 103)

mc.setBlock(M_2 + 16, AH - 0, 0, 103)
mc.setBlock(M_2 + 16, AH - 1, 0, 103)
mc.setBlock(M_2 + 16, AH - 2, 0, 103)
mc.setBlock(M_2 + 16, AH - 3, 0, 103)
mc.setBlock(M_2 + 16, AH - 4, 0, 103)
#--------------------------------

# 1o NUMERO SEGUNDOS
mc.setBlock(S_1 + 20, AH - 0, 0, 103)
mc.setBlock(S_1 + 20, AH - 1, 0, 103)
mc.setBlock(S_1 + 20, AH - 2, 0, 103)
mc.setBlock(S_1 + 20, AH - 3, 0, 103)
mc.setBlock(S_1 + 20, AH - 4, 0, 103)

mc.setBlock(S_1 + 21, AH - 0, 0, 103)
mc.setBlock(S_1 + 21, AH - 1, 0,   0)
mc.setBlock(S_1 + 21, AH - 2, 0,   0)
mc.setBlock(S_1 + 21, AH - 3, 0,   0)
mc.setBlock(S_1 + 21, AH - 4, 0, 103)

mc.setBlock(S_1 + 22, AH - 0, 0, 103)
mc.setBlock(S_1 + 22, AH - 1, 0, 103)
mc.setBlock(S_1 + 22, AH - 2, 0, 103)
mc.setBlock(S_1 + 22, AH - 3, 0, 103)
mc.setBlock(S_1 + 22, AH - 4, 0, 103)

# 2o NUMERO SEGUNDOS
mc.setBlock(S_2 + 24, AH - 0, 0, 103)
mc.setBlock(S_2 + 24, AH - 1, 0, 103)
mc.setBlock(S_2 + 24, AH - 2, 0, 103)
mc.setBlock(S_2 + 24, AH - 3, 0, 103)
mc.setBlock(S_2 + 24, AH - 4, 0, 103)

mc.setBlock(S_2 + 25, AH - 0, 0, 103)
mc.setBlock(S_2 + 25, AH - 1, 0,   0)
mc.setBlock(S_2 + 25, AH - 2, 0,   0)
mc.setBlock(S_2 + 25, AH - 3, 0,   0)
mc.setBlock(S_2 + 25, AH - 4, 0, 103)

mc.setBlock(S_2 + 26, AH - 0, 0, 103)
mc.setBlock(S_2 + 26, AH - 1, 0, 103)
mc.setBlock(S_2 + 26, AH - 2, 0, 103)
mc.setBlock(S_2 + 26, AH - 3, 0, 103)
mc.setBlock(S_2 + 26, AH - 4, 0, 103)
#--------------------------------

# DOIS PONTOS ':'
mc.setBlock(S_1 + 8,  AH - 1, 0, 103)
mc.setBlock(S_1 + 8,  AH - 3, 0, 103)

mc.setBlock(S_1 + 18, AH - 1, 0, 103)
mc.setBlock(S_1 + 18, AH - 3, 0, 103)



#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#
#                         D A T A
#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

AD = 33 # ALTURA DA DATA

#-------------------------------
# 1o NUMERO DIA
mc.setBlock(Di_1 + 0, AD - 0, 0, 103)
mc.setBlock(Di_1 + 0, AD - 1, 0, 103)
mc.setBlock(Di_1 + 0, AD - 2, 0, 103)
mc.setBlock(Di_1 + 0, AD - 3, 0, 103)
mc.setBlock(Di_1 + 0, AD - 4, 0, 103)

mc.setBlock(Di_1 + 1, AD - 0, 0, 103)
mc.setBlock(Di_1 + 1, AD - 1, 0,   0)
mc.setBlock(Di_1 + 1, AD - 2, 0,   0)
mc.setBlock(Di_1 + 1, AD - 3, 0,   0)
mc.setBlock(Di_1 + 1, AD - 4, 0, 103)

mc.setBlock(Di_1 + 2, AD - 0, 0, 103)
mc.setBlock(Di_1 + 2, AD - 1, 0, 103)
mc.setBlock(Di_1 + 2, AD - 2, 0, 103)
mc.setBlock(Di_1 + 2, AD - 3, 0, 103)
mc.setBlock(Di_1 + 2, AD - 4, 0, 103)

# 2o NUMERO DIA
mc.setBlock(Di_2 + 4, AD - 0, 0, 103)
mc.setBlock(Di_2 + 4, AD - 1, 0, 103)
mc.setBlock(Di_2 + 4, AD - 2, 0, 103)
mc.setBlock(Di_2 + 4, AD - 3, 0, 103)
mc.setBlock(Di_2 + 4, AD - 4, 0, 103)

mc.setBlock(Di_2 + 5, AD - 0, 0, 103)
mc.setBlock(Di_2 + 5, AD - 1, 0,   0)
mc.setBlock(Di_2 + 5, AD - 2, 0,   0)
mc.setBlock(Di_2 + 5, AD - 3, 0,   0)
mc.setBlock(Di_2 + 5, AD - 4, 0, 103)

mc.setBlock(Di_2 + 6, AD - 0, 0, 103)
mc.setBlock(Di_2 + 6, AD - 1, 0, 103)
mc.setBlock(Di_2 + 6, AD - 2, 0, 103)
mc.setBlock(Di_2 + 6, AD - 3, 0, 103)
mc.setBlock(Di_2 + 6, AD - 4, 0, 103)
#-------------------------------


# 1o NUMERO MES
mc.setBlock(Me_1 + 10, AD - 0, 0, 103)
mc.setBlock(Me_1 + 10, AD - 1, 0, 103)
mc.setBlock(Me_1 + 10, AD - 2, 0, 103)
mc.setBlock(Me_1 + 10, AD - 3, 0, 103)
mc.setBlock(Me_1 + 10, AD - 4, 0, 103)

mc.setBlock(Me_1 + 11, AD - 0, 0, 103)
mc.setBlock(Me_1 + 11, AD - 1, 0,   0)
mc.setBlock(Me_1 + 11, AD - 2, 0,   0)
mc.setBlock(Me_1 + 11, AD - 3, 0,   0)
mc.setBlock(Me_1 + 11, AD - 4, 0, 103)

mc.setBlock(Me_1 + 12, AD - 0, 0, 103)
mc.setBlock(Me_1 + 12, AD - 1, 0, 103)
mc.setBlock(Me_1 + 12, AD - 2, 0, 103)
mc.setBlock(Me_1 + 12, AD - 3, 0, 103)
mc.setBlock(Me_1 + 12, AD - 4, 0, 103)

# 2o NUMERO MES
mc.setBlock(Me_2 + 14, AD - 0, 0, 103)
mc.setBlock(Me_2 + 14, AD - 1, 0, 103)
mc.setBlock(Me_2 + 14, AD - 2, 0, 103)
mc.setBlock(Me_2 + 14, AD - 3, 0, 103)
mc.setBlock(Me_2 + 14, AD - 4, 0, 103)

mc.setBlock(Me_2 + 15, AD - 0, 0, 103)
mc.setBlock(Me_2 + 15, AD - 1, 0,   0)
mc.setBlock(Me_2 + 15, AD - 2, 0,   0)
mc.setBlock(Me_2 + 15, AD - 3, 0,   0)
mc.setBlock(Me_2 + 15, AD - 4, 0, 103)

mc.setBlock(Me_2 + 16, AD - 0, 0, 103)
mc.setBlock(Me_2 + 16, AD - 1, 0, 103)
mc.setBlock(Me_2 + 16, AD - 2, 0, 103)
mc.setBlock(Me_2 + 16, AD - 3, 0, 103)
mc.setBlock(Me_2 + 16, AD - 4, 0, 103)
#--------------------------------

# 1o NUMERO ANO
mc.setBlock(An_1 + 20, AD - 0, 0, 103)
mc.setBlock(An_1 + 20, AD - 1, 0, 103)
mc.setBlock(An_1 + 20, AD - 2, 0, 103)
mc.setBlock(An_1 + 20, AD - 3, 0, 103)
mc.setBlock(An_1 + 20, AD - 4, 0, 103)

mc.setBlock(An_1 + 21, AD - 0, 0, 103)
mc.setBlock(An_1 + 21, AD - 1, 0,   0)
mc.setBlock(An_1 + 21, AD - 2, 0,   0)
mc.setBlock(An_1 + 21, AD - 3, 0,   0)
mc.setBlock(An_1 + 21, AD - 4, 0, 103)

mc.setBlock(An_1 + 22, AD - 0, 0, 103)
mc.setBlock(An_1 + 22, AD - 1, 0, 103)
mc.setBlock(An_1 + 22, AD - 2, 0, 103)
mc.setBlock(An_1 + 22, AD - 3, 0, 103)
mc.setBlock(An_1 + 22, AD - 4, 0, 103)

# 2o NUMERO ANO
mc.setBlock(An_2 + 24, AD - 0, 0, 103)
mc.setBlock(An_2 + 24, AD - 1, 0, 103)
mc.setBlock(An_2 + 24, AD - 2, 0, 103)
mc.setBlock(An_2 + 24, AD - 3, 0, 103)
mc.setBlock(An_2 + 24, AD - 4, 0, 103)

mc.setBlock(An_2 + 25, AD - 0, 0, 103)
mc.setBlock(An_2 + 25, AD - 1, 0,   0)
mc.setBlock(An_2 + 25, AD - 2, 0,   0)
mc.setBlock(An_2 + 25, AD - 3, 0,   0)
mc.setBlock(An_2 + 25, AD - 4, 0, 103)

mc.setBlock(An_2 + 26, AD - 0, 0, 103)
mc.setBlock(An_2 + 26, AD - 1, 0, 103)
mc.setBlock(An_2 + 26, AD - 2, 0, 103)
mc.setBlock(An_2 + 26, AD - 3, 0, 103)
mc.setBlock(An_2 + 26, AD - 4, 0, 103)
#--------------------------------

# PONTO '.'
mc.setBlock(An_1 + 8,  AD - 2, 0, 103)
mc.setBlock(An_1 + 18, AD - 2, 0, 103)




#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#
#            T E M P E R A T U R A    A T U A L
#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

AT = 54  # ALTURA DA TEMPERATURA

#-------------------------------
# 1o NUMERO TEMPERATURA
mc.setBlock(T_1 + 0, AT - 0, 0, 103)
mc.setBlock(T_1 + 0, AT - 1, 0, 103)
mc.setBlock(T_1 + 0, AT - 2, 0, 103)
mc.setBlock(T_1 + 0, AT - 3, 0, 103)
mc.setBlock(T_1 + 0, AT - 4, 0, 103)

mc.setBlock(T_1 + 1, AT - 0, 0, 103)
mc.setBlock(T_1 + 1, AT - 1, 0,   0)
mc.setBlock(T_1 + 1, AT - 2, 0,   0)
mc.setBlock(T_1 + 1, AT - 3, 0,   0)
mc.setBlock(T_1 + 1, AT - 4, 0, 103)

mc.setBlock(T_1 + 2, AT - 0, 0, 103)
mc.setBlock(T_1 + 2, AT - 1, 0, 103)
mc.setBlock(T_1 + 2, AT - 2, 0, 103)
mc.setBlock(T_1 + 2, AT - 3, 0, 103)
mc.setBlock(T_1 + 2, AT - 4, 0, 103)

# 2o NUMERO TEMPERATURA
mc.setBlock(T_2 + 4, AT - 0, 0, 103)
mc.setBlock(T_2 + 4, AT - 1, 0, 103)
mc.setBlock(T_2 + 4, AT - 2, 0, 103)
mc.setBlock(T_2 + 4, AT - 3, 0, 103)
mc.setBlock(T_2 + 4, AT - 4, 0, 103)

mc.setBlock(T_2 + 5, AT - 0, 0, 103)
mc.setBlock(T_2 + 5, AT - 1, 0,   0)
mc.setBlock(T_2 + 5, AT - 2, 0,   0)
mc.setBlock(T_2 + 5, AT - 3, 0,   0)
mc.setBlock(T_2 + 5, AT - 4, 0, 103)

mc.setBlock(T_2 + 6, AT - 0, 0, 103)
mc.setBlock(T_2 + 6, AT - 1, 0, 103)
mc.setBlock(T_2 + 6, AT - 2, 0, 103)
mc.setBlock(T_2 + 6, AT - 3, 0, 103)
mc.setBlock(T_2 + 6, AT - 4, 0, 103)

# 3o NUMERO TEMPERATURA
mc.setBlock(T_3 + 10, AT - 0, 0, 103)
mc.setBlock(T_3 + 10, AT - 1, 0, 103)
mc.setBlock(T_3 + 10, AT - 2, 0, 103)
mc.setBlock(T_3 + 10, AT - 3, 0, 103)
mc.setBlock(T_3 + 10, AT - 4, 0, 103)

mc.setBlock(T_3 + 11, AT - 0, 0, 103)
mc.setBlock(T_3 + 11, AT - 1, 0,   0)
mc.setBlock(T_3 + 11, AT - 2, 0,   0)
mc.setBlock(T_3 + 11, AT - 3, 0,   0)
mc.setBlock(T_3 + 11, AT - 4, 0, 103)

mc.setBlock(T_3 + 12, AT - 0, 0, 103)
mc.setBlock(T_3 + 12, AT - 1, 0, 103)
mc.setBlock(T_3 + 12, AT - 2, 0, 103)
mc.setBlock(T_3 + 12, AT - 3, 0, 103)
mc.setBlock(T_3 + 12, AT - 4, 0, 103)

# 4o SIMBOLO DO GRAU 
mc.setBlock(GR + 14, AT - 0, 0, 103)
mc.setBlock(GR + 14, AT - 1, 0, 103)
mc.setBlock(GR + 14, AT - 2, 0, 103)
mc.setBlock(GR + 14, AT - 3, 0,   0)
mc.setBlock(GR + 14, AT - 4, 0,   0)

mc.setBlock(GR + 15, AT - 0, 0, 103)
mc.setBlock(GR + 15, AT - 1, 0,   0)
mc.setBlock(GR + 15, AT - 2, 0, 103)
mc.setBlock(GR + 15, AT - 3, 0,   0)
mc.setBlock(GR + 15, AT - 4, 0,   0)

mc.setBlock(GR + 16, AT - 0, 0, 103)
mc.setBlock(GR + 16, AT - 1, 0, 103)
mc.setBlock(GR + 16, AT - 2, 0, 103)
mc.setBlock(GR + 16, AT - 3, 0,   0)
mc.setBlock(GR + 16, AT - 4, 0,   0)

# 5o SIMBOLO DO CELSIUS
mc.setBlock(CE + 18, AT - 0, 0, 103)
mc.setBlock(CE + 18, AT - 1, 0, 103)
mc.setBlock(CE + 18, AT - 2, 0, 103)
mc.setBlock(CE + 18, AT - 3, 0, 103)
mc.setBlock(CE + 18, AT - 4, 0, 103) 

mc.setBlock(CE + 19, AT - 0, 0, 103)
mc.setBlock(CE + 19, AT - 1, 0,   0)
mc.setBlock(CE + 19, AT - 2, 0,   0)
mc.setBlock(CE + 19, AT - 3, 0,   0)
mc.setBlock(CE + 19, AT - 4, 0, 103)

mc.setBlock(CE + 20, AT - 0, 0, 103)
mc.setBlock(CE + 20, AT - 1, 0,   0)
mc.setBlock(CE + 20, AT - 2, 0,   0)
mc.setBlock(CE + 20, AT - 3, 0,   0)
mc.setBlock(CE + 20, AT - 4, 0, 103)
#-------------------------------

# PONTO '.'
mc.setBlock(PD + 8,  AT - 4, 0, 103)



#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#
#           T E M P E R A T U R A    M A X I M A 
#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

AT = 48  # ALTURA DA TEMPERATURA

#-------------------------------
# 1o NUMERO TEMPERATURA
mc.setBlock(T_1 + 0, AT - 0, 0, 103)
mc.setBlock(T_1 + 0, AT - 1, 0, 103)
mc.setBlock(T_1 + 0, AT - 2, 0, 103)
mc.setBlock(T_1 + 0, AT - 3, 0, 103)
mc.setBlock(T_1 + 0, AT - 4, 0, 103)

mc.setBlock(T_1 + 1, AT - 0, 0, 103)
mc.setBlock(T_1 + 1, AT - 1, 0,   0)
mc.setBlock(T_1 + 1, AT - 2, 0,   0)
mc.setBlock(T_1 + 1, AT - 3, 0,   0)
mc.setBlock(T_1 + 1, AT - 4, 0, 103)

mc.setBlock(T_1 + 2, AT - 0, 0, 103)
mc.setBlock(T_1 + 2, AT - 1, 0, 103)
mc.setBlock(T_1 + 2, AT - 2, 0, 103)
mc.setBlock(T_1 + 2, AT - 3, 0, 103)
mc.setBlock(T_1 + 2, AT - 4, 0, 103)

# 2o NUMERO TEMPERATURA
mc.setBlock(T_2 + 4, AT - 0, 0, 103)
mc.setBlock(T_2 + 4, AT - 1, 0, 103)
mc.setBlock(T_2 + 4, AT - 2, 0, 103)
mc.setBlock(T_2 + 4, AT - 3, 0, 103)
mc.setBlock(T_2 + 4, AT - 4, 0, 103)

mc.setBlock(T_2 + 5, AT - 0, 0, 103)
mc.setBlock(T_2 + 5, AT - 1, 0,   0)
mc.setBlock(T_2 + 5, AT - 2, 0,   0)
mc.setBlock(T_2 + 5, AT - 3, 0,   0)
mc.setBlock(T_2 + 5, AT - 4, 0, 103)

mc.setBlock(T_2 + 6, AT - 0, 0, 103)
mc.setBlock(T_2 + 6, AT - 1, 0, 103)
mc.setBlock(T_2 + 6, AT - 2, 0, 103)
mc.setBlock(T_2 + 6, AT - 3, 0, 103)
mc.setBlock(T_2 + 6, AT - 4, 0, 103)

# 3o NUMERO TEMPERATURA
mc.setBlock(T_3 + 10, AT - 0, 0, 103)
mc.setBlock(T_3 + 10, AT - 1, 0, 103)
mc.setBlock(T_3 + 10, AT - 2, 0, 103)
mc.setBlock(T_3 + 10, AT - 3, 0, 103)
mc.setBlock(T_3 + 10, AT - 4, 0, 103)

mc.setBlock(T_3 + 11, AT - 0, 0, 103)
mc.setBlock(T_3 + 11, AT - 1, 0,   0)
mc.setBlock(T_3 + 11, AT - 2, 0,   0)
mc.setBlock(T_3 + 11, AT - 3, 0,   0)
mc.setBlock(T_3 + 11, AT - 4, 0, 103)

mc.setBlock(T_3 + 12, AT - 0, 0, 103)
mc.setBlock(T_3 + 12, AT - 1, 0, 103)
mc.setBlock(T_3 + 12, AT - 2, 0, 103)
mc.setBlock(T_3 + 12, AT - 3, 0, 103)
mc.setBlock(T_3 + 12, AT - 4, 0, 103)

# 4o SIMBOLO DO GRAU 
mc.setBlock(GR + 14, AT - 0, 0, 103)
mc.setBlock(GR + 14, AT - 1, 0, 103)
mc.setBlock(GR + 14, AT - 2, 0, 103)
mc.setBlock(GR + 14, AT - 3, 0,   0)
mc.setBlock(GR + 14, AT - 4, 0,   0)

mc.setBlock(GR + 15, AT - 0, 0, 103)
mc.setBlock(GR + 15, AT - 1, 0,   0)
mc.setBlock(GR + 15, AT - 2, 0, 103)
mc.setBlock(GR + 15, AT - 3, 0,   0)
mc.setBlock(GR + 15, AT - 4, 0,   0)

mc.setBlock(GR + 16, AT - 0, 0, 103)
mc.setBlock(GR + 16, AT - 1, 0, 103)
mc.setBlock(GR + 16, AT - 2, 0, 103)
mc.setBlock(GR + 16, AT - 3, 0,   0)
mc.setBlock(GR + 16, AT - 4, 0,   0)

# 5o SIMBOLO DO CELSIUS
mc.setBlock(CE + 18, AT - 0, 0, 103)
mc.setBlock(CE + 18, AT - 1, 0, 103)
mc.setBlock(CE + 18, AT - 2, 0, 103)
mc.setBlock(CE + 18, AT - 3, 0, 103)
mc.setBlock(CE + 18, AT - 4, 0, 103) 

mc.setBlock(CE + 19, AT - 0, 0, 103)
mc.setBlock(CE + 19, AT - 1, 0,   0)
mc.setBlock(CE + 19, AT - 2, 0,   0)
mc.setBlock(CE + 19, AT - 3, 0,   0)
mc.setBlock(CE + 19, AT - 4, 0, 103)

mc.setBlock(CE + 20, AT - 0, 0, 103)
mc.setBlock(CE + 20, AT - 1, 0,   0)
mc.setBlock(CE + 20, AT - 2, 0,   0)
mc.setBlock(CE + 20, AT - 3, 0,   0)
mc.setBlock(CE + 20, AT - 4, 0, 103)
#-------------------------------

# PONTO '.'
mc.setBlock(PD + 8,  AT - 4, 0, 103)


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#
#            T E M P E R A T U R A    M I N I M A
#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

AT = 42  # ALTURA DA TEMPERATURA

#-------------------------------
# 1o NUMERO TEMPERATURA
mc.setBlock(T_1 + 0, AT - 0, 0, 103)
mc.setBlock(T_1 + 0, AT - 1, 0, 103)
mc.setBlock(T_1 + 0, AT - 2, 0, 103)
mc.setBlock(T_1 + 0, AT - 3, 0, 103)
mc.setBlock(T_1 + 0, AT - 4, 0, 103)

mc.setBlock(T_1 + 1, AT - 0, 0, 103)
mc.setBlock(T_1 + 1, AT - 1, 0,   0)
mc.setBlock(T_1 + 1, AT - 2, 0,   0)
mc.setBlock(T_1 + 1, AT - 3, 0,   0)
mc.setBlock(T_1 + 1, AT - 4, 0, 103)

mc.setBlock(T_1 + 2, AT - 0, 0, 103)
mc.setBlock(T_1 + 2, AT - 1, 0, 103)
mc.setBlock(T_1 + 2, AT - 2, 0, 103)
mc.setBlock(T_1 + 2, AT - 3, 0, 103)
mc.setBlock(T_1 + 2, AT - 4, 0, 103)

# 2o NUMERO TEMPERATURA
mc.setBlock(T_2 + 4, AT - 0, 0, 103)
mc.setBlock(T_2 + 4, AT - 1, 0, 103)
mc.setBlock(T_2 + 4, AT - 2, 0, 103)
mc.setBlock(T_2 + 4, AT - 3, 0, 103)
mc.setBlock(T_2 + 4, AT - 4, 0, 103)

mc.setBlock(T_2 + 5, AT - 0, 0, 103)
mc.setBlock(T_2 + 5, AT - 1, 0,   0)
mc.setBlock(T_2 + 5, AT - 2, 0,   0)
mc.setBlock(T_2 + 5, AT - 3, 0,   0)
mc.setBlock(T_2 + 5, AT - 4, 0, 103)

mc.setBlock(T_2 + 6, AT - 0, 0, 103)
mc.setBlock(T_2 + 6, AT - 1, 0, 103)
mc.setBlock(T_2 + 6, AT - 2, 0, 103)
mc.setBlock(T_2 + 6, AT - 3, 0, 103)
mc.setBlock(T_2 + 6, AT - 4, 0, 103)

# 3o NUMERO TEMPERATURA
mc.setBlock(T_3 + 10, AT - 0, 0, 103)
mc.setBlock(T_3 + 10, AT - 1, 0, 103)
mc.setBlock(T_3 + 10, AT - 2, 0, 103)
mc.setBlock(T_3 + 10, AT - 3, 0, 103)
mc.setBlock(T_3 + 10, AT - 4, 0, 103)

mc.setBlock(T_3 + 11, AT - 0, 0, 103)
mc.setBlock(T_3 + 11, AT - 1, 0,   0)
mc.setBlock(T_3 + 11, AT - 2, 0,   0)
mc.setBlock(T_3 + 11, AT - 3, 0,   0)
mc.setBlock(T_3 + 11, AT - 4, 0, 103)

mc.setBlock(T_3 + 12, AT - 0, 0, 103)
mc.setBlock(T_3 + 12, AT - 1, 0, 103)
mc.setBlock(T_3 + 12, AT - 2, 0, 103)
mc.setBlock(T_3 + 12, AT - 3, 0, 103)
mc.setBlock(T_3 + 12, AT - 4, 0, 103)

# 4o SIMBOLO DO GRAU 
mc.setBlock(GR + 14, AT - 0, 0, 103)
mc.setBlock(GR + 14, AT - 1, 0, 103)
mc.setBlock(GR + 14, AT - 2, 0, 103)
mc.setBlock(GR + 14, AT - 3, 0,   0)
mc.setBlock(GR + 14, AT - 4, 0,   0)

mc.setBlock(GR + 15, AT - 0, 0, 103)
mc.setBlock(GR + 15, AT - 1, 0,   0)
mc.setBlock(GR + 15, AT - 2, 0, 103)
mc.setBlock(GR + 15, AT - 3, 0,   0)
mc.setBlock(GR + 15, AT - 4, 0,   0)

mc.setBlock(GR + 16, AT - 0, 0, 103)
mc.setBlock(GR + 16, AT - 1, 0, 103)
mc.setBlock(GR + 16, AT - 2, 0, 103)
mc.setBlock(GR + 16, AT - 3, 0,   0)
mc.setBlock(GR + 16, AT - 4, 0,   0)

# 5o SIMBOLO DO CELSIUS
mc.setBlock(CE + 18, AT - 0, 0, 103)
mc.setBlock(CE + 18, AT - 1, 0, 103)
mc.setBlock(CE + 18, AT - 2, 0, 103)
mc.setBlock(CE + 18, AT - 3, 0, 103)
mc.setBlock(CE + 18, AT - 4, 0, 103) 

mc.setBlock(CE + 19, AT - 0, 0, 103)
mc.setBlock(CE + 19, AT - 1, 0,   0)
mc.setBlock(CE + 19, AT - 2, 0,   0)
mc.setBlock(CE + 19, AT - 3, 0,   0)
mc.setBlock(CE + 19, AT - 4, 0, 103)

mc.setBlock(CE + 20, AT - 0, 0, 103)
mc.setBlock(CE + 20, AT - 1, 0,   0)
mc.setBlock(CE + 20, AT - 2, 0,   0)
mc.setBlock(CE + 20, AT - 3, 0,   0)
mc.setBlock(CE + 20, AT - 4, 0, 103)
#-------------------------------

# PONTO '.'
mc.setBlock(PD + 8,  AT - 4, 0, 103)


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



mc.postToChat("Ola! Vamos comecar? ")
mc.postToChat("Qual seu nome? ")
nome = input ("Qual seu nome? ")

while nome =="":
    mc.postToChat("Qual seu nome? ")
    nome = input ("Qual seu nome? ")

mc.postToChat(nome + " Entrou no jogo !!!")



#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$




now = datetime.now()

print(str(now.day)  + "/" + str(now.month)  + "/" + str(now.year))
print(str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))




#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def simbolo_grau_celsius():

    # PONTO DECIMAL
    mc.setBlock(S_1 + 8,  AN-4, 0, MATERIAL)

    # 4o SIMBOLO DO GRAU 
    mc.setBlock(H_2 + 14, AN-0, 0, MATERIAL)
    mc.setBlock(H_2 + 14, AN-1, 0, MATERIAL)
    mc.setBlock(H_2 + 14, AN-2, 0, MATERIAL)
    mc.setBlock(H_2 + 14, AN-3, 0,   0)
    mc.setBlock(H_2 + 14, AN-4, 0,   0)

    mc.setBlock(H_2 + 15, AN-0, 0, MATERIAL)
    mc.setBlock(H_2 + 15, AN-1, 0,   0)
    mc.setBlock(H_2 + 15, AN-2, 0, MATERIAL)
    mc.setBlock(H_2 + 15, AN-3, 0,   0)
    mc.setBlock(H_2 + 15, AN-4, 0,   0)

    mc.setBlock(H_2 + 16, AN-0, 0, MATERIAL)
    mc.setBlock(H_2 + 16, AN-1, 0, MATERIAL)
    mc.setBlock(H_2 + 16, AN-2, 0, MATERIAL)
    mc.setBlock(H_2 + 16, AN-3, 0,   0)
    mc.setBlock(H_2 + 16, AN-4, 0,   0)

    # 5o SIMBOLO DO CELSIUS
    mc.setBlock(H_2 + 18, AN-0, 0, MATERIAL)
    mc.setBlock(H_2 + 18, AN-1, 0, MATERIAL)
    mc.setBlock(H_2 + 18, AN-2, 0, MATERIAL)
    mc.setBlock(H_2 + 18, AN-3, 0, MATERIAL)
    mc.setBlock(H_2 + 18, AN-4, 0, MATERIAL)

    mc.setBlock(H_2 + 19, AN-0, 0, MATERIAL)
    mc.setBlock(H_2 + 19, AN-1, 0,   0)
    mc.setBlock(H_2 + 19, AN-2, 0,   0)
    mc.setBlock(H_2 + 19, AN-3, 0,   0)
    mc.setBlock(H_2 + 19, AN-4, 0, MATERIAL)

    mc.setBlock(H_2 + 20, AN-0, 0, MATERIAL)
    mc.setBlock(H_2 + 20, AN-1, 0,   0)
    mc.setBlock(H_2 + 20, AN-2, 0,   0)
    mc.setBlock(H_2 + 20, AN-3, 0,   0)
    mc.setBlock(H_2 + 20, AN-4, 0, MATERIAL)
    

def pegar_numero(numero):

    global MATERIAL

    if numero == 0:

        # NUMERO 0
        mc.setBlock(SN + N+0, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-1, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-3, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-4, 0, MATERIAL)

        mc.setBlock(SN + N+1, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-1, 0,   0)
        mc.setBlock(SN + N+1, AN-2, 0,   0)
        mc.setBlock(SN + N+1, AN-3, 0,   0)
        mc.setBlock(SN + N+1, AN-4, 0, MATERIAL)

        mc.setBlock(SN + N+2, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-1, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-3, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-4, 0, MATERIAL)
        #--------------------------------

    if numero == 1:
        
        # NUMERO 1 
        mc.setBlock(SN + N+0, AN-0, 0,   0)
        mc.setBlock(SN + N+0, AN-1, 0,   0)
        mc.setBlock(SN + N+0, AN-2, 0,   0)
        mc.setBlock(SN + N+0, AN-3, 0,   0)
        mc.setBlock(SN + N+0, AN-4, 0,   0)

        mc.setBlock(SN + N+1, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-1, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-3, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-4, 0, MATERIAL)

        mc.setBlock(SN + N+2, AN-0, 0,   0)
        mc.setBlock(SN + N+2, AN-1, 0,   0)
        mc.setBlock(SN + N+2, AN-2, 0,   0)
        mc.setBlock(SN + N+2, AN-3, 0,   0)
        mc.setBlock(SN + N+2, AN-4, 0,   0)
        #--------------------------------

    if numero == 2:
        
        # NUMERO 1 
        mc.setBlock(SN + N+0, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-1, 0,   0)
        mc.setBlock(SN + N+0, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-3, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-4, 0, MATERIAL)

        mc.setBlock(SN + N+1, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-1, 0,   0)
        mc.setBlock(SN + N+1, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-3, 0,   0)
        mc.setBlock(SN + N+1, AN-4, 0, MATERIAL)

        mc.setBlock(SN + N+2, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-1, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-3, 0,   0)
        mc.setBlock(SN + N+2, AN-4, 0, MATERIAL)
        #--------------------------------

    if numero == 3:
        
        # NUMERO 1 
        mc.setBlock(SN + N+0, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-1, 0,   0)
        mc.setBlock(SN + N+0, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-3, 0,   0)
        mc.setBlock(SN + N+0, AN-4, 0, MATERIAL)

        mc.setBlock(SN + N+1, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-1, 0,   0)
        mc.setBlock(SN + N+1, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-3, 0,   0)
        mc.setBlock(SN + N+1, AN-4, 0, MATERIAL)

        mc.setBlock(SN + N+2, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-1, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-3, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-4, 0, MATERIAL)
        #--------------------------------

    if numero == 4:
      
        # NUMERO 1 
        mc.setBlock(SN + N+0, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-1, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-3, 0,   0)
        mc.setBlock(SN + N+0, AN-4, 0,   0)

        mc.setBlock(SN + N+1, AN-0, 0,   0)
        mc.setBlock(SN + N+1, AN-1, 0,   0)
        mc.setBlock(SN + N+1, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-3, 0,   0)
        mc.setBlock(SN + N+1, AN-4, 0,   0)

        mc.setBlock(SN + N+2, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-1, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-3, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-4, 0, MATERIAL)
        #--------------------------------

    if numero == 5:
        
        # NUMERO 1 
        mc.setBlock(SN + N+0, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-1, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-3, 0,   0)
        mc.setBlock(SN + N+0, AN-4, 0, MATERIAL)

        mc.setBlock(SN + N+1, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-1, 0,   0)
        mc.setBlock(SN + N+1, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-3, 0,   0)
        mc.setBlock(SN + N+1, AN-4, 0, MATERIAL)

        mc.setBlock(SN + N+2, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-1, 0,   0)
        mc.setBlock(SN + N+2, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-3, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-4, 0, MATERIAL)
        #--------------------------------

    if numero == 6:
        
        # NUMERO 1 
        mc.setBlock(SN + N+0, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-1, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-3, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-4, 0, MATERIAL)

        mc.setBlock(SN + N+1, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-1, 0,   0)
        mc.setBlock(SN + N+1, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-3, 0,   0)
        mc.setBlock(SN + N+1, AN-4, 0, MATERIAL)

        mc.setBlock(SN + N+2, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-1, 0,   0)
        mc.setBlock(SN + N+2, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-3, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-4, 0, MATERIAL)
        #--------------------------------

    if numero == 7:
       
        # NUMERO 1 
        mc.setBlock(SN + N+0, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-1, 0,   0)
        mc.setBlock(SN + N+0, AN-2, 0,   0)
        mc.setBlock(SN + N+0, AN-3, 0,   0)
        mc.setBlock(SN + N+0, AN-4, 0,   0) 

        mc.setBlock(SN + N+1, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-1, 0,   0)
        mc.setBlock(SN + N+1, AN-2, 0,   0)
        mc.setBlock(SN + N+1, AN-3, 0,   0)
        mc.setBlock(SN + N+1, AN-4, 0,   0)

        mc.setBlock(SN + N+2, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-1, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-3, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-4, 0, MATERIAL)
        #--------------------------------

    if numero == 8:
        
        # NUMERO 1 
        mc.setBlock(SN + N+0, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-1, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-3, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-4, 0, MATERIAL)

        mc.setBlock(SN + N+1, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-1, 0,   0)
        mc.setBlock(SN + N+1, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-3, 0,   0)
        mc.setBlock(SN + N+1, AN-4, 0, MATERIAL)

        mc.setBlock(SN + N+2, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-1, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-3, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-4, 0, MATERIAL)
        #--------------------------------    
        
    if numero == 9:
       
        # NUMERO 1 
        mc.setBlock(SN + N+0, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-1, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+0, AN-3, 0,   0)
        mc.setBlock(SN + N+0, AN-4, 0, MATERIAL)

        mc.setBlock(SN + N+1, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-1, 0,   0)
        mc.setBlock(SN + N+1, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+1, AN-3, 0,   0)
        mc.setBlock(SN + N+1, AN-4, 0, MATERIAL)

        mc.setBlock(SN + N+2, AN-0, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-1, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-2, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-3, 0, MATERIAL)
        mc.setBlock(SN + N+2, AN-4, 0, MATERIAL)
        #--------------------------------

#*********************************************************
#*********************************************************
        
while True:
    
    print(str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))

    now = datetime.now()


    MATERIAL = 5

    
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #            MONTANDO OS SEGUNDOS
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    AN = 27
    SN = S_1
    
    mc.setBlock(S_1 + 8,  AN-1, 0, MATERIAL) # DOIS PONTOS 1 DA HORA
    mc.setBlock(S_1 + 8,  AN-3, 0, MATERIAL)
    
    mc.setBlock(S_1 + 18, AN-1, 0, MATERIAL) # DOIS PONTOS 2 DA HORA
    mc.setBlock(S_1 + 18, AN-3, 0, MATERIAL)

    segundos = now.second

    primeiro_numero = segundos // 10
    segundo_numero  = segundos %  10

    N = 24
    numero = segundo_numero
    pegar_numero(numero)

    N = 20
    numero = primeiro_numero
    pegar_numero(numero)
    
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #            MONTANDO OS MINUTOS
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    minutos = now.minute

    primeiro_numero = minutos // 10
    segundo_numero  = minutos %  10

    N = 14
    numero = segundo_numero
    pegar_numero(numero)

    N = 10
    numero = primeiro_numero
    pegar_numero(numero)
    
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #            MONTANDO AS HORAS
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    horas = now.hour

    primeiro_numero = horas // 10
    segundo_numero  = horas %  10

    N = 4
    numero = segundo_numero
    pegar_numero(numero)

    N = 0
    numero = primeiro_numero
    pegar_numero(numero)


    

    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

   


    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #            MONTANDO O DIA
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    AN = 33
    SN = Di_1
    
    mc.setBlock(S_1 + 8,  AN-2, 0, MATERIAL) # BARRA 1 DA DATA
    mc.setBlock(S_1 + 18, AN-2, 0, MATERIAL) # BARRA 2 DA DATA
    
    dias = now.day

    primeiro_numero = dias // 10
    segundo_numero  = dias %  10

    N = 4
    numero = segundo_numero
    pegar_numero(numero)

    N = 0
    numero = primeiro_numero
    pegar_numero(numero)
    
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #            MONTANDO O MES
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    meses = now.month

    primeiro_numero = meses // 10
    segundo_numero  = meses %  10

    N = 14
    numero = segundo_numero
    pegar_numero(numero)

    N = 10
    numero = primeiro_numero
    pegar_numero(numero)
    
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #            MONTANDO O ANO
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    anos = now.year

    anos_aux  = anos %  1000

    primeiro_numero = anos_aux // 10
    segundo_numero  = anos_aux % 10

    N = 24
    numero = segundo_numero
    pegar_numero(numero)

    N = 20
    numero = primeiro_numero
    pegar_numero(numero)




    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


    

    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #            MONTANDO A TEMPERATURA
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   

    temperature = sensor.get_temperature()

    if (temperature < tempMIN):
        tempMIN = temperature

    if (temperature > tempMAX):
        tempMAX = temperature
        
    temp = int(temperature * 10)

    print("Temperatura: %.01f"%temperature)
    print("Temp MINIMA: %.01f"%tempMIN)
    print("Temp MAXIMA: %.01f"%tempMAX)


    #@@@@@@@@@@@@@@@@@@
    # TEMPERATURA ATUAL
    #@@@@@@@@@@@@@@@@@@
    
    MATERIAL = 103
    AN = 54
    SN = T_1
    
    N = 0
    primeiro_numero = temp // 100
    numero = primeiro_numero
    pegar_numero(numero)

    N = 4
    temp_aux_1 = temp % 100
    segundo_numero = temp_aux_1 // 10
    numero =  segundo_numero
    pegar_numero(numero)

    N = 10
    terceiro_numero = temp_aux_1 % 10
    numero = terceiro_numero
    pegar_numero(numero)
    
    simbolo_grau_celsius()


    #@@@@@@@@@@@@@@@@@@
    # TEMPERATURA MAX
    #@@@@@@@@@@@@@@@@@@

    MATERIAL = 41
    AN = 48
    SN = T_1

    temp = int(tempMAX * 10)
    
    N = 0
    primeiro_numero = temp // 100
    numero = primeiro_numero
    pegar_numero(numero)

    N = 4
    temp_aux_1 = temp % 100
    segundo_numero = temp_aux_1 // 10
    numero =  segundo_numero
    pegar_numero(numero)

    N = 10
    terceiro_numero = temp_aux_1 % 10
    numero = terceiro_numero
    pegar_numero(numero)
    
    simbolo_grau_celsius()

    mc.setBlock(H_2 + 22, AN-0, 0, MATERIAL)
    mc.setBlock(H_2 + 22, AN-1, 0, 0)
    mc.setBlock(H_2 + 22, AN-2, 0, 0)
    mc.setBlock(H_2 + 22, AN-3, 0, 0)
    mc.setBlock(H_2 + 22, AN-4, 0, MATERIAL)

    mc.setBlock(H_2 + 23, AN-0, 0, 0)
    mc.setBlock(H_2 + 23, AN-1, 0, MATERIAL)
    mc.setBlock(H_2 + 23, AN-2, 0, 0)
    mc.setBlock(H_2 + 23, AN-3, 0, MATERIAL)
    mc.setBlock(H_2 + 23, AN-4, 0, 0)

    mc.setBlock(H_2 + 24, AN-0, 0, 0)
    mc.setBlock(H_2 + 24, AN-1, 0, 0)
    mc.setBlock(H_2 + 24, AN-2, 0, MATERIAL)
    mc.setBlock(H_2 + 24, AN-3, 0, 0)
    mc.setBlock(H_2 + 24, AN-4, 0, 0)


    #@@@@@@@@@@@@@@@@@@
    # TEMPERATURA MIN
    #@@@@@@@@@@@@@@@@@@
    
    MATERIAL = 41
    AN = 42
    SN = T_1
    
    temp = int(tempMIN * 10)

    N = 0
    primeiro_numero = temp // 100
    numero = primeiro_numero
    pegar_numero(numero)

    N = 4
    temp_aux_1 = temp % 100
    segundo_numero = temp_aux_1 // 10
    numero =  segundo_numero
    pegar_numero(numero)

    N = 10
    terceiro_numero = temp_aux_1 % 10
    numero = terceiro_numero
    pegar_numero(numero)
    
    simbolo_grau_celsius()

    mc.setBlock(H_2 + 22, AN-0, 0, 0)
    mc.setBlock(H_2 + 22, AN-1, 0, 0)
    mc.setBlock(H_2 + 22, AN-2, 0, MATERIAL)
    mc.setBlock(H_2 + 22, AN-3, 0, 0)
    mc.setBlock(H_2 + 22, AN-4, 0, 0)

    mc.setBlock(H_2 + 23, AN-0, 0, 0)
    mc.setBlock(H_2 + 23, AN-1, 0, MATERIAL)
    mc.setBlock(H_2 + 23, AN-2, 0, 0)
    mc.setBlock(H_2 + 23, AN-3, 0, MATERIAL)
    mc.setBlock(H_2 + 23, AN-4, 0, 0)

    mc.setBlock(H_2 + 24, AN-0, 0, MATERIAL)
    mc.setBlock(H_2 + 24, AN-1, 0, 0)
    mc.setBlock(H_2 + 24, AN-2, 0, 0)
    mc.setBlock(H_2 + 24, AN-3, 0, 0)
    mc.setBlock(H_2 + 24, AN-4, 0, MATERIAL)

    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
