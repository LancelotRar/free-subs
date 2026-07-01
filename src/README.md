<div align="center">

<h2> 策略分组预览 </h2>

<img width="800" src="/src/pic1.png">

<h2> 分流规则预览（白名单模式）</h2>

<img width="800" src="/src/pic2.png">

<h2> Windwos端节点延迟表现 （Clash Verge）</h2>

<img width="800" src="/src/pic3.png">

<h2> 安卓手机端节点延迟表现 （Clash Meta For Android）</h2>

<img width="800" src="/src/pic4.png">

</div>

<br>

<h1>🚀 Clash.Meta 精简清爽分流规则配置文件 </h1>

<p>
    这是一个基于 <strong>Clash.Meta (Mihomo)</strong> 核心定制的配置文件。它旨在提供精简、准确、性能的分流配置文件。提供自动化节点选择、负载均衡、故障切换等策略。
</p>


## 💡 为什么选择本套配置？

本规则集基于 Mihomo / Clash 内核深度定制，遵循“极速响应、隐私第一、极致分流”的设计哲学，是一套兼顾去广告、高吞吐与防泄露的现代化策略路由方案。

其核心优势如下：

### 1. 科学的自上而下匹配架构

规则链条严格遵循“**去广告 ➔ 常用域名精准分流 ➔ 国内外 IP 补漏 ➔ 最终兜底**”的逻辑。

* 在请求发起的第一时间拦截广告，省去不必要的域名解析与流量损耗。
* 将 Google、GitHub、Telegram、Microsoft 等高频海外生产力工具前置，确保日常开发与沟通秒级响应。

### 2. 严谨的 `no-resolve` 设计，杜绝 DNS 泄漏

我们在所有的 IP 规则（如 `cnip`、`telegramip` 等）中均启用了 `,no-resolve` 标记。

* **隐私保护**：防止内核为了匹配 IP 规则而强制在本地解析被墙的域名，从根源上杜绝了 DNS 污染与隐私泄漏风险。
* **性能优化**：大幅减少无用的本地 DNS 查询，降低网络请求延迟。

### 3. “国内白名单”式的策略兜底

针对国内复杂的网络环境，本配置采用了更聪明的路由闭环：

* 优先通过 `cn` 和 `cnip` 规则将绝大多数国内已知网站、APP 及大陆 IP 剥离，确保**国内流量 100% 直连**，不占用代理带宽。
* 尾部采用 `MATCH,🌀境外畅通` 进行防御性兜底。这意味着任何冷门、新出的海外网站或小众服务，无需手动添加规则，均可自动走代理顺畅访问。

### 4. 针对特定域名的精细化调优

针对 `jsdelivr.net`等公共前端库或特定解析服务进行了单独的直连优化。避免了因代理节点绕路导致的网页加载“卡图”、“卡脚本”问题，网页秒开体验更佳。

<br>

<h2>👥 适用人群</h2>

<table>
    <thead>
        <tr>
            <th>用户类型</th>
            <th>适用理由</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>追求稳定的用户</strong></td>
            <td>没理由，用就完了。</td>
        </tr>
        <tr>
            <td><strong>下载/看片爱好者</strong></td>
            <td>没理由，用就完了。</td>
        </tr>
        <tr>
            <td><strong>高级玩家</strong></td>
            <td>没理由，用就完了。</td>
        </tr>
        <tr>
            <td><strong>懒人一族</strong></td>
            <td>没理由，用就完了。</td>
        </tr>
    </tbody>
</table>

<hr>

<h2>⚠️ 以下需要注意 </h2>

<ol>
    <li><strong>核心依赖性：</strong> 请确保客户端使用的是最新的 Mihomo 核心，版本不要过于落后，以免代理客户端无法应对新的规则逻辑。</li>
    <li><strong>不适合对IP地理位置有精细需求的人群：</strong> 目前代理落地IP在韩国或日本。可正常访问Gemini、Chatgpt、Google、Youtube等几乎所有国外知名站点。 
    </li>
</ol>