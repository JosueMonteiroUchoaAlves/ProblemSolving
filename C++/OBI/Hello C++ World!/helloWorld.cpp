
/* Se você não quiser ter todo esse
   trabalho de adicionar uma por uma é
   só memorizar a biblioteca "bits/stdc++.h"
   (sem as aspas) que inclue todas as outras.
   É aceito pela OBI.
   */
#include <bits/stdc++.h>
#include <iostream>

using namespace std;

// Link da aula: https://noic.com.br/materiais-informatica/curso/comecando-do-zero/aula/

/* Uma dica e que se você declarar um numero dentro da main
 ele tera um valor aleatorio muito grande, mas se declarar fora
  ele vai ser inicializado com o valor padrao, que e 0
  */
int i;

int main()
{
  // A estrutura do cout e:
  // cout << valor1 << valor2 << ...;

  cout << 1898 << endl;          // Colocando um fim de linha
  cout << 3 << ' ' << 1 << endl; // Colocando um espaco entre os caracteres/numeros

  // Podemos realizar operaçoes com os numeros no C++
  // + -> adiçao
  // - -> subtraçao
  // / -> divisao
  // * -> multiplicaçao
  // % -> modulo, ou seja, a % b = resto da divisao inteira de a por b. Ex.: 8 % 5 = 3
  cout << 2 * 3 * 5 * 7 << endl;

  // Tambem e possivel imprimir frases (de maneira geral, varios caracteres de uma vez so)
  // usando as aspas duplas para indicar que e uma string (o nome nao importa agora), assim:
  cout << "Ola mundo!" << endl;

  cout << "Hello World!\n";
  /*
  Criacao de variaveis:
  Tipo Nome;
  ou
  Tipo Nome = Valor;
  */
  char letra = 'b'; // Aspa simples
  double variavel_decimal_grande = 2.4999999;
  float variavel_decimal_pequena = 2.5;
  bool booleano = true;
  string nome = "Josue"; // Aspas Duplas
  i++;
  i--;
  i += 3;
  i *= 4;
  cout << i;
  cin >> nome;
  cout << nome;
  /*
  operadores logicos de comparacao
  >
  <
  >=
  <=
  ==
  !=
  */

  /*
   No caso específico de adicionar 1 ou subtrair 1 de uma variável também existem
  outros tipos de operadores. Para acrescentar existe o x++ e o ++x, assim como
  para subtrair existe o x-- e o --x. Se essas expressões forem usadas com o objetivo
  exclusivo de incrementar/decrementar em 1 a variável, tanto faz usar a com o símbolo
  para direita ou esquerda (pós e pré incremento/decremento, respectivamente).
  Mas caso esse valor esteja sendo impresso, por exemplo, em cout << x++; a ordem das operações é:

  Imprime o valor de x.
  Incrementa o valor de x em 1.

  */
  return 0;
}
