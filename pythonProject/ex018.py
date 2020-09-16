import math
ang = float(input("Digite o angulo: "))
angx = math.radians(ang)
cos = math.cos(angx)
sen = math.sin(angx)
tan = math.tan(angx)
print("O angulo eh {}, o cosseno eh {:.7f},o seno eh {:.7f} e a tangente eh {:.7f}".format(angx, cos, sen, tan))