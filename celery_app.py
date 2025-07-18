from celery import Celery

celery = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery.task
def send_mock_email(email: str):
    import time
    time.sleep(10)
    print(f"Email sent to {email}") 