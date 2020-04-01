# issue-05
Дана функция, возвращающая текущий год. Дату и время получаем из API-worldclock

```python
# полный код в файле what_is_year_now.py
def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год

    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)
```

Напишите на неё тесты, проверяющие все сценарии работы

**DoD (Definition of Done) - критерии, позволяющие понять, что задача сделана, как ожидается**и:
* добейтесь 100% покртыия кода тестами
* используйте unittest.mock для замены реального обращения к API
* предоставьте отчет о покрытии в виде директории с html файлами
* файл README.md с описанием шагов для запуска
* файл result с командами и результатами запуска
* файл *.py с функцией и тестами
* нет замечаний от `flake8`
