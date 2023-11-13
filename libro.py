print('Escribir los siguientes datos para los libros: ')
nombre = input('Escriba el nombre del libro: ')
id = int(input('Proposione la ID de un libro: '))
precio = float(input('Proposcionar el valor del libro: '))
envioGratuito = input('Indicar si es gratuito (True/False)')

if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'Valor incorrecto, debe cumplirse True/False'
    
print(f'''
      Nombre: {nombre}
      Id: {id}
      Precio: {precio}
      Envio Gratuito?: {envioGratuito}
      ''')