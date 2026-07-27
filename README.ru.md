## 🏪 Liqun Public Proxy - Общедоступная подписка Liqun

Добро пожаловать в **Liqun**. Этот проект предоставляет стабильные, высокоскоростные и постоянно бесплатные общественные сетевые подписки на основе технологии граничных вычислений Cloudflare.

<p align="center">
  <a href="https://t.me/liqunchannel"><img src="https://badgen.net/badge/Liqun/Канал/2CA5E0" align="absmiddle" style="height:28px"></a>
  <a href="https://t.me/liqunchat01"><img src="https://badgen.net/badge/Liqun/Чат/2CA5E0" align="absmiddle" style="height:28px"></a>
</p>
<p align="center">
  <img src="https://count.getloli.com/@:LancelotRar?name=%3ALancelotRar&theme=booru-koe&padding=7&offset=0&align=top&scale=1&pixelated=1&darkmode=auto">
</p>

> [!IMPORTANT]
> Независимо от того, где и из чьего руководства вы узнали о Cloudflare (далее CF) и о том, что на CF можно бесплатно разместить проекты для обхода блокировок, вы должны знать, кто автор проекта и как он называется. Ниже приведён обзор. Пожалуйста, поддержите авторов **Star** ⭐️⭐️⭐️!

### 1. Автор: Cmliu
* **Основная работа:** `edgetunnel`
* **Адрес проекта:** [https://github.com/cmliu/edgetunnel](https://github.com/cmliu/edgetunnel)
* **Звёзд:** <img src="https://badgen.net/github/stars/cmliu/edgetunnel" align="absmiddle">
* **Блог автора:** [https://blog.cmliussss.com/](https://blog.cmliussss.com/)
* **YouTube:** [CMLiussss](https://www.youtube.com/@CMLiussss)

### 2. Автор: Joey
* **Основная работа:** `cfnew`
* **Адрес проекта:** [https://github.com/byJoey/cfnew](https://github.com/byJoey/cfnew)
* **Звёзд:** <img src="https://badgen.net/github/stars/byJoey/cfnew" align="absmiddle">
* **Блог автора:** [https://joeyblog.net/](https://joeyblog.net/)
* **YouTube:** [joeyblog](https://www.youtube.com/@joeyblog)

### 3. Автор: Wang
* **Основная работа:** `Cloudflare-proxy`
* **Адрес проекта:** [https://github.com/eooce/Cloudflare-proxy](https://github.com/eooce/Cloudflare-proxy)
* **Звёзд:** <img src="https://badgen.net/github/stars/eooce/Cloudflare-proxy" align="absmiddle">
* **Блог автора:** нет
* **YouTube:** [eooce](https://www.youtube.com/@eooce)

### 4. Автор: ygkkk
* **Основная работа:** `Cloudflare-vless-trojan`
* **Адрес проекта:** [https://github.com/yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan)
* **Звёзд:** <img src="https://badgen.net/github/stars/yonggekkk/Cloudflare-vless-trojan" align="absmiddle">
* **Блог автора:** [https://ygkkk.blogspot.com/](https://ygkkk.blogspot.com/)
* **YouTube:** [ygkkk](https://www.youtube.com/@ygkkk)

-----

## 🚀 Особенности проекта

  - **Постоянная ссылка:** ссылка на подписку действительна долгое время, один импорт — пожизненное автообновление.
  - **Поддержка основных клиентов:** глубокая совместимость с ядрами Mihomo, xray и Sing-box.
  - **На базе Cloudflare:** построено на высокопроизводительных открытых решениях Cloudflare, баланс скорости и стабильности.
  - **Полное покрытие протоколов:** адаптивная конвертация, автоматическое преобразование в формат подписки, поддерживаемый клиентом.
  - **В данный момент проект использует Cmliu edgetunnel**

-----

## 📥 Адрес подписки

**Получение:**
* Подпишитесь на канал «Liqun» выше, следите за информацией о подписке (обычно в закреплённых сообщениях). Или вступите в группу и отправьте слово "подписка", чтобы получить больше адресов.

> [!TIP]  
> ### 🎯 Особенности файла конфигурации
> * **[📄 Адрес файла конфигурации](/src/example.yaml)**
>
> * **[📄 Подробное описание правил маршрутизации](/src/README.md)**
> #### 1. Предотвращение утечки DNS
>
> Внутренние китайские домены разрешаются через внутренние DNS (Aliyun, Tencent) прямым подключением, внешние домены — через публичные DNS через прокси. Эти два потока строго изолированы. Режим FakeIP дополнительно скрывает реальный IP на уровне ядра, предотвращая утечку информации о местоположении пользователя. Проверено на нескольких конфигурациях — риск утечки DNS отсутствует.
>
> #### 2. Группировка по странам
>
> Узлы автоматически группируются по странам: **Гонконг, Япония, Южная Корея, США, Сингапур, Тайвань**, остальные узлы попадают в категорию «Другие».
>
> #### 3. Прямое подключение внутри страны + прокси за рубеж, автоматическая маршрутизация
>
> Набор правил готов к использованию: посещение внутренних сайтов автоматически идёт через прямое подключение, не влияя на локальную скорость; посещение зарубежных сайтов автоматически идёт через прокси-узлы, без ручного переключения. Рекламные домены и домены конфиденциальности блокируются на этапе запроса, сокращая ненужный трафик.
>
> #### 4. Встроенный автоматический тест задержки для каждой группы
>
> Каждая групповая страна имеет подгруппу **автовыбора**. Система в реальном времени измеряет задержку и автоматически выбирает оптимальный узел. Пользователь также может вручную зафиксировать конкретный узел.

---

## 📋 Рекомендуемые клиенты прокси

> <b>Нажмите на название клиента для перехода на страницу релиза</b>

| Платформа | Рекомендуемые клиенты |
| :--- | :--- |
| **Windows** | [v2rayN](https://github.com/2dust/v2rayN/releases)・[Hiddify](https://github.com/hiddify/hiddify-app/releases)・[FlClash](https://github.com/chen08209/FlClash/releases)・[mihomo-party](https://github.com/mihomo-party-org/clash-party/releases)・[Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev/releases)・[Clashmi](https://github.com/KaringX/clashmi/releases)・[FlyClash](https://github.com/GtxFury/FlyClash/releases)・[Karing](https://github.com/KaringX/karing/releases)・[Bettbox](https://github.com/appshubcc/Bettbox/releases) |
| **Android** | [v2rayNG](https://github.com/2dust/v2rayNG/releases)・[ClashMetaForAndroid](https://github.com/MetaCubeX/ClashMetaForAndroid/releases/)・[FlClash](https://github.com/chen08209/FlClash/releases)・[Clashmi](https://github.com/KaringX/clashmi/releases)・[Hiddify](https://github.com/hiddify/hiddify-app/releases)・[NekoBox](https://github.com/MatsuriDayo/NekoBoxForAndroid/releases)・[FlyClash](https://github.com/GtxFury/FlyClash/releases)・[Karing](https://github.com/KaringX/karing/releases)・[Bettbox](https://github.com/appshubcc/Bettbox/releases) |
| **iOS** | Surge・Shadowrocket・Stash・[Hiddify](https://github.com/hiddify/hiddify-app/releases)・Loon・Egern・[Clashmi](https://clashmi.app/download)・[Karing](https://karing.app/)・Quantumult X |
| **macOS** | [FlClash](https://github.com/chen08209/FlClash/releases)・[mihomo-party](https://github.com/mihomo-party-org/clash-party/releases)・[Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev/releases)・Surge・[Clashmi](https://clashmi.app/download)・[Karing](https://karing.app/)・[FlyClash](https://github.com/GtxFury/FlyClash/releases) |
| **HarmonyOS** | [ClashBox](https://github.com/xiaobaigroup/ClashBox/releases) |

> [!TIP]
> Настоятельно рекомендуется установить **"интервал автообновления (Update Interval)"** в клиенте на 1 час, чтобы уменьшить количество запросов к CF Workers и избежать неработоспособности подписки из-за превышения лимита.

------

## ⚖️ Отказ от ответственности

1. **Заявление об источниках**: Ресурсы подписки, предоставляемые в данном проекте, собраны из общедоступных источников интернета и предназначены исключительно для исследований сетевых технологий, академического обмена и в качестве справочного материала для разработчиков.
2. **Обязанность законного использования**: Пользователи обязаны соблюдать соответствующие местные законы и нормативные акты. Использование любых ресурсов данного проекта в целях, противоречащих государственным законам, нормативным актам и политике, строго запрещено. Пользователи несут единоличную ответственность за все правовые последствия, возникшие в результате ненадлежащего использования.
3. **Заявление о характере услуг**: Данный проект предоставляется на общественных началах и не даёт никаких явных или подразумеваемых гарантий относительно непрерывности, стабильности, доступности и точности услуг. Проект не несёт ответственности за любые прямые или косвенные убытки, возникшие в результате использования или невозможности использования данных услуг.
4. **Защита интеллектуальной собственности**: Если какая-либо организация или частное лицо считает, что содержание данного проекта нарушает их законные права, пожалуйста, сообщите нам через страницу Issues проекта. Мы своевременно примем меры после проверки.
