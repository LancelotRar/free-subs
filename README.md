
## 🏪 利群Public Proxy - 利群便利店公益订阅

欢迎来到 **利群便利店**。本项目致力于通过 Cloudflare 边缘计算技术，为广大网友提供稳定、高速且永久免费的公益网络订阅服务。  

[🌐 中文](README.md) | [🇮🇷 فارسی](README.fa.md) | [🇷🇺 Русский](README.ru.md)

<p align="center">
  <a href="https://t.me/liqunchannel"><img src="https://badgen.net/badge/利群便利店/频道/2CA5E0" align="absmiddle" style="height:28px"></a>
  <a href="https://t.me/liqunchat01"><img src="https://badgen.net/badge/利群便利店/交流群/2CA5E0" align="absmiddle" style="height:28px"></a>
</p>
<p align="center">
  <img src="https://count.getloli.com/@:LancelotRar?name=%3ALancelotRar&theme=booru-koe&padding=7&offset=0&align=top&scale=1&pixelated=1&darkmode=auto">
</p>

> [!IMPORTANT]
>无论你是从哪里、从谁的教程知道了 Cloudflare（以下简称 CF），知道了 CF 上可以免费搭建科学上网项目，你都应该知道项目作者是谁，项目名字是什么。故做以下盘点，希望大家多多去给作者点赞和 **Star** ⭐️⭐️⭐️！  

### 1. 作者：Cmliu
* **代表作：** `edgetunnel`
* **项目地址：** [https://github.com/cmliu/edgetunnel](https://github.com/cmliu/edgetunnel)
* **现 Star 数：** <img src="https://badgen.net/github/stars/cmliu/edgetunnel" align="absmiddle">
* **作者博客：** [https://blog.cmliussss.com/](https://blog.cmliussss.com/)
* **YouTube 主页：** [CMLiussss](https://www.youtube.com/@CMLiussss)

### 2. 作者：Joey
* **代表作：** `cfnew`
* **项目地址：** [https://github.com/byJoey/cfnew](https://github.com/byJoey/cfnew)
* **现 Star 数：** <img src="https://badgen.net/github/stars/byJoey/cfnew" align="absmiddle">
* **作者博客：** [https://joeyblog.net/](https://joeyblog.net/)
* **YouTube 主页：** [joeyblog](https://www.youtube.com/@joeyblog)

### 3. 作者：佬王
* **代表作：** `Cloudflare-proxy`
* **项目地址：** [https://github.com/eooce/Cloudflare-proxy](https://github.com/eooce/Cloudflare-proxy)
* **现 Star 数：** <img src="https://badgen.net/github/stars/eooce/Cloudflare-proxy" align="absmiddle">
* **作者博客：** 无
* **YouTube 主页：** [eooce](https://www.youtube.com/@eooce)

### 4. 作者：ygkkk
* **代表作：** `Cloudflare-vless-trojan`
* **项目地址：** [https://github.com/yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan)
* **现 Star 数：** <img src="https://badgen.net/github/stars/yonggekkk/Cloudflare-vless-trojan" align="absmiddle">
* **作者博客：** [https://ygkkk.blogspot.com/](https://ygkkk.blogspot.com/)
* **YouTube 主页：** [ygkkk](https://www.youtube.com/@ygkkk)

-----

## 🚀 本项目亮点

  -  **永久固定：** 订阅链接长期有效，一次导入，终身自动更新。
  -  **主流支持：** 深度适配 Mihomo、xray、Sing-box内核为代表的主流代理客户端。
  -  **Cloudflare赋能：** 基于 Cloudflare 高性能开源方案搭建，兼顾速度与稳定性。
  -  **全协议覆盖：** 提供自适应转换，自动转换为各客户端支持的订阅格式。
  -  **本项目当前使用Cmliu edgetunnel 搭建**

-----

## 📥 订阅地址    

**获取方式：（防止Github爬虫）**  
* 关注上方利群便利店『频道』，注意公益订阅信息（一般在置顶）。或加入群组，回复“订阅”，即可获取更多公益订阅地址。

> [!TIP]  
> ### Clash.Meta 精简分流规则 v8 版 — 配置特性说明
>
> #### 1. YAML 锚点模板复用（Anchors）
>
> 配置通过 `&anchor` 定义基础参数模板，`<<: *anchor` 引用复用：
> - `&baseProvider` 定义代理集通用参数（type/interval/header/health-check），proxy-providers 只需补充 url
> - `&baseSelect` / `&baseUrltest` / `&baseFallback` / `&baseLoadbalance` 定义四种代理组策略骨架
> - `&rulesetDN` / `&rulesetIP` 定义规则集通用参数（type/behavior/format/interval），rule-providers 仅需指定 url
>
> #### 2. 代理组多锚点组合（Array Merge）
>
> 支持 `<<: [*anchorA, *anchorB]` 数组合并语法，将策略类型、偏好优先级、地域过滤解耦组合：
> - `🚀打包代理` = `baseSelect`（选择器）+ `preferUrltest`（自动优先）
> - `🇭🇰香港` = `baseSelect`（选择器）+ `filterHK`（地域过滤）
> - 三组策略优先级锚点 `preferUrltest` / `preferDirect` / `preferReject` 分别注入三个入口组
>
> #### 3. 七维地域过滤与分级代理
>
> - 7 组正则过滤锚点覆盖 HK/SG/JP/KR/US/TW/Other，匹配维度含国家代码、中文名、国旗 emoji、机场代码
> - 每地区设两级代理组：地区选择器（手动固定节点）+ 自动选择器（url-test 自动测速优选）
> - `filterOther` 采用 `exclude-filter` 反选策略，兜底未被其他筛选捕获的节点
>
> #### 4. DNS 路由与缓存优化
>
> - `enhanced-mode: fake-ip` + `fake-ip-filter: ['rule-set:private']` 规避私有地址虚假 IP 冲突
> - `respect-rules: true` 确保 DNS 请求遵循规则匹配链路
> - `cache-algorithm: arc` 自适应替换缓存算法，提升 DNS 缓存命中率
> - `nameserver-policy` 实现规则集级 DNS 路由：国内域名走阿里 DNS（DIRECT），其他走 Google/OpenDNS
> - `hosts` 显式映射 DNS 服务器域名为固定 IP，消除递归解析额外延迟
>
> #### 5. 透明代理与持久化
>
> - 内置 TUN 模块：支持 `auto-route` / `auto-redirect` / `dns-hijack` / `stack: mixed` 全栈透明代理
> - `profile.store-selected: true` 持久化用户节点选择，重启不丢失
> - `profile.store-fake-ip: true` 持久化 FakeIP 映射缓存，加速 DNS 重解析
>
> #### 6. 多端口监听与兼容
>
> - 同时监听 `mixed-port` / `port` / `socks-port` / `redir-port` / `tproxy-port` 五种端口，兼容各类客户端接入模式
> - TCP 并发（`tcp-concurrent: true`）+ `unified-delay: true` 统一延迟统计
> - `find-process-mode: strict` 精确进程识别
>
> * 🔥🔥🔥 更多分流规则细节请查看 → **[📄 分流规则详解](/src/README.md)**

---

## 📋 代理客户端推荐  

> <b>点击客户端名称可跳转至项目发布页下载</b>

| 平台 | 推荐客户端 |
| :--- | :--- |
| **Windows** | [v2rayN](https://github.com/2dust/v2rayN/releases)、[Hiddify](https://github.com/hiddify/hiddify-app/releases)、[FlClash](https://github.com/chen08209/FlClash/releases)、[mihomo-party](https://github.com/mihomo-party-org/clash-party/releases)、[Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev/releases)、[Clashmi](https://github.com/KaringX/clashmi/releases)、[FlyClash](https://github.com/GtxFury/FlyClash/releases)、[Karing](https://github.com/KaringX/karing/releases)、[Bettbox](https://github.com/appshubcc/Bettbox/releases) |
| **Android** | [v2rayNG](https://github.com/2dust/v2rayNG/releases)、[ClashMetaForAndroid](https://github.com/MetaCubeX/ClashMetaForAndroid/releases/)、[FlClash](https://github.com/chen08209/FlClash/releases)、[Clashmi](https://github.com/KaringX/clashmi/releases)、[Hiddify](https://github.com/hiddify/hiddify-app/releases)、[NekoBox](https://github.com/MatsuriDayo/NekoBoxForAndroid/releases)、[FlyClash](https://github.com/GtxFury/FlyClash/releases)、[Karing](https://github.com/KaringX/karing/releases)、[Bettbox](https://github.com/appshubcc/Bettbox/releases) |
| **iOS** | Surge、Shadowrocket、Stash、[Hiddify](https://github.com/hiddify/hiddify-app/releases)、Loon、Egern、[Clashmi](https://clashmi.app/download)、[Karing](https://karing.app/)、Quantumult X |
| **macOS** | [FlClash](https://github.com/chen08209/FlClash/releases)、[mihomo-party](https://github.com/mihomo-party-org/clash-party/releases)、[Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev/releases)、Surge、[Clashmi](https://clashmi.app/download)、[Karing](https://karing.app/)、[FlyClash](https://github.com/GtxFury/FlyClash/releases) |
| **鸿蒙** | [ClashBox](https://github.com/xiaobaigroup/ClashBox/releases) |


> [!TIP]
> 强烈建议在客户端内设置 **“自动更新频率 (Update Interval)”** 为 1 小时，以减少CF Workers请求数，以免刷爆导致订阅不可用。 完全不影响使用。

------

## ⚖️ 免责声明  

1. **信息来源声明**：本项目所提供之订阅资源均采集自互联网公开渠道，仅供网络技术研究、学术交流及开发人员学习参考之用。
2. **合法使用义务**：使用者应严格遵守所在地相关法律法规。禁止将本项目任何资源用于违反国家法律、法规及政策的任何用途。使用者须自行承担因不当使用所引致的一切法律责任。
3. **服务性质声明**：本项目系以公益目的提供，不对服务的连续性、稳定性、可用性及准确性作出任何明示或暗示的保证。本项目不对因使用或无法使用本服务所导致的任何直接或间接损失承担责任。
4. **知识产权保护**：如任何组织或个人认为本项目内容侵犯其合法权益，请通过项目 Issues 页面向我们反馈，我们将在核实后及时处理。
