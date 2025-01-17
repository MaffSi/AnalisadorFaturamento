### Analisador de Faturamento 📈 ###

O objetivo dessa aplicação é fazer a analise de um arquivo json, com dados diários de faturamento, de uma empresa, e extrair informações a partir deles.

### Requesitos e dependências 🧰 ###
----

- Python 3.6+ <br>
- PyQt5
- PyInstaller (para gerar executáveis) *Opcional*

### Instruções para Uso

1. Faça a instalação das dependências utilizando o arquivo `requirements.txt` com o seguinte comando:  
   ```bash
   pip install -r requirements.txt
   ```
2. Em seguida, execute o arquivo `main.py`
    ```bash
    python main.py
    ```
Ou, você pode realizar o download do executável da aplicação na aba de [Releases](https://github.com/MaffSi/AnalisadorFaturamento/releases/latest). <br>
> **Esse executável foi gerado pelo PyInstaller** 
### Capturas de Tela ###
---
#### Janela Inicial  
Com os campos aguardando a inserção do arquivo:

![Janela com os dados em branco](https://i.imgur.com/2SwLNbT.png)


#### Janela após processamento do arquivo
Após a inserção do arquivo, os campos que estavam com "-x-", são preenchidos com os dados referentes a análise.

![Janela com dados preenchidos](https://i.imgur.com/QB7YHfs.png)



