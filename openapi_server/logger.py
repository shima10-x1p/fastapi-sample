import logging
import sys
import functools
import inspect
from logging import Formatter, StreamHandler, Logger
from typing import Optional, Callable, Any
import uuid

class ApiLogger:
    _instance: Optional['ApiLogger'] = None
    _logger: Optional[Logger] = None
    _trace_id: str = ""

    def __new__(cls) -> 'ApiLogger':
        if cls._instance is None:
            cls._instance = super(ApiLogger, cls).__new__(cls)
            cls._instance._initialize_logger()
        return cls._instance

    def _initialize_logger(self) -> None:
        """ロガーの初期化"""
        self._logger = logging.getLogger('ngo-recitation-api')
        self._logger.setLevel(logging.DEBUG)

        # 既存のハンドラーを削除（重複を防ぐ）
        if self._logger.handlers:
            self._logger.handlers.clear()

        # ハンドラーの設定
        handler = StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)

        # フォーマッターの設定
        formatter = Formatter(
            '[%(asctime)s.%(msecs)03d] [%(trace_id)s] (%(levelname)s) <%(caller_func)s>: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)

        # ハンドラーの追加
        self._logger.addHandler(handler)
        
    def set_trace_id(self, trace_id: str) -> None:
        """X-Trace-IDを設定する"""
        self._trace_id = trace_id or str(uuid.uuid4())
        
    def get_trace_id(self) -> str:
        """現在のX-Trace-IDを取得する"""
        if not self._trace_id:
            self._trace_id = str(uuid.uuid4())
        return self._trace_id

    def _log(self, level: int, message: str, func_name: str = '') -> None:
        """内部ログメソッド"""
        if not func_name:
            # 呼び出し元の関数名を取得
            frame = inspect.currentframe()
            if frame:
                caller_frame = frame.f_back.f_back  # 2レベル上のフレームを取得
                if caller_frame:
                    func_name = caller_frame.f_code.co_name
                frame = None  # 循環参照を防ぐ

        self._logger.log(
            level,
            message,
            extra={
                'caller_func': func_name,
                'trace_id': self._trace_id or '-'
            }
        )

    def debug(self, message: str, func_name: str = '') -> None:
        """DEBUGレベルのログを出力"""
        self._log(logging.DEBUG, message, func_name)

    def info(self, message: str, func_name: str = '') -> None:
        """INFOレベルのログを出力"""
        self._log(logging.INFO, message, func_name)

    def warning(self, message: str, func_name: str = '') -> None:
        """WARNINGレベルのログを出力"""
        self._log(logging.WARNING, message, func_name)

    def error(self, message: str, func_name: str = '') -> None:
        """ERRORレベルのログを出力"""
        self._log(logging.ERROR, message, func_name)

    def critical(self, message: str, func_name: str = '') -> None:
        """CRITICALレベルのログを出力"""
        self._log(logging.CRITICAL, message, func_name)


def log_function(level: str = 'INFO'):
    """
    関数の実行をログ出力するデコレータ
    
    Args:
        level (str): ログレベル（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'）
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger = get_logger()
            func_name = func.__name__
            log_method = getattr(logger, level.lower())
            
            # 引数をログ出力（必要に応じて）
            if level.upper() == 'DEBUG':
                args_str = ', '.join([str(arg) for arg in args[1:]])  # self を除外
                kwargs_str = ', '.join([f"{k}={v}" for k, v in kwargs.items()])
                params = f"args: [{args_str}], kwargs: {{{kwargs_str}}}"
                logger.debug(f"Started with {params}", func_name)
            else:
                log_method(f"Started", func_name)
            
            try:
                result = func(*args, **kwargs)
                log_method(f"Completed successfully", func_name)
                return result
            except Exception as e:
                logger.error(f"Failed with error: {str(e)}", func_name)
                raise
            
        return wrapper
    return decorator


# シングルトンインスタンスを取得するための関数
def get_logger() -> ApiLogger:
    """ロガーインスタンスを取得"""
    return ApiLogger()