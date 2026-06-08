# DD Engine Bot — Deployment

**Бот:** `@DD_engine_bot` (отдельный от `@antonmining_bot`)
**Репо:** `dd-engine` (отдельный от `metals-news-bot`)
**Время от начала до первого работающего сообщения:** ~20 минут.

---

## Что это

DD Engine Bot — Telegram-интерфейс к DD Production Line. Принимает команды от тебя, возвращает skeleton, intel, методологии, отслеживает активные DD-проекты.

**Архитектура:**
- GitHub Actions запускает `bot/dd_bot.py` каждые 5 минут
- Бот опрашивает Telegram `getUpdates` API, обрабатывает команды
- State (`data/active_dds.json`, `data/last_update_id.json`) комитится обратно в репо
- Daily status job (`bot/daily_status.py`) шлёт сводку утром в 09:00 MSK Пн-Пт

**Стоимость:** $0. GitHub Actions на публичных репах = безлимит. Telegram Bot API = бесплатно. DeepSeek опционален (только для Phase 2 `/research` команды).

---

## Шаг 1 — Создай репозиторий (2 минуты)

1. Открой https://github.com/new
2. **Repository name:** `dd-engine`
3. **Visibility:** Public (на публичных репах GitHub Actions безлимитный)
4. **НЕ ставь** галку "Add a README" (репо должен быть пустым)
5. Жми **Create repository**

---

## Шаг 2 — Залей файлы (5 минут)

Распакуй архив `dd-engine.zip` (полный пакет всех 35+ файлов: 27 файлов Phase 1b + 6 файлов бота + workflows + data).

Два варианта залить:

### A. Через веб-интерфейс GitHub (проще)

1. На странице репо `dd-engine` → **Add file** → **Upload files**
2. Перетащи **содержимое** распакованной папки (не саму папку), включая скрытые `.github/`
3. Внизу: **Commit changes** → Commit directly to main

⚠️ Если веб-аплоадер не видит `.github/` — создай файлы вручную:
- На странице репо: **Add file** → **Create new file**
- В поле имени введи: `.github/workflows/dd_bot_poll.yml`
- Вставь содержимое файла → Commit
- Повтори для `.github/workflows/dd_status_daily.yml`

### B. Через git (если установлен локально)

```bash
cd /путь/к/распакованному/dd-engine
git init
git add .
git commit -m "Initial dd-engine commit"
git branch -M main
git remote add origin https://github.com/antonsergeevichzaytsev-cell/dd-engine.git
git push -u origin main
```

---

## Шаг 3 — Получи токен бота (3 минуты)

1. Открой Telegram, найди чат с **@BotFather**
2. Отправь команду: `/mybots`
3. В списке выбери **@DD_engine_bot**
4. Тапни **API Token**
5. Скопируй строку вида `8123456789:AAEabcd...`

⚠️ Этот токен видишь один раз. Если уже терял — `@BotFather` → `/mybots` → `@DD_engine_bot` → **API Token** → опять покажет. Можно сделать `Revoke current token` если хочешь перевыпустить.

---

## Шаг 4 — Добавь secrets в репо (3 минуты)

Открой:
```
https://github.com/antonsergeevichzaytsev-cell/dd-engine/settings/secrets/actions
```

Создай **3 secrets** (зелёная кнопка **New repository secret**):

| Name | Value |
|---|---|
| `TELEGRAM_BOT_TOKEN` | (токен от BotFather, шаг 3) |
| `TELEGRAM_CHAT_ID` | `849676420` |
| `DEEPSEEK_API_KEY` | (тот же что в metals-news-bot — открой их secrets, скопируй) |

`DEEPSEEK_API_KEY` опционален — бот работает без него, но `/research` команда (Phase 2) не будет.

---

## Шаг 5 — Запусти первый раз вручную (2 минуты)

1. Открой: `https://github.com/antonsergeevichzaytsev-cell/dd-engine/actions/workflows/dd_bot_poll.yml`
2. Справа: **Run workflow** → ветка `main` → зелёная кнопка **Run workflow**
3. Подожди 30-60 сек, обнови страницу — должен пройти зелёный чекмарк

---

## Шаг 6 — Тест в Telegram (1 минута)

1. Открой чат с `@DD_engine_bot`
2. Отправь: `/start`
3. Подожди до 5 минут (cron работает каждые 5 мин)
4. Должен прийти ответ с приветственным сообщением

Если работает — отправь `/help` и попробуй:
- `/skeleton al_smelter` — должен прийти файл skeleton
- `/intel sanctions` — intelligence файл
- `/sectors` — список секторов

---

## Что бот умеет (актуальный список команд)

### Skeletons и intel
- `/skeleton <sector>` — sector DD skeleton (файл .md)
- `/intel <topic>` — intel file: `sanctions`, `cbam`, `tailings`, `jorc`
- `/method <name>` — methodology: `fel`, `owner_team`, `workflow`, `metal_acc`
- `/template <name>` — client templates: `ic_memo`, `mgmt_session`, `red_flag_alert`

### Управление DD
- `/new_dd <asset> | <sector> | <client>` — создать DD (Standard)
- `/new_dd <asset> | <sector> | <client> | Deep` — создать Deep DD
- `/list` — все активные DD
- `/status <id>` — детали конкретного DD
- `/phase <id> <0-8>` — обновить фазу (см. workflow)
- `/note <id> <text>` — добавить заметку
- `/done <id>` — закрыть DD

### Quick reference
- `/killer_q <sector>` — топ killer questions
- `/red_flags <sector>` — sector red flag checklist
- `/checklist <0-8>` — workflow phase detail
- `/sectors` — список доступных секторов
- `/ping` — проверка что бот жив

### Sectors
`al_smelter`, `al_downstream`, `ni_pgm`, `gold_hydromet`, `copper_concentrator`, `alumina_refinery`.

Псевдонимы работают: `aluminium`, `nickel`, `gold`, `copper`, `casthouse`, `pgm`, etc.

---

## Latency

Минимальный cron на GitHub Actions free tier = 5 минут. Это значит:
- Ты пишешь команду → ждёшь до 5 минут → бот отвечает
- Если хочешь мгновенный ответ — открой Actions → `DD Engine Bot poll` → `Run workflow` (вручную запустит)

В отличие от `@antonmining_bot` который **тебе пишет** по расписанию, `@DD_engine_bot` это **интерактивный command-bot** — он ждёт твою команду и отвечает.

Если в будущем понадобится мгновенный ответ — можно переехать на cloudflare workers с webhook (бесплатно, но требует HTTPS endpoint). Пока MVP с поллингом достаточно.

---

## Что дальше — Phase 2 будущего

После того как бот заработает, могу добавить:

1. **`/research <asset>`** — DeepSeek auto-research по публичным источникам (SEC filings, JORC reports, новости). Заполняет первичный Phase 2 black research.
2. **`/assemble <id>`** — собирает полный DD draft из skeleton + intel + relevant cases. Для конкретного DD по его ID.
3. **`/lessons <id>`** — после `/done` — извлекает уроки в `knowledge/anton_cases.json` автоматически.
4. **Cross-bot integration** — `@antonmining_bot` шлёт сигнал в DD Engine когда платформа отправляет project invitation, можно одним кликом создать DD-черновик.

---

## Troubleshooting

**Бот не отвечает после 10 минут:**
1. Открой Actions, проверь не упал ли последний run
2. Открой логи последнего run — посмотри ошибку
3. Самые частые причины:
   - `TELEGRAM_BOT_TOKEN` неправильный (проверь шаг 4)
   - `TELEGRAM_CHAT_ID` не строка из секрета (должно быть `849676420`, не имя)
   - Бот не запущен (отправь `/start` боту хотя бы раз в Telegram)

**Cron работает но команды не доходят:**
- Проверь что отправляешь команды с авторизованного chat_id (`849676420`). Бот игнорирует сообщения с других chat_id для безопасности.

**State не сохраняется:**
- Проверь GitHub Actions permissions: repo Settings → Actions → General → Workflow permissions → "Read and write permissions" должно быть выбрано.

---

## Архитектурная заметка

`dd-engine` репо изолирован от `metals-news-bot`. Они не пересекаются. Разные боты, разные репо, разные циклы deploy.

Общее у них:
- Один и тот же `TELEGRAM_CHAT_ID = 849676420` (Anton получает оба потока сообщений)
- Один и тот же DeepSeek key (один платёжный аккаунт)
- Один паттерн архитектуры (GitHub Actions + Python stdlib + state в JSON)

Это правильно: расширение, не дублирование.
