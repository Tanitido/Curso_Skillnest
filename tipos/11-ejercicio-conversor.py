div = float(input("ingresa la cantidad en moneda local "))
usd = div*0.0050
eur = div*0.0047
gbp = div*0.0039
jpy = div*7.71

mensaje = f""" Cantidad Equivalente en USD{usd:.2f} #el ":.2f" es solo 2 decimales
Cantidad Equivalente en EUR{eur:.2f}
Cantidad Equivalente en GBP{gbp:.2f}
Cantidad Equivalente en JPY{jpy:.2f}"""

print(mensaje)
