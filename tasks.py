from rq.decorators import job
from redis import Redis
import os
import time
from datetime import datetime


redis_conn = Redis.from_url(os.getenv('REDIS_URL', 'redis://localhost:6379/0'))

@job('notifications', connection=redis_conn)
def send_notification(notification_id, email, message):
    print("Starting message id: {notification_id} to {email}...")
    time.sleep(3)
    print("Finished notification id: {notification_id}")
    return {
        "id" : notification_id, 
        "email" : email, 
        "message" : message, 
        "status" : "sent", 
        "sent_at" : datetime.utcnow().isoformat()
        } 

