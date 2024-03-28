def to_hms(seconds: int) -> list:
    
            # Type your code below
    pass
    if isinstance(seconds, int):
        hours = seconds // 3600
        minutes = (seconds%3600) // 60
        seconds = (seconds%3600) %60
        return [hours, minutes, seconds]
    
    else:
        print("Unsupported input type.")
    
    
    
    