Guia para Executar o Projeto "Vitrine Virtual" Localmente

Passo 0: Pré-requisitos ter instalado **Python** e o **Git** instalados.

	1.Verificação do Python
  		* Abra o terminal ou o Prompt de Comando
    		* Digite "python --version" e aperte Enter.
    		* Se aparecer uma versão (ex: `Python 3.10.4`) ótimo!
			Se der erro ou a versão for inferior a 3.8, você precisa instalá-lo.(https://www.python.org/downloads/)
				Na instalação não esqueça de marcar acaixa que diz "Add Python to PATH"

	2.Verificar o Git
      		* No mesmo terminal, digite "git --version" e aperte Enter.
      		* Se aparecer uma versão, perfeito. Se não instale: (https://git-scm.com/downloads/).

Passo 1: Usar o Git p/ baixar os arquivos do projeto

	1.  Abra novamente o terminal.
	2.  Navegue para a pasta onde você quer salvar o projeto (Exemplo disco local C) usando o comando "C:" (sem aspas)
	3.  baixe o repositório com o seguinte comando:"git clone https://github.com/JoseeeVitor/Vitrine-Virtual.git"
	4.  Isso criará uma pasta chamada "Vitrine-Virtual".
		Entre nela "cd Vitrine-Virtual"

 				****Atenção:****
***Todos os comandos seguintes devem ser executados de dentro desta pasta***

Passo 2: Criar e Ativar o Ambiente Virtual ("venv")

	1.  Crie o ambiente virtual (venv)
		no terminal digite: "python -m venv venv"
 	2.  Agora, ative-o.
         ".\venv\Scripts\activate"

Se tudo estiver correto até aqui o nome do seu terminal vai mudar, mostrando (venv) no início da linha.


Passo 3: Instalar as Dependências do Projeto com o ambiente ativado, vamos instalar todos os
pacotes que o projeto precisa, que estão listados no arquivo `requirements.txt`.

	1.  Execute o comando: "pip install -r requirements.txt"
		(Isso vai baixar e instalar o Django e outras bibliotecas necessárias)

Passo 4: Preparar o Banco de Dados

	1.  Execute o seguinte comando (para criar o arquivo db.sqlite3): "python manage.py migrate"
  
Passo 5: Rodar o Servidor Local

	1.  Execute o comando: "python manage.py runserver"
	2.  O terminal vai mostrar algumas linhas e, por último, algo como:
   		 "Starting development server at http://127.0.0.1:8000/
   		 Quit the server with CTRL-BREAK (Windows) or CONTROL-C (macOS/Linux)."

    	3.Abra o seu navegador de internet e acesse o endereço:"http://127.0.0.1:8000"


**Para desligar o servidor**, volte ao terminal e pressione `Ctrl + C`.
