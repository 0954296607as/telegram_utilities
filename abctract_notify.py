from abc import ABC, abstractmethod
import time


class Notify(ABC):
    def start_nofify(self, client_id: int, task_name: str):
        self.try_send_message(client_id, f"Start {task_name}")

    def end_notify(self, client_id: int, task_name: str, duration: float = 0.0):
        msg = f"End: {task_name}."
        if duration:
            msg += f" Duration: {duration:.1f} sek."
        self.try_send_message(client_id, msg)

    def notify_error(self, client_id: int, error: str):
        return self.try_send_message(client_id, f"Error: {error}")

    def heartbeat(self, client_id: int, interval: int = 600):
        self.try_send_message(client_id, f"Working... time pass {interval // 60} min.")
        time.sleep(interval)

    @abstractmethod
    def try_send_message(self, client_id: int, msg: str) -> bool:
        pass
