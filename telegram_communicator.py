from logger_level import LoggerLevel
import logger


class TelegramCommunicator:
    def init(self, token: str, allowed_client_ids: list[int], log_path: str = ""):
        self.base_url = f"https://api.telegram.org/bot{token}"
        self.allowed_client_ids = allowed_client_ids

    def try_send_message(self, client_id: int, message: str) -> bool:
        if client_id not in self.allowed_client_ids:
            msg = f"Sending to not allowed client, id = {client_id}"
            print(msg)
            return False

        return True
