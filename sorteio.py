import tkinter as tk
import random
import time

class SorteioApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sorteio de Números")
        self.master.geometry("1920x1080")
        self.master.configure(bg="#f0f0f0")
        
        self.config_frame = tk.Frame(master, bg="#f0f0f0")
        self.config_frame.pack(fill="both", expand=True)
        
        self.intervalo_label = tk.Label(self.config_frame, text="Intervalo de números", font=("Helvetica", 36), bg="#f0f0f0")
        self.intervalo_label.pack(pady=20)
        
        self.intervalo_frame = tk.Frame(self.config_frame, bg="#f0f0f0")
        self.intervalo_frame.pack(pady=20)
        
        self.inicio_label = tk.Label(self.intervalo_frame, text="Início:", font=("Helvetica", 24), bg="#f0f0f0")
        self.inicio_label.pack(side="left", padx=10)
        self.inicio_entry = tk.Entry(self.intervalo_frame, font=("Helvetica", 24), width=10)
        self.inicio_entry.pack(side="left", padx=10)
        
        self.fim_label = tk.Label(self.intervalo_frame, text="Fim:", font=("Helvetica", 24), bg="#f0f0f0")
        self.fim_label.pack(side="left", padx=10)
        self.fim_entry = tk.Entry(self.intervalo_frame, font=("Helvetica", 24), width=10)
        self.fim_entry.pack(side="left", padx=10)
        
        self.repetir_var = tk.BooleanVar()
        self.repetir_check = tk.Checkbutton(self.config_frame, text="Permitir repetição", variable=self.repetir_var, font=("Helvetica", 24), bg="#f0f0f0")
        self.repetir_check.pack(pady=20)
        
        self.button = tk.Button(self.config_frame, text="Iniciar Sorteio", command=self.configurar_sorteio, font=("Helvetica", 24), bg="#4CAF50", fg="white")
        self.button.pack(pady=40)
        
        self.sorteio_frame = tk.Frame(master, bg="#f0f0f0")
        
        self.intervalo_sorteio_label = tk.Label(self.sorteio_frame, text="", font=("Helvetica", 36), bg="#f0f0f0")
        self.intervalo_sorteio_label.pack(pady=20)
        
        self.result_label = tk.Label(self.sorteio_frame, text="", font=("Helvetica", 400), bg="#f0f0f0")
        self.result_label.pack(pady=40, expand=True)
        
        self.buttons_frame = tk.Frame(self.sorteio_frame, bg="#f0f0f0")
        self.buttons_frame.pack(side="left", anchor="s", padx=40, pady=40)
        
        self.sortear_button = tk.Button(self.buttons_frame, text="Sortear", command=self.sortear, font=("Helvetica", 24), bg="#4CAF50", fg="white")
        self.sortear_button.pack(side="left", padx=10)
        
        self.reiniciar_button = tk.Button(self.buttons_frame, text="Reiniciar Sorteio", command=self.reiniciar_sorteio, font=("Helvetica", 24), bg="#FF5733", fg="white")
        self.reiniciar_button.pack(side="left", padx=10)
        
        self.voltar_button = tk.Button(self.buttons_frame, text="Voltar", command=self.voltar_config, font=("Helvetica", 24), bg="#FF5733", fg="white")
        self.voltar_button.pack(side="left", padx=10)
        
        self.historico_frame = tk.Frame(self.sorteio_frame, bg="#f0f0f0")
        self.historico_frame.pack(side="right", anchor="n", padx=40, pady=40)
        
        self.historico_label = tk.Label(self.historico_frame, text="Histórico de Números Sorteados:", font=("Helvetica", 24), bg="#f0f0f0")
        self.historico_label.pack(pady=20)
        
        self.historico_text = tk.Label(self.historico_frame, text="", font=("Helvetica", 18), bg="#f0f0f0", anchor="w", justify="left")
        self.historico_text.pack(pady=20, fill="both", expand=True)
        
        self.numeros_sorteados = set()

    def configurar_sorteio(self):
        self.config_frame.pack_forget()
        self.sorteio_frame.pack(fill="both", expand=True)
        
        min_num = self.inicio_entry.get()
        max_num = self.fim_entry.get()
        self.intervalo_sorteio_label.config(text=f"Sorteando números de {min_num} a {max_num}")

    def sortear(self):
        repetir = self.repetir_var.get()
        min_num = int(self.inicio_entry.get())
        max_num = int(self.fim_entry.get())
        
        numero = random.randint(min_num, max_num)
        if not repetir:
            while numero in self.numeros_sorteados:
                numero = random.randint(min_num, max_num)
            self.numeros_sorteados.add(numero)
        
        self.animar_sorteio(numero, min_num, max_num)
        self.atualizar_historico(numero)

    def animar_sorteio(self, numero_final, min_num, max_num):
        for _ in range(10):
            self.result_label.config(text=str(random.randint(min_num, max_num)))
            self.master.update()
            time.sleep(0.1)
        
        for _ in range(10):
            self.result_label.config(text=str(random.randint(min_num, max_num)))
            self.master.update()
            time.sleep(0.2)
        
        self.result_label.config(text=str(numero_final))

    def atualizar_historico(self, numero):
        historico_texto = self.historico_text.cget("text")
        novo_historico = f"{historico_texto} {numero} " if historico_texto else f"{numero} "
        self.historico_text.config(text=novo_historico)

    def reiniciar_sorteio(self):
        self.numeros_sorteados.clear()
        self.historico_text.config(text="")
        self.result_label.config(text="")

    def voltar_config(self):
        self.sorteio_frame.pack_forget()
        self.config_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = SorteioApp(root)
    root.mainloop()
