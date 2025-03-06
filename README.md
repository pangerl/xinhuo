# XinhAPI 项目文档

## 项目概述
基于FastAPI构建的RESTful API服务，集成SQLAlchemy ORM和Dependency Injector依赖注入框架。支持用户管理基础功能，采用异步SQLite数据库。

## 技术栈
- Python 3.12
- FastAPI
- SQLAlchemy 2.0
- Dependency Injector
- Uvicorn
- aiosqlite

## 系统功能模块
### 用户管理模块
- 用户注册/查询
- 用户信息维护
- 激活状态管理

### 数据库模块
- 异步SQLite连接池
- 声明式ORM模型
- 依赖注入会话管理

## 环境配置
### 开发环境
```bash
pipenv install
pipenv run python start.py --env dev
```

### 生产环境
```bash
pipenv install --deploy
pipenv run python start.py --env prod --workers 4
```

## 部署配置
### Docker部署
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install pipenv && pipenv install --deploy
EXPOSE 8000
CMD ["pipenv", "run", "python", "start.py", "--env", "prod"]
```

### 环境变量
| 变量名         | 默认值                          | 说明               |
|----------------|--------------------------------|--------------------|
| ENV_MODE       | dev                            | 运行环境           |
| DATABASE_URL   | sqlite+aiosqlite:///./test.db | 数据库连接字符串   |

## API文档访问
- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

## 启动参数对比表
| 参数      | 开发环境 | 生产环境 | 说明                  |
|-----------|----------|----------|-----------------------|
| --env     | dev      | prod     | 运行环境              |
| --reload  | ✓        | ✗        | 热重载                |
| --workers | 1        | 4        | 工作进程数            |
| --log-dir | logs     | logs     | 日志目录              |
