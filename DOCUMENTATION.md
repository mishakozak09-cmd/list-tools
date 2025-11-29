\# Документація API



\## Модуль `lists.py`



\### Функція `get\_even\_numbers(numbers)`



\*\*Опис:\*\* Повертає всі парні числа зі списку.



\*\*Параметри:\*\*

\- `numbers` (list\[int | float]) – вхідний список чисел.



\*\*Повертає:\*\* `list` — список парних чисел.



\*\*Приклад:\*\*



```python

from lists import get\_even\_numbers



data = \[1, 2, 3, 4, 5, 6]



result = get\_even\_numbers(data)



print(result)  # \[2, 4, 6]

```



\### Функція get\_unique\_sorted(numbers)



\*\*Опис:\*\* Повертає відсортований список унікальних елементів.



\*\*Параметри:\*\*



numbers (list\[int | float]) – вхідний список чисел.



\*\*Повертає:\*\* list — відсортований список без дублікатів.



Приклад:



from lists import get\_unique\_sorted



data = \[3, 1, 2, 2, 3]



result = get\_unique\_sorted(data)



print(result)  # \[1, 2, 3]



```md

\## Документація



Детальний опис функцій: \[DOCUMENTATION.md](DOCUMENTATION.md)



