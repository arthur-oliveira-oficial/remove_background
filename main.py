import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from rembg import remove
import os

class RemoveBackgroundApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Removedor de Fundo de Imagem")
        self.root.geometry("800x600")
        
        # Variáveis
        self.input_path = None
        self.output_path = None
        
        # Frame principal
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Área de visualização das imagens
        self.images_frame = tk.Frame(self.main_frame)
        self.images_frame.pack(expand=True, fill='both')
        
        # Frame para imagem original
        self.original_frame = tk.LabelFrame(self.images_frame, text="Imagem Original")
        self.original_frame.pack(side='left', expand=True, fill='both', padx=5)
        self.original_label = tk.Label(self.original_frame)
        self.original_label.pack(expand=True, fill='both')
        
        # Frame para imagem processada
        self.processed_frame = tk.LabelFrame(self.images_frame, text="Imagem Processada")
        self.processed_frame.pack(side='right', expand=True, fill='both', padx=5)
        self.processed_label = tk.Label(self.processed_frame)
        self.processed_label.pack(expand=True, fill='both')
        
        # Frame para botões
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(fill='x', pady=10)
        
        # Botões
        self.select_btn = tk.Button(self.button_frame, text="Selecionar Imagem", command=self.select_image)
        self.select_btn.pack(side='left', padx=5)
        
        self.process_btn = tk.Button(self.button_frame, text="Remover Fundo", command=self.process_image)
        self.process_btn.pack(side='left', padx=5)
        
        self.save_btn = tk.Button(self.button_frame, text="Salvar Imagem", command=self.save_image)
        self.save_btn.pack(side='left', padx=5)
        
    def select_image(self):
        self.input_path = filedialog.askopenfilename(
            filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp *.gif")])
        if self.input_path:
            self.display_image(self.input_path, self.original_label)
            
    def display_image(self, path, label, processed=None):
        image = Image.open(path) if not processed else processed
        # Tamanho da janela mais adequado
        display_size = (400, 400)
        
        # Calcular proporção para manter aspecto
        width, height = image.size
        ratio = min(display_size[0]/width, display_size[1]/height)
        new_size = (int(width*ratio), int(height*ratio))
        
        # Redimensionar com alta qualidade
        image = image.resize(new_size, Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        label.configure(image=photo)
        label.image = photo
        
    def process_image(self):
        if not self.input_path:
            messagebox.showerror("Erro", "Por favor, selecione uma imagem primeiro!")
            return
            
        try:
            input_image = Image.open(self.input_path)
            processed_image = remove(input_image)
            self.processed_image = processed_image  # Guardar referência
            self.display_image(None, self.processed_label, processed=processed_image)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar imagem: {str(e)}")
            
    def save_image(self):
        if not hasattr(self, 'processed_image'):
            messagebox.showerror("Erro", "Processe uma imagem primeiro!")
            return
            
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG", "*.png")]
        )
        
        if save_path:
            try:
                self.processed_image.save(save_path)
                messagebox.showinfo("Sucesso", "Imagem salva com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar imagem: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RemoveBackgroundApp(root)
    root.mainloop()