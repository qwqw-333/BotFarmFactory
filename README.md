# Запуск фермы
Алгоритм действий для запуска фермы:
1. Установить [docker engine](https://docs.docker.com/engine/install/).
2. Клонировать repo `git clone https://github.com/qwqw-333/BotFarmFactory.git`.
3. Создать файл `account.json` с перечнем желаемых телеграмм аккаунтов. Пример файла `account.json.example`.
> [!NOTE]
> В файле `account.json` указываются номера и по необходимости прокси.
4. По необходимости внести изменния в настройки фермы `config.py `.
5. Подключить аккаунты к ферме. Используя консоль в папке проекта запустить контейнер `docker compose run botfarmfactory` и ввести коды аутинтификации.
> [!NOTE]
> После запуска данной команды, ферма аутентифицируется в каждом из аккаунтов телеграмма и под каждый из них создаст `_number_.session`.
> В дальнейшем бот использует `_number_.session` для получения доступа к ботам.
6. Остановить ферму `ctrl+c`.
7. Запустить ферму в фоновом режиме `docker compose up -d`.

---
# Обновление фермы
> [!NOTE]
> Объязательно находится в папке проекта
```bash
docker stop botfarmfactory
git fetch origin
git branch
git log HEAD..origin/main --oneline
git merge origin/main
```

# Работа с фермой
## Логи

* Просмотр логов фермы в реальном времени:

`docker logs -f botfarmfactory`
* Просмотр последних _N_ логов:

`docker logs -n _N_ botfarmfactory`

Пример логов:
![img.png](img.png)

## Управление
* Остановить ферму:

    `docker stop botfarmfactory`
* Запустить ферму в фоновом режиме:

    `docker start botfarmfactory`

## Настройки фермы
> [!IMPORTANT]
> Все настройки фермы находятся в файле `config.py`

### "Тапалки"
> [!NOTE]
> По умолчанию включены все 'тапалки'

* Для включение только определенных 'тапалок' добавить их название в перечень `ENABLED_BOTS`. 
  > [!NOTE]
  > Если надо включить только определенные 'тапалки'.

  Пример записи:
    ```python
    ENABLED_BOTS = [
      'blum',
    ]
    ```
* Для выключение только определенных тапалок добавить их название в перечень `DISABLED_BOTS`. 
  > [!NOTE]
  > Для выключение определенных 'тапалок'.  
  
  Пример записи:
  ```python
  DISABLED_BOTS = [
    'blum',
  ]
  ```

### Многопоточность
> [!NOTE]
> Параллельный запуск аккаунтов

* Для включение в файле `config.py` изменить значение строки `MULTITHREAD` с `FALSE` на `TRUE`

---

# DONATE
> [!CAUTION]
> Проект прододжает развивается на безвозмездной основе, и ваша поддержка поможет последователям не закидывать развитие проекта.

---
#### Cпасибо [автору проекта](https://github.com/TotalAwesome/BotFarmFactory):
USDT:
*  TRC20 – `TTTMM1PXxNS7d3tAcruamT6GE8ye5BrZ4w`
