### Тестовое задание
Документ с тестовым заданием лежит в репозитории - [здесь](https://github.com/arkuz/vse_instrum_test/blob/master/others/%D0%92%D0%B5%D0%B4%D1%83%D1%89%D0%B8%D0%B9%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%20-%20%D1%82%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%92%D0%98.docx).

### Описание
 - В репозитории есть драйвер для браузера Chrome - [chromedriver.exe](https://github.com/arkuz/vse_instrum_test/blob/master/chromedriver.exe)
 - Видеоотчет о прохождении тестов - [run_tests_2019-04-05.mp4](https://github.com/arkuz/vse_instrum_test/blob/master/others/run_tests_2019-04-05.mp4)
 - HTML отчет о прохождении тестов - [Test Results - Unittests_in_Tests_py.html](https://github.com/arkuz/vse_instrum_test/blob/master/others/Test%20Results%20-%20Unittests_in_Tests_py.html)

### Требования
1. В системе должен быть установлен Python версии 3.
2. У Вас должен быть установлен virtualenv.
```bash
pip install virtualenv
```

### Установка
```bash
git clone https://github.com/arkuz/vse_instrum_test
cd vse_instrum_test
virtualenv venv
venv/scripts/activate
pip install -r requirements.txt
```

### Запуск
```bash
python -m unittest -v tests.MainTests
```
