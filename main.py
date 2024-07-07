import cv2
from pyzbar.pyzbar import decode
import pandas as pd

def scan_qr_code():
    cap = cv2.VideoCapture(0)  # Inicializa la captura desde la cámara web (cambiar el índice si tienes varias cámaras).
    
    # Abre el archivo CSV para escritura una vez fuera del bucle
    with open('qr_data.csv', 'a') as f:
        f.write('Nombre,Código\n')  # Escribe la cabecera del CSV
    
    while True:
        ret, frame = cap.read()  # Lee un frame desde la cámara.
        
        # Decodifica los códigos QR presentes en el frame.
        decoded_objects = decode(frame)
        
        for obj in decoded_objects:
            # Extrae el nombre y el código del QR.
            data = obj.data.decode('utf-8')
            name, code = data.split(',')
            print(f'Nombre: {name}, Código: {code}')
            
            # Guarda los datos en el archivo CSV.
            with open('qr_data.csv', 'a') as f:
                f.write(f'{name},{code}\n')
                
            # Muestra el resultado en el frame.
            cv2.putText(frame, f'Nombre: {name}, Código: {code}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            
        # Muestra el frame con el resultado.
        cv2.imshow('QR Scanner', frame)
        
        # Espera a que se presione 'q' para salir del bucle.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Libera la captura y destruye todas las ventanas abiertas.
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    scan_qr_code()
