from time import perf_counter

# Defino uma função (Decorador) que se chama relógio e não retorna nada
def clock(func) -> None:
  # meu complemento de função (o wrapper) aceita *args (x argumentos sem nome) e **kwargs (y argumentos com nome)
  def wrapper(*args, **kwargs):
    inicio = perf_counter()
    func(*args, **kwargs)
    total = perf_counter() - inicio
    print(f"A funcao {func.__name__} executou em {total} segundos")
  return wrapper
