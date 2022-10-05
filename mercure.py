m=float(input("donner la valeur de la masse de mercure"))
R=float(input("donner la valeur de la masse volumique de mercure"))
VT=float(input("donner la valeur du volume versé de mercure"))
vt=float(input("donner la valeur du volume versé dans chaque tube"))
vpar=float(input("donner la valeur du volume de parallélépipède"))
S=float(input("donner la valeur de la section"))
H=float(input("donner la valeur de la hauteur"))
VT=m/R
print("le volume versé de mercure est:",VT)
vt=VT-vpar/3
print("le volume versé dans chaque tube est:",vt)
H=vt/S
print("la hauteur est:",H)
