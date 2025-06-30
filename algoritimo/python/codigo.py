import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def atualizar_texto():
    texto = entrada.get()
    resultado = texto.upper()  # Exemplo simples: transforma em maiúsculas
    label_resultado.configure(text=resultado)

def alterar_tamanho_font(value):
    tamanho = int(float(value))
    label_resultado.configure(font=("Arial", tamanho))

janela = ctk.CTk()
janela.title("Exemplo CustomTkinter Avançado")
janela.geometry("450x300")

frame = ctk.CTkFrame(janela)
frame.pack(padx=20, pady=20, fill="both", expand=True)

label_instrucao = ctk.CTkLabel(frame, text="Digite algo para converter em maiúsculas:")
label_instrucao.pack(pady=(10,5))

entrada = ctk.CTkEntry(frame, width=300)
entrada.pack(pady=5)

botao = ctk.CTkButton(frame, text="Converter", command=atualizar_texto)
botao.pack(pady=10)

label_resultado = ctk.CTkLabel(frame, text="", font=("Arial", 18))
label_resultado.pack(pady=10)

slider = ctk.CTkSlider(frame, from_=10, to=40, command=alterar_tamanho_font)
slider.set(18)
slider.pack(pady=10)

janela.mainloop()

