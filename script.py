import pyautogui
import time

def auto_clicker(interval, duration):
   
    start_time = time.time()
    while time.time() - start_time < duration:
        pyautogui.click()  
        time.sleep(interval)  
        
if __name__ == "__main__":
    # Customize the interval between clicks and duration
    interval_between_clicks = 0.1  # Interval in seconds between clicks
    click_duration = 60  # Total duration in seconds for auto-clicker to run
    
    print(f"Auto-clicker will run for {click_duration} seconds with an interval of {interval_between_clicks} seconds.")
    
    time.sleep(3)  # Give yourself 3 seconds to position the mouse
    auto_clicker(interval_between_clicks, click_duration)
