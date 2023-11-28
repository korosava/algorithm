import timeit
from typing import List, Callable, Any


def insertion_sort(array: List[float]) -> List[float]:
    for i in range(1, len(array)):
        elem_i = array[i]
        j = i - 1
        while j >= 0 and array[j] > elem_i:
            array[j + 1] = array[j]
            j -= 1
        array[j+1] = elem_i

    return array



def fn_time(fn: Callable[[], Any], call_num: int, name: str = 'fn'):
    print(f'[{name}] execution time: [{timeit.timeit(lambda: fn(), number=call_num)*1e6/call_num}] ns/execution')


if __name__ == '__main__':
    import random
    rnd = random.Random(42)
    arr = [rnd.uniform(0, 100) for i in range(100)]

    print(arr[:5])
    print(insertion_sort(arr)[:5])

    fn_time(fn=lambda: insertion_sort(arr), call_num=int(1e5), name='insertion_sort')
    fn_time(fn=lambda: sorted(arr), call_num=int(1e5), name='sorted')



