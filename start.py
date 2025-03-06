import argparse
import os
import logging
from pathlib import Path
import uvicorn
from app.main import app

def main():
    parser = argparse.ArgumentParser(description='启动FastAPI服务器')
    parser.add_argument('--env', default='dev', choices=['dev', 'prod'], help='运行环境: dev/prod')
    parser.add_argument('--host', default='0.0.0.0', help='监听地址')
    parser.add_argument('--port', type=int, default=8000, help='监听端口')
    parser.add_argument('--log-dir', default='logs', help='日志目录路径')
    args = parser.parse_args()

    # 环境配置
    os.environ['ENV_MODE'] = args.env
    os.environ.setdefault('DATABASE_URL', 'sqlite+aiosqlite:///./test.db')

    # 创建日志目录
    log_dir = Path(args.log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)

    # 配置日志
    logging.basicConfig(
        filename=log_dir/'server.log',
        level=logging.INFO if args.env == 'prod' else logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # 启动参数
    server_config = {
        'host': args.host,
        'port': args.port,
        'reload': args.env == 'dev',
        'workers': 4 if args.env == 'prod' else 1
    }

    uvicorn.run(
        'app.main:app',
        **server_config
    )

if __name__ == '__main__':
    main()