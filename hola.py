import sys
class Saludador:
    def __init__(self, entidad: str = "Mundo"):
        self.entidad = entidad

    def generar_mensaje(self) -> str:
        if not self.entidad:
            raise ValueError("La entidad no puede estar vacía.")
        return f"¡Hola, {self.entidad}! Bienvenido al sistema."

def decorador_log(func):
    """Añade un registro simple a la ejecución."""
    def wrapper(*args, **kwargs):
        print("[LOG] Iniciando proceso de saludo...")
        resultado = func(*args, **kwargs)
        print("[LOG] Proceso finalizado con éxito.")
        return resultado
    return wrapper

@decorador_log
def ejecutar_aplicacion():
    try:
        # Instanciamos la clase con un nombre personalizado
        app = Saludador("Usuario Extraordinario")
        mensaje = app.generar_mensaje()
        
        print("\n" + "="*30)
        print(mensaje)
        print("="*30 + "\n")
        
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    ejecutar_aplicacion()