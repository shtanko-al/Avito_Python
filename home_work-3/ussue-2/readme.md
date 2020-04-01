## issue-02
Дана функция, декодирующая строку из азбуки Морзе в английский

```python
# полный код в файле morse.py
def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    """
    decoded_letters = [
        MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]

    return ''.join(decoded_letters)
```

Напишите на неё параметрический тест, используя `pytest.mark.parametrize`

**DoD (Definition of Done) - критерии, позволяющие понять, что задача сделана, как ожидается**:
* минимум 3 тестовых примера
* файл README.md с описанием шагов для запуска
* файл result с командами и результатами запуска
* файл *.py с функцией и тестами
* нет замечаний от `flake8`
