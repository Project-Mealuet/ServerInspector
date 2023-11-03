# Mealuet Server Inspector

A simple API implementation based on `flask`, used for obtaining server performance data and Minecraft server parameters.

# Setup

- Before running, ensure all dependencies are installed:
    ```bash
    pip3 install -r requirements.txt
    ```

- The environment variable `SECRET_KEY` must be set:
    ```bash
    echo 'SECRET_KEY="your_secret_key"' > .env
    ```

- The API is designed to run on the **same machine** as the Minecraft server, to monitor the server's CPU and memory usage.  
- If you need to run the API on another machine, please modify the `host` in `main.py`.
- Configure `server.properties`:
    ```properties
    enable-query=true
    query.port=25585
    ```
- Start the API server:
    ```bash
    python3 main.py
    ```
- ⚠ ***Note: The API server defaults to port `25595`. It is strongly recommended to configure a reverse proxy and set up SSL. Configuration examples can be found in `examples`.***

# Usage

## Environment Variables:

`SECRET_KEY`: Used for API authorization.

## Endpoints:

1. Get system status (GET /api/status/system)  
2. Get Minecraft server status (GET /api/status/minecraft)

## Request Headers:

`X-API-KEY`: API key, which must match the set `SECRET_KEY`.

## Responses:

1. `GET /api/status/system` returns the CPU usage percentage, memory total, memory used, memory usage percentage, as well as disk total, disk used, and disk usage percentage.
2. `GET /api/status/minecraft` returns the status of the Minecraft server, including host name, game type, game ID, version, plugins, map, host port, and the number of players, maximum players, and player list.

## Examples

### Get System Status

Request:

```vbnet
GET /api/status/system
Headers: X-API-KEY: your_secret_key
```

Response: 

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

### Get Minecraft Server Status

Request:

```vbnet
GET /api/status/minecraft
Headers: X-API-KEY: your_secret_key
```

Response:

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
### Errors

If the API key does not match or is not provided, you will receive the following error response: 

**403 Forbidden**

```json
{
    "error": "Invalid API key"
}
```