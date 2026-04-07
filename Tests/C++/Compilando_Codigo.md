# Como compilar e testar o código diretamente do terminal
É a maneira mais profissional e competitiva de se executar o código.

### C++
```bash
    g++ -Wall -std=c++17 arquivo.cpp

    time ./a.out < arquivo.in > my.sol

    diff arquivo.sol my.sol
```    
- `g++`: É o compilador GCC para C++, responsável por transformar o código-fonte em um programa executável.
- `-Wall`: Habilita todas as mensagens de aviso (warnings). Isso é essencial para identificar possíveis erros de lógica ou boas práticas negligenciadas no código.
- `-std=c++17`: Define a versão do padrão da linguagem a ser utilizada, neste caso, o C++17, garantindo que recursos modernos da linguagem sejam aceitos.
- `arquivo.cpp`: É o nome do arquivo com o seu código-fonte que será compilado.
- `-o` (opcional): Seguido por um nome, permite definir o nome do arquivo binário de saída (executável). Caso não seja usado, o sistema gera o padrão a.out.

- time: Executa o programa e faz a cronometragem do tempo de execução. Fundamental para testar se a sua solução respeita o limite de tempo estipulado pela plataforma.

- diff: Compara o arquivo de saída gerado pelo seu programa (my.sol) com o gabarito esperado (arquivo.sol). Se o terminal não retornar nada, os arquivos são idênticos e o teste passou. Se houver divergências, ele apontará exatamente em quais linhas os resultados diferem.

# Criando todos os arquivos necessarios pelo terminal

```bash
    code problema.{cpp,in,sol}
```
