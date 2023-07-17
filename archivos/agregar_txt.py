with open('archivos\\texto_de_dalto.txt','a',encoding="UTF-8") as archivo:
    #usando un bucle para agregar varias lineas
    for i in range(5): archivo.write(f"\nLinea {i+1} agregada")
        #agregando lineas