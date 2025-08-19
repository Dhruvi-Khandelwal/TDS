import itertools
import time

import os

# Read environment variables
api_key1 = os.getenv("GOOGLE_API_KEY")
api_key2 = os.getenv("GOOGLE_API_KEY2")
api_key3 = os.getenv("GOOGLE_API_KEY3")

# Initialize with empty list
API_KEYS = [
     {"key": "AIzaSyAFoEHTEOj6pZrJIgl0ZbKHLOGR-fbsxWc", "req_timestamps": []},
        {"key": "AIzaSyB95M_D1qXL8-WQ9QX968zQviqaO6udkG8", "req_timestamps": []},
        {"key": "AIzaSyCMpGyo7EkwcpsxgZwHkn4JvqRtlfAl1FQ", "req_timestamps": []}
]

# Add environment API keys if they exist
for api_key in [api_key1, api_key2, api_key3]:
    if api_key:
        print("API Key found and added to rotation")
        API_KEYS.append({"key": api_key, "req_timestamps": []})        
    else:
        print("API Key not set in environment variables")

# If no environment variables are set, you can add fallback keys here
# WARNING: Remove these hardcoded keys before deploying to production
if not API_KEYS:
    print("No API keys found in environment variables. Using fallback keys.")
    API_KEYS = [
        {"key": "AIzaSyAFoEHTEOj6pZrJIgl0ZbKHLOGR-fbsxWc", "req_timestamps": []},
        {"key": "AIzaSyB95M_D1qXL8-WQ9QX968zQviqaO6udkG8", "req_timestamps": []},
        {"key": "AIzaSyCMpGyo7EkwcpsxgZwHkn4JvqRtlfAl1FQ", "req_timestamps": []}
    ]

if not API_KEYS:
    raise ValueError("No API keys available. Please set GOOGLE_API_KEY environment variables.")
        
key_cycle = itertools.cycle(API_KEYS)
MAX_REQS_PER_MIN = 5


def cleanup_usage(key_info):
    """Remove requests older than 60s."""
    now = time.time()
    key_info["req_timestamps"] = [
        t for t in key_info["req_timestamps"] if now - t < 60
    ]


def get_api_key(auto_wait=True):
    """Return an API key that has quota. Waits if needed."""
    while True:
        for _ in range(len(API_KEYS)):
            key_info = next(key_cycle)
            cleanup_usage(key_info)

            if len(key_info["req_timestamps"]) < MAX_REQS_PER_MIN:
                key_info["req_timestamps"].append(time.time())
                return key_info["key"]

        if auto_wait:
            # Find soonest timestamp that will expire
            next_free_time = min(
                min(k["req_timestamps"]) for k in API_KEYS if k["req_timestamps"]
            )
            sleep_for = max(0, 60 - (time.time() - next_free_time))
            print(f"⏳ All keys exhausted. Waiting {sleep_for:.1f}s...")
            time.sleep(sleep_for + 0.1)
        else:
            raise RuntimeError("🚨 All API keys hit 5 req/min limit")
