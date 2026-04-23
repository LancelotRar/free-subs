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


<h1>🚀 Clash.Meta 精简清爽分流规则配置文件 </h1>

<p>
    这是一个基于 <strong>Clash.Meta (Mihomo)</strong> 核心深度定制的配置文件。它旨在为用户提供从自动化节点选择、负载均衡到精细化 DNS 解析的一站式科学上网体验。
</p>

<hr>

<h2>✨ 核心特点</h2>

<ul>
    <li><strong>多重代理策略：</strong> 预设了 <em>自动选择</em>、<em>负载均衡</em>、<em>故障切换</em> 和 <em>手动选择</em> 四种模式，满足从稳定性到高宽带的不同需求。</li>
    <li><strong>现代 DNS 架构：</strong> 采用 <code>fake-ip</code> 模式，配合阿里、腾讯及 Cloudflare 的 DoH/DoT 解析，不仅提升了首包响应速度，更通过 <code>respect-rules</code> 确保了国内外域名解析不走弯路。</li>
    <li><strong>智能分流规则：</strong> 
        <ul>
            <li>自动屏蔽广告流量（拦截 UDP 443 端口及常见广告域名）。</li>
            <li>内置大陆地理位置（GeoSite/GeoIP）直连，确保国内应用不掉线、不降速。</li>
            <li>支持 <code>sniffing</code> 流量嗅探，能够精准识别并分流被加密的流量。</li>
        </ul>
    </li>
    <li><strong>Provider 动态维护：</strong> 通过 <code>proxy-providers</code> 远程引入节点，实现节点列表的自动更新，无需频繁手动更换配置文件。</li>
    <li><strong>高性能设置：</strong> 开启了 <code>tcp-concurrent</code>（TCP 并发建立连接）和 <code>unified-delay</code>（统一延迟计算），优化了弱网环境下的连接体验。</li>
</ul>

<hr>

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
            <td>“故障切换”策略能确保当前节点失效时，秒级自动跳转至备用节点。</td>
        </tr>
        <tr>
            <td><strong>下载/看大片爱好者</strong></td>
            <td>“负载均衡”策略（round-robin）可以将流量分配到多个节点，最大化利用订阅宽带。</td>
        </tr>
        <tr>
            <td><strong>高级玩家</strong></td>
            <td>配置文件支持 TUN 模式（预留接口）、IPv6 优化以及详尽的 Fake-IP 过滤名单。</td>
        </tr>
        <tr>
            <td><strong>懒人一族</strong></td>
            <td>一次配置，长期自动更新，无需干预。</td>
        </tr>
    </tbody>
</table>

<hr>

<h2>⚠️ 缺点与不足</h2>

<blockquote>
    <p>💡 <em>在分享给朋友前，请务必知晓以下几点：</em></p>
</blockquote>

<ol>
    <li><strong>核心依赖性：</strong> 此配置使用了大量 Clash.Meta 特有字段（如 <code>unified-delay</code>, <code>proxy-providers</code> 中的新语法），<strong>不兼容</strong> 原版 Clash 开源版。请确保客户端使用的是 Mihomo 核心。</li>
    <li><strong>内存占用：</strong> 开启了 <code>geodata-mode</code> 和 <code>memconservative</code> 内存优化，但在节点极多或老旧设备（如旧款路由器）上，依然可能占用较多内存。</li>
    <li><strong>广告误杀：</strong> 开启了 <code>AND,((DST-PORT,443),(NETWORK,UDP))</code> 拦截（针对 QUIC 协议），虽然能有效屏蔽视频广告，但可能导致部分支持 HTTP/3 的网页加载略有延迟。</li>
    <li><strong>隐私风险：</strong> 配置文件中包含私人的 <code>token</code> 或订阅链接（示例中已包含利群公益链接），分享前请提醒朋友保护好自己的订阅信息。</li>
</ol>

<hr>

<h2>🛠️ 使用说明</h2>

<ol>
    <li>下载 <code>config.yaml</code>。</li>
    <li>在 Clash 客户端中导入，并确保 <strong>内核切换为 Clash.Meta / Mihomo</strong>。</li>
    <li>根据需要，在代理组中选择“🥳打包代理”下的具体模式。</li>
</ol>

<p align="center">
    <em>如有问题，请通过 Issues 或私信反馈。祝上网愉快！</em>
</p>

</body>
</html>
