import typing as tp

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class Session:
    """
    Сессия.
    :param base_url: Базовый адрес, на который будут выполняться запросы.
    :param timeout: Максимальное время ожидания ответа от сервера.
    :param max_retries: Максимальное число повторных запросов.
    :param backoff_factor: Коэффициент экспоненциального нарастания задержки.
    """

    import requests

    class HTTPClient:
        def __init__(self, base_url: str, timeout: float = 5.0) -> None:
            self.base_url = base_url
            self.timeout = timeout
            self.session = requests.Session()

        def get(self, url: str, *args: tp.Any, **kwargs: tp.Any) -> requests.Response:
            url = f"{self.base_url}/{url}"
            response = self.session.get(url, params=kwargs, timeout=self.timeout)
            return response

        def post(self, url: str, *args: tp.Any, **kwargs: tp.Any) -> requests.Response:
            url = f"{self.base_url}/{url}"
            response = self.session.post(url, data=kwargs, timeout=self.timeout)
            return response

