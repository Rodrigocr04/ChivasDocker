import random
import time

class SimuladorFutbol:
    def __init__(self):
        self.equipos = ["Chivas", "Atlas"]
        self.turno = random.choice(self.equipos)
        self.goles_chivas = 0
        self.goles_atlas = 0
        self.minuto = 0
        self.eventos = []
    
    def cambiar_turno(self):
        self.turno = "Atlas" if self.turno == "Chivas" else "Chivas"
    
    def simular_evento(self):
        numero = random.randint(1, 350)
        
        if 1 <= numero <= 100:
            return f"{self.turno}: Disparo desviado"
        elif 101 <= numero <= 200:
            return f"{self.turno}: Portero ataja el balón"
        elif 201 <= numero <= 250:
            if self.turno == "Chivas":
                self.goles_chivas += 1
            else:
                self.goles_atlas += 1
            return f"GOOOL de {self.turno}! Gol de cabeza!"
        elif 251 <= numero <= 300:
            if self.turno == "Chivas":
                self.goles_chivas += 1
            else:
                self.goles_atlas += 1
            return f"GOOOL de {self.turno}! Gol de penal!"
        elif 301 <= numero <= 350:
            if self.turno == "Chivas":
                self.goles_chivas += 1
            else:
                self.goles_atlas += 1
            return f"GOOOL de {self.turno}! Gol con el pie!"
    
    def simular_partido(self):
        print("¡Comienza el partido entre Chivas y Atlas!")
        print(f"Empieza atacando: {self.turno}\n")
        
        while self.minuto < 90:
            self.minuto += 1
            evento = self.simular_evento()
            self.eventos.append((self.minuto, evento))
            
            print(f"Minuto {self.minuto}: {evento}")
    
            self.cambiar_turno()
            
            time.sleep(0.1)
        
        print("\n¡Final del partido!")
        print(f"Resultado final: Chivas {self.goles_chivas} - {self.goles_atlas} Atlas")
        
        if self.goles_chivas > self.goles_atlas:
            print("¡Ganan las Chivas!")
        elif self.goles_atlas > self.goles_chivas:
            print("¡Gana el Atlas!")
        else:
            print("¡Empate!")

if __name__ == "__main__":
    simulador = SimuladorFutbol()
    simulador.simular_partido()