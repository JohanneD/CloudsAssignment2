import time
from locust import HttpUser, task

class WebsiteUser(HttpUser):
    @task
    def test(self):
        self.client.get("/numbericalintegralservice/0/3.14159")
