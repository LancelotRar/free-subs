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

<hr>

<h2>✨ 核心特点</h2>

<ul>
    <li><strong>白名单配置：</strong> 按地理区域划分，国内网站，可以直连访问的，全部走直连。除此之外，全部走代理。省时省力，分流规则再不眼花缭乱。</li>
    <li><strong>懒人福音：</strong> 日常使用仅需调整打包代理内的节点运行策略。且每个分组默认选择的最优策略。开箱即用。</li>
    <li><strong>多重代理策略：</strong> 预设了 <em>自动选择</em>、<em>负载均衡</em>、<em>故障切换</em> 和 <em>手动选择</em> 四种模式，满足从稳定性到高宽带的不同需求。</li>
    <li><strong>DNS配置防泄露：</strong> 采用 <code>fake-ip</code> 模式，配合阿里、腾讯及 Cloudflare 的 DoH/DoT 解析，不仅提升了首包响应速度，更通过 <code>respect-rules</code> 确保了国内外域名解析不走弯路。且已多次迭代，参考十余份大佬的DNS配置，自测无DNS泄露</li>
    <li><strong>智能分流规则：</strong> 
        <ul>
            <li>自动屏蔽广告流量（拦截常见广告域名）。</li>
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
            <td><strong>下载/看片爱好者</strong></td>
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

<h2>⚠️ 以下需要注意 </h2>

<ol>
    <li><strong>核心依赖性：</strong> 请确保客户端使用的是最新的 Mihomo 核心，版本不要过于落后，以免代理客户端无法应对新的规则逻辑。</li>
    <li><strong>不适合对IP地理位置有精细需求的人群：</strong> 目前代理落地IP在韩国或日本。可正常访问Gemini、Chatgpt、Google、Youtube.  
    </li>
</ol>