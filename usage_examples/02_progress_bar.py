import time

from advanced_console.progress_bars import ClassicProgressBar


total_iterations = 100
with ClassicProgressBar(total=total_iterations, width=35, fill_char="#", prefix="Downloading: ",
                        suffix="", show_complete_status=True) as pb:
    for i in range(total_iterations):
        time.sleep(0.06)  # Simulate work
        pb.increment()
