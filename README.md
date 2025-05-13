# Terminology Quiz Application

A Python application that fetches term definitions from Wikipedia pages and creates an interactive quiz to test your knowledge.

## Features

- 📥 **Web Scraping** - Extracts term definitions from Wikipedia URLs
- ✨ **Smart Formatting** - Cleans and standardizes definitions automatically
- ❓ **Interactive Quiz** - Multiple-choice test with scoring system
- 📊 **Progress Tracking** - Shows real-time score and correct answers
- 💾 **Data Management** - Saves processed definitions to CSV

## How to Work
1. Prepare a JSON file with Wikipedia URLs (example in `data/links.json`)
```json
{
  "urls": [
    "https://en.wikipedia.org/wiki/Algorithm",
    "https://en.wikipedia.org/wiki/Data_structure"
  ]
}
```
2. The program reads and processes the definitions:
```python
Data '..\data\links.json' read successfully.
Parsing 1/77...
Parsing 2/77...
Parsing 3/77...
```
3. Saves terms, definitions and links to `data/definitions.csv`

| Term          | Definition                                                                                                                                                                                   | Link                                                           |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| Система типов | Совокупность правил в языках программирования, назначающих свойства, именуемые типами, различным конструкциям, составляющим программу — таким как переменные, выражения, функции или модули. | [Wikipedia](https://ru.wikipedia.org/wiki/Система_типов)       |
| Адрес         | Символ или группа символов, которые идентифицируют регистр, отдельные части памяти или некоторые другие источники данных, либо место назначения информации.                                  | [Wikipedia](https://ru.wikipedia.org/wiki/Адрес_(информатика)) |

Download: [definitions.csv](./data/definitions.csv).
4. Take the quiz by selecting correct definitions
```
Score: 1
Question: Интерфе́йс
1. Переменная, диапазон значений которой состоит из адресов ячеек памяти или специального значения — нулевого адреса.
2. Класс, который позволяет хранить в себе ссылку на метод с определённой сигнатурой порядком и типами принимаемых и типом возвращаемого значений произвольного класса.
3. Структура программы/синтаксиса, определяющая отношение с объектами, объединенными только некоторым поведением.
Enter the correct option (1-3) or 'exit' to quit: 
```