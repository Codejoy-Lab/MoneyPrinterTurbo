import uvicorn
from loguru import logger
from app.config import config

if __name__ == '__main__':
    logger.info("start server, docs: http://127.0.0.1:" + str(8000) + "/docs")
    uvicorn.run(app="app.asgi:app", host="0.0.0.0", port=8000, reload=config.reload_debug,
                log_level="warning")
