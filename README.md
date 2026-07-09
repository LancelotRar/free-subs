
## 🏪 利群Public Proxy - 利群便利店公益订阅

欢迎来到 **利群便利店**。本项目致力于通过 Cloudflare 边缘计算技术，为广大网友提供稳定、高速且永久免费的公益网络订阅服务。  

<p align="center">
  <a href="https://t.me/liqunchannel"><img src="https://img.shields.io/badge/利群便利店-频道-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"></a>
  <a href="https://t.me/liqunchat01"><img src="https://img.shields.io/badge/利群便利店-交流群-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"></a>
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
  -  **全协议覆盖：** 提供单节点及全平台订阅格式，灵活切换。
  -  **本项目当前使用Cmliu edgetunnel 搭建**

-----

## 📥 订阅地址    

**包含：**  
* 自适应订阅     
* Base64订阅    
* Clash.meta订阅    

**获取方式：（防止Github爬虫）**  
* 关注上方利群便利店『频道』，注意公益订阅信息（一般在置顶）。或加入群组，回复“订阅”，即可获取更多公益订阅地址。

> [!TIP]  
> ### Clash.Meta 精简分流规则 v8 版技术解析
>
> #### 1. 分层优先级匹配架构（Hierarchical Matching）
>
> 规则采用**优先级递进式匹配策略**，遵循「广告拦截 → 精准分流 → IP 路由 → 兜底策略」的处理链路：
>
> - **广告拦截前置**：在 DNS 解析前拦截广告域名，降低无效请求与流量消耗
> - **高频服务优先**：Google、GitHub、Telegram、Microsoft 等海外基础设施前置匹配，保障即时响应
>
> #### 2. DNS 无解析特性（no-resolve）
>
> 所有 IP 路由规则（如 `cnip`、`telegramip` 等）均启用 `,no-resolve` 标记：
>
> - **隐私防护**：避免内核为匹配 IP 规则而触发本地 DNS 解析，从源头规避 DNS 污染与隐私泄露
> - **性能优化**：减少冗余本地 DNS 查询，降低网络延迟
>
> #### 3. 国内流量直连策略（China Direct）
>
> 采用**白名单直连 + 黑名单兜底**的混合路由模式：
>
> - **直连优先**：通过 `cn` 与 `cnip` 规则识别并直连国内已知网站、应用及大陆 IP 段，确保国内流量 100% 不走代理
> - **未墙域名自动放行**：以 `MATCH,🌀境外畅通` 作为最终策略，自动放行未被墙的其他域名，亦可切换为走代理节点，黑白名单双吃，更加节省流量。
>
> #### 4. 元规则集架构（MetaRuleSet / mrs 格式）
>
> - 采用 MetaCubeX 官方维护的 **mrs 格式规则集**，相比传统 `.mrs` 文件具有更优的匹配效率
> - 规则源统一托管于 `testingcf.jsdelivr.net`，支持**86400s 自动更新**
> - 涵盖域名规则（geosite）与 IP 规则（geoip）双维度，覆盖广告、服务分类、国家区域等场景
>
> #### 5. 代理节点懒加载机制（Lazy Proxy Providers）
>
> - 启用 `lazy: true` 配置，避免因远程配置源异常导致订阅失效
> - 支持通过 `override.additional-prefix` 实现多源容灾切换
> - 代理组内置**自动选节点**、**负载均衡**、**故障切换**三重保障策略
>
> #### 6. FakeIP 加速模式
>
> - 启用 `enhanced-mode: fake-ip`，对指定规则集应用虚假 IP 技术
> - 覆盖私有域名（`rule-set:private`）与国内域名（`rule-set:cn`），减少 IPv6 支持系统的性能损耗
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

## Star History

<a href="https://www.star-history.com/?repos=LancelotRar%2Ffree-subs&type=date&legend=bottom-right">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=LancelotRar/free-subs&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=LancelotRar/free-subs&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=LancelotRar/free-subs&type=date&legend=top-left" />
 </picture>
</a>  

## ⚖️ 免责声明  

1.  本站所有资源均来自互联网公开渠道，仅供网络技术研究及开发人员交流使用。
2.  请遵守当地相关法律法规，严禁用于任何非法用途。
3.  作为公益项目，不保证服务的绝对稳定性及可用性，请勿用于重要生产环境。
