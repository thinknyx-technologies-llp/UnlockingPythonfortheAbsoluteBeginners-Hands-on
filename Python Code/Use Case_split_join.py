log_entry = "2024-07-28 14:23:45 INFO User login successful"
parts = log_entry.split()
timestamp = f"{parts[0]} {parts[1]}" 
log_level = parts[2]
message = " ".join(parts[3:])
print("Timestamp:", timestamp)
print("Log Level:", log_level)
print("Message:", message)
