import subprocess
import os
import uuid

#la tool debe ser determinista

def medical_extract_tool():

    run_id = str(uuid.uuid4()) #CREA UN ID UNICO PARA CADA EJECUCION DE LA HERRAMIENTA, UTILIZANDO LA LIBRERIA UUID.

    run_path = f"/runs{run_id}" #DEFINIMOS UNA RUTA PARA GUARDAR LOS RESULTADOS DE LA EJECUCION DE LA HERRAMIENTA, UTILIZANDO EL ID UNICO CREADO ANTERIORMENTE.
    os.makedirs(run_path, exist_ok = True) #CREA EL DIRECTORIO PARA GUARDAR LOS RESULTADOS DE LA EJECUCION DE LA HERRAMIENTA, SI NO EXISTE YA.

    result = subprocess.run( #lanza un proceso real del sistema operativo, en este caso, ejecuta el comando "echo patient has diabetes" en la terminal.
        ["echo", "patient has diabetes"],
        capture_output = True, #caputra stdout y stderr del proceso.
        text = True #convierte la salida a texto en lugar de bytes.
    )

    with open(f"{run_path}/stdout.txt", "w") as f: #guarda la salida estándar del proceso en un archivo llamado stdout.txt dentro del directorio creado anteriormente.
        f.write(result.stdout)

    with open(f"{run_path}/stderr.txt", "w") as f: #guarda la salida de error del proceso en un archivo llamado stderr.txt dentro del directorio creado anteriormente.
        f.write(result.stderr)

    
    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "return_code": result.returncode
    }

