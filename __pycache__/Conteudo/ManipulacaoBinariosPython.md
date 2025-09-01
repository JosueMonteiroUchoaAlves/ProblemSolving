# 🧮 Manipulação de Números Binários em Python

## 1. Representação em binário
- Python não tem um tipo especial para binário, usa apenas `int`.
- Para escrever um número em binário:
```python
x = 0b1011   # 11 em decimal
```
- Para converter **decimal → binário**:
```python
bin(11)  # '0b1011'
```

---

## 2. Conversões
- **Binário (string) → inteiro**:
```python
int("1011", 2)  # 11
```
- **Inteiro → binário (sem `0b`)**:
```python
format(11, "b")  # '1011'
```

---

## Sobre os tipos de binarios:

### Diferenças práticas

`0b1011` → inteiro (dá pra somar, subtrair, aplicar &, |, ^).

`"1011"` → string (dá pra fatiar, contar "1", inverter, concatenar).


### Se quiser alternar entre os dois:

#### string -> int
    x = int("1011", 2)  # 11

#### int -> string binária
    s = format(11, "b")   # '1011'
    s_fixed = format(11, "08b")  # '00001011' (8 bits fixos)

---

## 3. Operadores bit a bit
| Operador | Nome | Exemplo | Explicação |
|----------|------|----------|----------|
| `&` | AND | `0b1010 & 0b1100 → 0b1000` ||
| `\|` | OR  | `0b1010 \| 0b1100 → 0b1110` ||
| `^` | XOR | `0b1010 ^ 0b1100 → 0b0110` ||
| `~` | NOT | `~0b1010 → ...11110101` (cuidado, infinito)||
| `<<` | Shift Left  | `0b1010 << 1 → 0b10100` | `numeroParaShift << quantidadeDeCasas`|
| `>>` | Shift Right | `0b1100 >> 2 → 0b11` |`numeroParaShift >> quantidadeDeCasas`|

---

## 4. Máscaras de bits
Úteis para acessar ou modificar bits específicos.

- **Pegar o n-ésimo bit**:
```python
N = 0b101101
bit = (N >> 2) & 1  # pega o 3º bit da direita
""" Explicando:
    N >> 2 sendo N = 101101 retornaria:
    001011 pois andou aqueles 2 zeros para a direita
    e descartaria os 2 primeiros numeros da direita.
    como queremos o primeiro numero da direita, usamos o "and",
    que faz o seguinte:
    o numero 1 é um binario para a maquina, e como o python sabe 
    disso ele trabalha com o 1 de forma binaria, mas se quisessemos
    poderiamos colocar: 0b1 ou 0b0001... tanto faz!
    o importante é que:
    se o bit final de N for "1", então a sentença será verdadeira e
    retornará 1 para a variável bit. mas caso o bit final for 0 
    então a sentença será falsa e retornará 0 para a variavel bit
    e é exatamente isso que queremos!
"""
# Um exemplo mais complexo:
#        v quero este aqui embaixo
n = 0b101101   # 45 decimal
k = 2          
"""
Queremos o 3º bit da direita, então acrescento 2 zeros antes do 1 
(que, como ja vimos antes, nos ajuda a retornar qual numero esta naquela "casa")
"""

mask = 1 << k  # 000100 
bit = (n & mask) >> k 
""" 
vai retornar o numero que tem naquela casa e depois vai voltar as casas que tinhamos acrescentar antes para retornar só o numero, sem os zeros e uns a direita dele
"""
print(bit)     # 1
```

- **Ligar o K-ésimo bit**:
```python
N = 0b101101   # 45
K = 4
"""
O "ou" retorna uma uniao dos binarios que estavam ligados em qualquer um dos numeros. Se a posição não estava ligada em nenhum dos dois ela permanece ligada. Então o objetivo aqui é criar um binario que tenha ligado o bit que a gente quer e unir com o outro binario  "target"
"""
mask = (1 << K)
# (1 << K) = 10000 nesse exemplo, pois K vale 4
N = N | mask # N = 111101
``` 

- **Desligar o N-ésimo bit**:
```python
n = 0b101101   # 45
k = 3

mask = ~(1 << k)

N = N & mask # 0b111101

"""
(1 << k) é 1000 pois k vale 3
NOT (1 << k) é ...0111 pois ele é invertido de forma infinita
Então quando combinar este binario com um "and":

Tudo comparado com 1 sera verdadeiro: 
se for zero irá permanecer zero pois sao diferentes
se for um irá permanecer 1 pois são iguais
Porém o que for comparado com o 0 da mascara será desligado, pois:
tudo o que for 0 permanecera zero pois 2 zeros não se ligam
tudo o que for 1 ficara zero pois são diferentes.

A regra do AND é: 
se os dois estiverem ligados, permanecem. (If true AND true)
qualquer outro caso o zero permanece.

"""
```

- **Inverter o N-ésimo bit**:
```python
n = 0b101101   # 45
k = 0

mask = 1 << k # 0b1 -> pois quero inverter o ultimo bit
n = n ^ mask   # ou: n ^= mask
"""
Usamos o XOR (Exclusive OR) pois ele é muito exigente:
Ele aceita bits 1 (True), mas apenas se eles forem exclusivos de um 
dos "comparandos". Se aquele bit estiver ligado em ambos, ele vira zero. Com o zero ele não faz nada.
Exemplos:
------
n =   0b101101
mask: 0b000001
mask ^ n =  0b101100
O 1 se tornou 0 pois não era exclusivo
------
------
n =   0b101100
mask: 0b000001
mask ^ n =  0b101101
O zero se tornou 1 pois a mascara continha um 1 exclusivo
------
ou seja, o 1 está: 
tirando a exclusividade do 1 de N 
ou trocando o 0 por um 1 exclusivo
"""
print(bin(n))  # 0b101100  (44 decimal)
```

- **Checar se um bit está ligado**:
```python
n = 0b101101
k = 3

mask = 1 << k # 1000 pois k = 3
is_set = (n & mask) != 0 
"""
se o bit ligado na mascara estiver 
em comum com o n, (n & mask) será  0b1000, que é diferente de 0
"""
print(is_set)   # True (bit 3 é 1)
```
- **Isolar apenas alguns bits**:
```python
n = 0b101101
mask = 0b111     # queremos os 3 últimos bits
result = n & mask
print(bin(result))  # 0b101
```


---

## 5. Contagem e manipulação
- **Contar bits 1**:
```python
bin(0b101101).count("1")  # 4
```

- **Checar se é potência de 2**:
```python
def is_power_of_two(x):
    return x > 0 and (x & (x - 1)) == 0
```
- **Checar em qual "casa" está o último bit**

```python
N = 0b1001101100
mask = -N 
""" 
numeros binarios negativos são o 
inverso deles + 1 , pois se:
-0b1001101100 = 0b0110010011
a subtração seria:
    012 02 012
  0b1001101100
+ 0b0110010011 ( é uma soma pois esse binario já seria o numero negativo)
---------------
  0b0011011001
Ou seja, deu um outro numero que não é 0, e sabemos
que deveria ser: N + (-N) = 0, então o que falta?
falta um unico bit dar um empurraozinho! que todos os bits
de N vão se tornar 0. então, em binario, os numeros negativos são o inverso
dos positivos + 1: -N = ~(N) + 1 (o inverso dos bits de N mais 1)
então o certo ficaria:
-0b1001101100 = 0b0110010100 (pois o inverso é 0b0110010011 e eu 
acrescentei 1) 
veja que o unico bit que eles compartilham é o primeiro 1 à direita (que é o empurrãozinho que ele precisava)
---------------
    1111111
  0b1001101100
+ 0b0110010100 ->  ( é uma soma pois esse binario já É o numero negativo)
---------------
  0b0000000000 # Aqui criaria um bit a mais, porem vou ocultar, se precisar se livrar 
  desse overflow de bits manualmente, volto aqui e modifico para incluir como tratar


"""
```
---

## 6. Cuidados
- Python não tem limite fixo de bits → `~x` gera infinitos `1`s à esquerda.  
- Para simular **N bits fixos**, use máscara:
```python
N = 8
x = 0b1011
x = x & ((1 << N) - 1)  # garante que cabe em 8 bits
# (1 << N) cria um numero: 0b1_0000_0000 (com 8 zeros, então 9 bits), então precisamos tirar 1 bit e ainda por cima transformar todos esses zeros em 1, então subtraimos 1 e o numero fica assim: 0b1111_1111. Esse numero é o que mantém os uns e zeros do numero x intactos
# mas como esta mascara só tem 8 bits, x tambem sera forçado a ter 8!
```

---

✅ **Resumo:**  
Para manipular números binários em Python você precisa entender:
- Representação e conversão  
- Operadores bit a bit  
- Uso de máscaras  
- Controle de tamanho fixo de bits  
