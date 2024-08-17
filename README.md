<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://raw.githubusercontent.com/tkgs0/nbpt/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://raw.githubusercontent.com/tkgs0/nbpt/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-looklike

_✨ 你看我像人吗? ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/tkgs0/nonebot-plugin-looklike.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-looklike">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-looklike.svg" alt="pypi">
</a>
<a href="https://www.python.org">
    <img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">
</a>
<a href="https://nonebot.dev">
    <img src="https://img.shields.io/badge/nonebot-2.3.1+-red.svg" alt="nonebot">
</a>

</div>

## 📖 介绍

检测到关键字 `你看我像` 时自动进行赐封

## 💿 安装

**nb-cli安装, 包管理器安装  二选一**

<details>
<summary>使用 nb-cli 安装</summary>

在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-looklike

</details>

<details>
<summary>使用包管理器安装</summary>

在 nonebot2 项目的插件目录下, 打开命令行,

**根据你使用的包管理器, 输入相应的安装命令**

<details>
<summary>pip</summary>

    pip install nonebot-plugin-looklike

</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-looklike

</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-looklike

</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-looklike

</details>

打开 bot项目下的 `pyproject.toml` 文件,

在其 `plugins` 里加入 `nonebot_plugin_looklike`

    plugins = ["nonebot_plugin_looklike"]

</details>
</details>

## 🎉 使用

### 指令表

<table> 
  <tr align="center">
    <th> 指令 </th>
    <th> 权限 </th>
    <th> 需要@ </th>
    <th> 范围 </th>
    <th> 说明 </th>
  </tr>
  <tr align="center">
    <td> 你看我像 </td>
    <td> None </td>
    <td> 否 </td>
    <td> 私聊 | 群聊 </td>
    <td> 关键字匹配 </td>
  </tr>
</table>
