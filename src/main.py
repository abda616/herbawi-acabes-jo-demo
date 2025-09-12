import redis
import os

# Environment variables
env_host = os.getenv('ENV_VAR_REDIS', 'localhost')
env_key = os.getenv('ENV_VAR_KEY', 'hello')
env_value = os.getenv('ENV_VAR_VALUE', 'world!')

# Connect to Redis
redis_client = redis.StrictRedis(host=env_host, port=6379)
check_key = redis_client.get(env_key)
# Set a default value if not already set
if not check_key:
    print(f"missing key, setting default value. '{env_key}': {env_value}")
    redis_client.set(env_key, env_value)
else:
    print(f"Value for '{env_key}': {redis_client.get(env_key)}")
