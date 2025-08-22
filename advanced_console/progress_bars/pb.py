import sys


class ClassicProgressBar:
    """A customizable progress bar for Python console applications."""

    def __init__(self, total, width=50, fill_char="█", empty_char="-",
                 prefix="", suffix="", show_percentage=True, show_bar=True, show_complete_status=False):
        """
        Initialize the progress bar.

        Args:
            total (int): Total number of iterations.
            width (int): Width of the progress bar in characters.
            fill_char (str): Character to use for filled portion.
            empty_char (str): Character to use for empty portion.
            prefix (str): Text to display before the bar.
            suffix (str): Text to display after the bar.
            show_percentage (bool): Whether to show percentage complete.
            show_bar (bool): Whether to show the bar itself.
        """

        self.total = total
        self.width = width
        self.fill_char = fill_char
        self.empty_char = empty_char
        self.prefix = prefix
        self.suffix = suffix
        self.show_percentage = show_percentage
        self.show_bar = show_bar
        self.show_complete_status = show_complete_status
        self.current = 0

    def update(self, value):
        """Update the progress bar with the current value."""
        self.current = value
        self._display()

    def increment(self, step=1):
        """Increment the progress bar by a specified step."""
        self.current += step
        self._display()

    def _display(self):
        """Display the progress bar with brackets around the bar."""
        if self.current > self.total:
            self.current = self.total

        percent = (self.current / self.total) * 100
        filled = int(self.width * self.current // self.total)
        bar = self.fill_char * filled + self.empty_char * (self.width - filled)

        output: list[str] = []
        if self.prefix:
            output.append(self.prefix)
        if self.show_bar:
            output.append(f"[{bar}]")
        if self.show_percentage:
            output.append(f"{percent:.1f}%")
        if self.suffix:
            output.append(self.suffix)
        if self.show_complete_status and self.current >= self.total:
            output.append("   [Complete]")

        sys.stdout.write("\r" + " ".join(output))
        sys.stdout.flush()

        if self.current >= self.total:
            sys.stdout.write("\n")
            sys.stdout.flush()

    def __enter__(self):
        """Support for context manager."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure the progress bar completes cleanly."""
        if self.current < self.total:
            self.update(self.total)
