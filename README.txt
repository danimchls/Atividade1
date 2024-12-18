Atividade 1: Python Environment e Manipulação de Imagens

Objetivo: Adquirir proficiência na geração de environments e manipulação de dados com as bibliotecas Opencv e Numpy. A partir do passo 5, criar commits para as modificações introduzidas no repositório.

Passos:
Criar um repositório público no Github
Clonar para sua máquina
Criar um python environment (utilizando Conda)
Commando: 
conda create -n <nome do environment> python=3.11 -y
Instalar Opencv e numpy utilizando o pip:
Comandos:
pip install <nome do pacote>
pip freeze (para observar pacotes instalados)
Criar um requirements.txt para registrar as versões das bibliotecas instaladas
Pesquisar como e porque o requirements.txt é utilizado
Criar um algoritmo de python para ler um vídeo e mostrar as frames deste na tela, usando Opencv
Modificar as frames usando numpy:
Fazer um crop do vídeo, centralizado, com metade da altura e largura da imagem original
Espelhar imagem
Rotacionar a imagem 90º usando:
numpy.transpose
Salvar vídeo modificado no disco usando Opencv.
