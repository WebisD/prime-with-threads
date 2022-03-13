import sympy
import concurrent.futures

def tCalculaPrimo(data):
    primos = 0
    eh = True
    for n in range(len(data)):
        #if sympy.isprime(data[i]):
        #    primos += 1
        if n <= 3:
            eh = n > 1
        elif n % 2 == 0 or n % 3 == 0:
            eh = False
        else:
            i = 5
            while i ** 2 <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    eh = False
                i += 6
        if eh:
            primos += 1
    return primos

def resolve_trhread(data, nThreads):
    ThreadsQtdd = nThreads
    tamanholista = len(data)
    index = range(0, tamanholista+(tamanholista//ThreadsQtdd), tamanholista//ThreadsQtdd)
    primos = 0
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(ThreadsQtdd):
            futures.append(executor.submit(tCalculaPrimo, data=data[index[i]:index[i+1]]))
        for future in concurrent.futures.as_completed(futures):
            #futures.append(future.result())
            primos += future.result()
    return primos
