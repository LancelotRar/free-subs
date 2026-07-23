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

> 完整配置示例见 [`example.yaml`](example.yaml)

## 💡 为什么选择本套配置？

本规则集基于 Mihomo / Clash 内核深度定制，遵循"极速响应、隐私第一、极致分流"的设计哲学，是一套兼顾去广告、高吞吐与防泄露的现代化策略路由方案。

### 1. 科学的自上而下匹配架构

规则链条严格遵循"**去广告 ➔ 常用域名精准分流 ➔ 国内外 IP 补漏 ➔ 最终兜底**"的逻辑。

* 在请求发起的第一时间拦截广告，省去不必要的域名解析与流量损耗。
* 将 Google、GitHub、Telegram、Microsoft 等高频海外生产力工具前置，确保日常开发与沟通秒级响应。

### 2. 严谨的 `no-resolve` 设计，杜绝 DNS 泄漏

在所有的 IP 规则（如 `cnip`、`telegramip` 等）中均启用了 `,no-resolve` 标记。

* **隐私保护**：防止内核为了匹配 IP 规则而强制在本地解析被墙的域名，从根源上杜绝了 DNS 污染与隐私泄漏风险。
* **性能优化**：大幅减少无用的本地 DNS 查询，降低网络请求延迟。

### 3. "国内白名单"式的策略兜底

针对国内复杂的网络环境，本配置采用了更聪明的路由闭环：

* 优先通过 `cn` 和 `cnip` 规则将绝大多数国内已知网站、APP 及大陆 IP 剥离，确保**国内流量 100% 直连**，不占用代理带宽。
* 尾部采用 `MATCH,🐠漏网之鱼` 进行防御性兜底。这意味着任何冷门、新出的海外网站或小众服务，无需手动添加规则，均可自动走代理顺畅访问。

### 4. 针对特定域名的精细化调优

针对 `jsdelivr.net`等公共前端库或特定解析服务进行了单独的直连优化。避免了因代理节点绕路导致的网页加载"卡图"、"卡脚本"问题，网页秒开体验更佳。

<br>

## YAML 配置特色

本配置充分利用了 Clash.Meta 的 YAML 语法特性，实现了高度自动化与可维护性：

### 1. 基于正则表达式的区域分流

每个地区策略组（香港、日本、韩国、美国、新加坡、台湾省）均通过 `filter` 正则自动匹配节点名称，无需手动维护节点列表：

```yaml
- name: 日本
  filter: '^(?=.*(?i)(日|🇯🇵|JP|Japan|NRT|HND|KIX|CTS|FUK)).*$'
  include-all: true
```

`exclude-filter` 用于"其他节点"策略组，自动归集未被任何地区匹配的剩余节点。

### 2. `include-all` 自动节点发现

策略组使用 `include-all: true` 替代手动罗列节点，新增或删除订阅节点后无需修改配置文件：

```yaml
- name: 🫱手动选择
  type: select
  include-all: true
```

### 3. `empty-fallback` 安全兜底

所有 `url-test` 和 `fallback` 策略组均配置了 `empty-fallback: REJECT`，当所有节点不可用时自动拒绝流量，避免断网后请求卡死。

### 4. 基于 `rule-set` 的模块化规则

规则集通过 `rule-providers` 从远程拉取 MRS 格式规则，本地仅维护规则名称与策略组的映射关系，规则内容与配置分离，更新规则集无需修改配置文件。

### 5. 智能 DNS 分流

采用 `fake-ip` 模式 + `nameserver-policy` 实现 DNS 分流：

- `rule-set:cn` 走阿里 DNS（直连解析）
- `rule-set:gfw` 走 Google DNS（代理解析）
- `proxy-server-nameserver` 用于解析代理服务器域名，避免 DNS 污染

### 6. 自动化的代理提供者

`proxy-providers` 通过 HTTP 拉取订阅，配合 `override.additional-prefix` 自动为节点添加前缀标识，`health-check` 确保节点可用性。

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
            <td>策略组自带故障切换与健康检查，节点挂了自动转移</td>
        </tr>
        <tr>
            <td><strong>下载/看片爱好者</strong></td>
            <td>YouTube、Netflix 等流媒体域名已前置分流，开箱即用</td>
        </tr>
        <tr>
            <td><strong>高级玩家</strong></td>
            <td>支持负载均衡、手动选择、正则过滤，满足个性化调优需求</td>
        </tr>
        <tr>
            <td><strong>懒人一族</strong></td>
            <td>`include-all` 自动发现节点，订阅更新后无需手动修改配置</td>
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