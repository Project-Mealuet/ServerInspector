***[English version](README_en.md)***

# Mealuet Server Inspector

基于 `flask` 的简单API实现，可以用于获取服务器的性能数据及Minecraft的服务端参数。

# 准备

- 运行之前，确保已经安装所有依赖：
    ```bash
    pip3 install -r requirements.txt
    ```

- 必须设置环境变量 `SECRET_KEY` ：
    ```bash
    echo 'SECRET_KEY="your_secret_key"' > .env
    ```

- 该 API 设计上是同 Minecraft 服务器运行在**一台机器**上的，这样可以监测服务器的CPU和内存使用情况。  
- 如果你需要在另一台机器上运行 API ，请修改 `main.py` 中的 `host`
- 配置 `server.properties` ：
    ```properties
    enable-query=true
    query.port=25585
    ```
- 启动 API 服务器：
    ```bash
    python3 main.py
    ```
- ⚠ ***注意：API 服务器默认开在 `25595` 端口，强烈建议配置反向代理并设置SSL。配置示例见 `examples`。***


# 用法

## 环境变量:

`SECRET_KEY`: 用于API的授权认证。


## 端点:

1. 获取系统状态 (GET /api/status/system)  
2. 获取Minecraft服务器状态 (GET /api/status/minecraft)

## 请求头:

`X-API-KEY`: API密钥，需要与设置的`SECRET_KEY`相匹配。

## 响应:

1. `GET /api/status/system` 返回系统的CPU百分比使用率，内存的总量、已使用量和使用百分比，以及磁盘的总量、已使用量和使用百分比。
2. `GET /api/status/minecraft` 返回Minecraft服务器的状态，包括主机名、游戏类型、游戏ID、版本、插件、地图、主机端口以及玩家的数量、最大玩家数和玩家列表。

## 示例

### 获取系统状态

请求：
```vbnet
GET /api/status/system
Headers: X-API-KEY: your_secret_key
```
响应：
```json
{
    "cpu_percent": 23.5,
    "memory": {
        "total": 16777216000,
        "used": 5872025600,
        "percent": 35.0
    },
    "disk": {
        "total": 250685575168,
        "used": 105025527808,
        "percent": 41.9
    }
}
```

### 获取Minecraft服务器状态

请求：

```vbnet
GET /api/status/minecraft
Headers: X-API-KEY: your_secret_key
```

响应：

```json
{
    "host_name": "My Minecraft Server",
    "game_type": "SMP",
    "game_id": "MINECRAFT",
    "version": "1.18.2",
    "plugins": ["Plugin1", "Plugin2"],
    "map": "world",
    "host_port": 25565,
    "player": {
        "num": 2,
        "max": 20,
        "list": ["player1", "player2"]
    }
}
```
### 错误

如果API密钥不匹配或未提供，将收到以下错误响应：  

**403 Forbidden**

```json
{
    "error": "Invalid API key"
}
```
