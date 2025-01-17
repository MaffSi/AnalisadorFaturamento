import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QGridLayout, QLabel, QPushButton, QGroupBox, QFileDialog, QFormLayout, QWidget
from componentes.tratamento_dados import analise_vendas

class MainInterface(QMainWindow):

    def __init__(self):
        self.caminho = ''
        super().__init__()
        self.setWindowTitle('Analisador de vendas por JSON')
        self.mainLayout = QGridLayout()
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)
        self.LabelTitle = QLabel('Análise de Vendas')
        self.mainLayout.addWidget(self.LabelTitle, 0, 0)

        self.LabelDesc = QLabel('Olá, por favor, clique no botão abaixo para selecionar o arquivo JSON com os dados de vendas.', self.mainWidget)
        self.mainLayout.addWidget(self.LabelDesc, 1, 0)

        self.ButtonSelectFile = QPushButton('Selecionar Arquivo', self.mainWidget)
        self.ButtonSelectFile.clicked.connect(self.getFilePath)
        self.mainLayout.addWidget(self.ButtonSelectFile, 2, 0) 

        self.AnaliseDadosGroupBox = QGroupBox()
        self.mainLayout.addWidget(self.AnaliseDadosGroupBox, 3, 0)

        self.AnaliseDadosLayout = QFormLayout()
        self.AnaliseDadosGroupBox.setLayout(self.AnaliseDadosLayout)
        self.AnaliseDadosGroupBox.setTitle('Análise de Dados')
        
        self.MaiorMediaVendasLabel = QLabel('Média de vendas:', self.AnaliseDadosGroupBox)
        self.AnaliseDadosLayout.addWidget(self.MaiorMediaVendasLabel)

        self.MaiorMediaVendasValue = QLabel('-x-', self.AnaliseDadosGroupBox)
        self.AnaliseDadosLayout.addWidget(self.MaiorMediaVendasValue)

        self.DiasComVendasAcimaMedia = QLabel('Dias com vendas acima da média:', self.AnaliseDadosGroupBox)
        self.AnaliseDadosLayout.addWidget(self.DiasComVendasAcimaMedia)

        self.DiasComVendasAcimaMediaValue = QLabel('-x-', self.AnaliseDadosGroupBox)
        self.AnaliseDadosLayout.addWidget(self.DiasComVendasAcimaMediaValue)

        self.MelhorFatDiaLabel = QLabel('Dia de melhor faturamento:', self.AnaliseDadosGroupBox)
        self.AnaliseDadosLayout.addWidget(self.MelhorFatDiaLabel)

        self.MelhorFatDiaValue = QLabel('-x-', self.AnaliseDadosGroupBox)
        self.AnaliseDadosLayout.addWidget(self.MelhorFatDiaValue)

        self.MelhorFatValorLabel = QLabel('Valor:', self.AnaliseDadosGroupBox)
        self.AnaliseDadosLayout.addWidget(self.MelhorFatValorLabel)

        self.MelhorFatValorValue = QLabel('-x-', self.AnaliseDadosGroupBox)
        self.AnaliseDadosLayout.addWidget(self.MelhorFatValorValue)

        self.PiorFatDiaLabel = QLabel('Dia de pior faturamento:', self.AnaliseDadosGroupBox)
        self.AnaliseDadosLayout.addWidget(self.PiorFatDiaLabel)
        
        self.PiorFatDiaValue = QLabel('-x-', self.AnaliseDadosGroupBox)
        self.AnaliseDadosLayout.addWidget(self.PiorFatDiaValue)

        self.PiorFatValorLabel = QLabel('Valor:', self.AnaliseDadosGroupBox)
        self.AnaliseDadosLayout.addWidget(self.PiorFatValorLabel)

        self.PiorFatValorValue = QLabel('-x-', self.AnaliseDadosGroupBox)
        self.AnaliseDadosLayout.addWidget(self.PiorFatValorValue)
    
    def getFilePath(self, x):
        caminho, tipo_arquivo = QFileDialog.getOpenFileName(self, 'OpenFile', os.getenv('HOME'), 'JSON Files (*.json)')
        self.caminho = caminho
        if self.caminho:
            self.calcular_dados()
    def calcular_dados(self):
        dados = analise_vendas(self.caminho)
        self.MaiorMediaVendasValue.setText(f'R$ {dados['MediaVenda']:.2f}')
        self.DiasComVendasAcimaMediaValue.setText(str(dados['DiasMaiorMedia']))
        self.MelhorFatDiaValue.setText(str(dados['MelhorFat']['dia']))
        self.MelhorFatValorValue.setText(f'R$ {dados['MelhorFat']['valor']:.2f}')
        self.PiorFatDiaValue.setText(str(dados['PiorFat']['dia']))
        self.PiorFatValorValue.setText(f'R$ {dados['PiorFat']['valor']:.2f}')

    