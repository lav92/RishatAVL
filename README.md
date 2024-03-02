скачиваем проект с github (git clone https://github.com/lav92/RishatAVL.git)
устанавливаем библиотеки Django, python-dotenv, Stripe 
список пакетов:
Package            Version
------------------ --------
asgiref            3.7.2
certifi            2024.2.2
charset-normalizer 3.3.2
Django             5.0.2
idna               3.6
pip                24.0
python-dotenv      1.0.1
requests           2.31.0
setuptools         68.2.0
sqlparse           0.4.4
stripe             8.4.0
typing_extensions  4.10.0
urllib3            2.2.1
wheel              0.41.2

в файле .env.example написаны примеры константы секретных ключей
создаем в рядом с ним свой файл ".env" с секретными ключами Stripe, и Django
что бы получить api key Stripe нужно зарегистрироваться на сайте stripe.com
https://dashboard.stripe.com/test/developers -> вкладка API keys
