import redis

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379)
print(redis_client.get("hello"))

# # Example data to simulate Redis keys and values
# redis_client.set("user:1", "Alice")
# redis_client.set("user:2", "Bob")
# redis_client.set("user:3", "Charlie")

# # **1. Caching with a Dictionary**
# cache_dict = {}

# def get_data_with_dict_cache(key):
#     if key in cache_dict:
#         print(f"Cache hit for key: {key}")
#         return cache_dict[key]
#     else:
#         print(f"Cache miss for key: {key}")
#         value = redis_client.get(key)
#         if value:
#             cache_dict[key] = value  # Store in cache
#         return value

# # Fetch data using dictionary cache
# print(get_data_with_dict_cache("user:1"))  # Cache miss
# print(get_data_with_dict_cache("user:1"))  # Cache hit

# # **2. Caching with a List**
# cache_list = []

# def get_data_with_list_cache(key):
#     for item in cache_list:
#         if item['key'] == key:
#             print(f"Cache hit for key: {key}")
#             return item['value']
#     print(f"Cache miss for key: {key}")
#     value = redis_client.get(key)
#     if value:
#         cache_list.append({'key': key, 'value': value})  # Store in cache
#     return value

# # Fetch data using list cache
# print(get_data_with_list_cache("user:2"))  # Cache miss
# print(get_data_with_list_cache("user:2"))  # Cache hit
