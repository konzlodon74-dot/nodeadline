"""One Line, No Deadline Met — writes a single-line deadline excuse."""

LINE = (
    "I told the deadline I'd be there in five minutes, but my laptop updated, "
    "my Wi-Fi died, and my chair quietly filed for overtime."
)


def main() -> None:
    line = LINE
    assert line.strip(), "line must not be empty or whitespace-only"
    assert "\n" not in line and "\r" not in line, "line must be exactly one line"
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"

    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
