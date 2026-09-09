import random

def calcular_altitud(presion_hpa):
    altitud = 44330 * (1 - (presion_hpa / 1013.25) ** 0.1903)
    return altitud

def determinar_estado_vuelo(altitud_actual, altitud_previa, aceleracion):
    if altitud_actual > altitud_previa:
        estado = "Ascenso"
    elif abs(aceleracion) > 8:
        estado = "Apogeo Inicio de Caida Libre"
    else:
        estado = "Despliegue de Paracaidas"
    return estado

def evaluar_alerta_temperatura(temp_celsius):
    limite_critico = 90.0
    alerta = temp_celsius > limite_critico
    return alerta

def main():

    altitud_previa = 0.0
    altitud_maxima = 0.0
    apogeo_detectado = False
    suma_temperaturas = 0.0
    contador_lecturas = 0
    aceleracion_maxima = 0.0
    continuar = True
    x=0
    estado_previo = ""

    print("Sistema de Monitorea de Vuela - Cohete subordital")
    modo = input("Modo: ¿(M)anul o (S)imulacion automica?").strip().upper()

    while continuar:
        if modo == "S":
            presion_hpa = random.uniform(200.0, 1013.25)
            aceleracion = random.uniform(-9.81, 50.0)
            temp_celsius = random.uniform(25.0, 150.0)
        else:
            presion_hpa = float(input(f"Presion (hPa): "))
            aceleracion = float(input(f"Aceleracion (m/s^2): "))
            temp_celsius = float(input(f"Temperatura (C): "))

        altitud_actual = calcular_altitud(presion_hpa)

        if altitud_actual > altitud_maxima:
            altitud_maxima = altitud_actual

        estado = determinar_estado_vuelo(altitud_actual, altitud_previa, aceleracion)
        alerta = evaluar_alerta_temperatura(temp_celsius)

        if estado != "Ascenso" and estado_previo == "Ascenso" and not apogeo_detectado:
            apogeo_detectado = True
            print(f"Apogeo detectado. Altitud maxima: {altitud_maxima:.2f} m") 

        suma_temperaturas = suma_temperaturas + temp_celsius
        contador_lecturas = contador_lecturas + 1
        altitud_previa = altitud_actual
        estado_previo = estado

        if aceleracion > aceleracion_maxima:
            aceleracion_maxima = aceleracion

        print (f"Altitud: {altitud_actual:.2f} m")
        print (f"Estado: {estado} ")
        print (f"Temperatura {temp_celsius} C")

        if alerta:
            print(f"ALERTA TERMICA: SI")
        else:
            print(f"ALERTA TERMICA: NO")

        x = x + 1

        if altitud_actual <= 0:
            print("El cohete ha aterrizado. Fin de la simulacion.")
        elif modo == "S":
            if x >= 5:
                continuar = False
                print(f"Se ha alcanzado el limite de 5 lecturas en modo simulacion.")
        elif modo == "M":
            respuesta = input("¿Continuar? (s/n): ").strip().lower()
            if respuesta == "n":
                continuar = False

        temperatura_promedio = suma_temperaturas / contador_lecturas if contador_lecturas > 0 else 0.0
        print(f"Altitud maxima (apogeo): {altitud_maxima:.2f} m")
        print(f"Temperatura promedio: {temperatura_promedio:.2f} C")
        print(f"Aceleracion maxima registrada: {aceleracion_maxima:.2f} m/s^2")
        print(f"{x}")

if __name__ == "__main__":
   main()  
