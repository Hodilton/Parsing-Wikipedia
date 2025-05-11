# Terminology Quiz Application

A Python application that fetches term definitions from Wikipedia pages and creates an interactive quiz to test your knowledge.

## Features

- 📥 **Web Scraping** - Extracts term definitions from Wikipedia URLs
- ✨ **Smart Formatting** - Cleans and standardizes definitions automatically
- ❓ **Interactive Quiz** - Multiple-choice test with scoring system
- 📊 **Progress Tracking** - Shows real-time score and correct answers
- 💾 **Data Management** - Saves processed definitions to CSV

## How to Use
1. Prepare a JSON file with Wikipedia URLs (see `data/links.json` example)
```json
{
  "urls": [
    "https://en.wikipedia.org/wiki/Algorithm",
    "https://en.wikipedia.org/wiki/Data_structure"
  ]
}
```
2. Run the main script: `python main.py`
3. Proramm parse defifnition
```python
Data '..\data\links.json' read successfully.
Parsing 1/77...
Parsing 2/77...
Parsing 3/77...
```
4. Take the quiz by selecting correct definitions
```
Score: 1
Question: Интерфе́йс
1. Переменная, диапазон значений которой состоит из адресов ячеек памяти или специального значения — нулевого адреса.
2. Класс, который позволяет хранить в себе ссылку на метод с определённой сигнатурой порядком и типами принимаемых и типом возвращаемого значений произвольного класса.
3. Структура программы/синтаксиса, определяющая отношение с объектами, объединенными только некоторым поведением.
```