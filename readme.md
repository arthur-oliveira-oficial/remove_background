# Ferramenta de Remoção de Fundo de Imagens

## Visão Geral
Esta é uma aplicação Python simples que permite aos usuários remover o fundo de imagens. A aplicação fornece uma interface gráfica do usuário (GUI) para selecionar uma imagem, processá-la para remover o fundo e salvar a imagem processada.

## Funcionalidades
- Selecionar uma imagem do sistema de arquivos local.
- Remover o fundo da imagem selecionada.
- Salvar a imagem processada no formato PNG.

## Requisitos
- Python 3.x
- Pacotes Python necessários:
  - `Pillow` para processamento de imagens.
  - `tkinter` para a GUI.
  - `remove` (ou qualquer outra biblioteca de remoção de fundo que você esteja usando).

## Instalação
1. Certifique-se de ter o Python 3.x instalado no seu sistema.
2. Instale os pacotes necessários usando o pip:
   ```bash
   pip install Pillow
   ```
   Note: A função `remove` é usada no código, mas não é uma biblioteca padrão. Você pode precisar instalar um pacote específico ou implementar essa função por si mesmo. Por exemplo, você pode usar `rembg`:
   ```bash
   pip install rembg
   ```

## Uso
1. Execute a aplicação:
   ```bash
   python main.py
   ```
2. Use a GUI para selecionar uma imagem.
3. Clique no botão "Processar Imagem" para remover o fundo.
4. Clique no botão "Salvar Imagem" para salvar a imagem processada.

## Estrutura do Código
- `main.py`: Contém a lógica principal da aplicação, incluindo processamento de imagem e manipulação da GUI.
  - `process_image`: Lida com o processamento da imagem removendo o fundo.
  - `display_image`: Exibe a imagem na GUI.
  - `save_image`: Salva a imagem processada em um arquivo.

## Solução de Problemas
- Se você encontrar problemas com a função `remove`, certifique-se de que a biblioteca está corretamente instalada e importada.
- Se a aplicação travar, verifique as mensagens de erro para mais detalhes.

## Contribuindo
Contribuições são bem-vindas! Por favor, faça um fork do repositório e envie um pull request com suas alterações.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.