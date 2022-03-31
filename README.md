#### Запуск
Для запуска нужно сохранить в samples фотографии и написать "bash run.sh". 
Форматы - png, jpeg, jpg. Имена - порядковые числа от 1. Примеры загружены.

#### Решение 
Я считаю "якобиан" и выделяю компоненты связности с примерно равным якобианом. Чтобы найти прямоугольник, использую стандартный алгоритм со стеком.
Асимптотика - O(N * M), где N * M - размер картинки.

#### Настройка
Алгоритм можно настаривать. Для этого есть файл CONST.py.
Там:
EXP - насколько резким может быть градиент,
LOCAL_SIZE - насколько локально считать якобиан,
BORDER_VALUE - насколько резкий переход не стоит учитавать при подсчете якобиана,
MIN_LENGTH - если якобиан по модулю меньше этого числа, то это 'константый цвет'.
