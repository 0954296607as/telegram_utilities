from abctract_notify import Notify
import logger
import requests


class TelegramCommunicator(Notify):
    def init(self, token: str, allowed_client_ids: list[int]):
        self.base_url = f"https://api.telegram.org/bot{token}"
        self.allowed_client_ids = allowed_client_ids
        self._log = logger.Logger()

    def try_send_message(self, client_id: int, message: str) -> bool:
        if client_id not in self.allowed_client_ids:
            msg = f"Sending to not allowed client, id = {client_id}"
            self._log.warn(msg)
            return False

        try:
            resp = requests.post(
                f"{self.base_url}/sendMessage",
                data={"chat_id": client_id, "text": message},
                timeout=10,
            )
            if resp.status_code == 200:
                msg = f"[{client_id}] Succses: {message[:60]}..."
                self._log.info(msg)
                return True
            else:
                status = f"HTTP {resp.status_code}: {resp.text}"
                msg = f"Error Telegram API : {status}"
                self._log.error(msg)
        except Exception as err:
            msg = f"Error connection with Telegram: {err}"
            self._log.error(msg)

        return True
