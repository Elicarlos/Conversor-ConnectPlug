import pandas as pd
import tkinter as tk
from tkinter import filedialog

def converter_csv():
   
    arquivo = filedialog.askopenfilename(title="Escolha o arquivo CSV", filetypes=[("Arquivos CSV", "*.csv;*.txt")])

    if arquivo:
     
        dataframe = pd.read_csv(arquivo)        
        dataframe = dataframe[dataframe['Código de barras'].notna()]

        if not dataframe.empty:
            
            nova_ordem_colunas = ['Código de barras', 'Nome', 'Valor']
          
            dataframe = dataframe[nova_ordem_colunas]
        
            dataframe['Valor'] = dataframe['Valor'].str.replace('"', '')
           
            dataframe.to_csv('produto_atualizado.txt', index=False, sep='|', header=False)

           
            mensagem_var.set("Conversão concluída. Novo arquivo: produto_atualizado.txt")
        else:
            mensagem_var.set("Nenhuma linha com 'Código de barras' encontrado. Nenhuma conversão realizada.")


def main():
    root = tk.Tk()
    root.title("Conversor CSV")

   
    botao_escolher_arquivo = tk.Button(root, text="Escolher Arquivo", command=converter_csv)
    botao_escolher_arquivo.pack(pady=20)

  
    global mensagem_var
    mensagem_var = tk.StringVar()
    mensagem_var.set("Escolha um arquivo e clique em 'Escolher Arquivo'")
    mensagem_label = tk.Label(root, textvariable=mensagem_var)
    mensagem_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
