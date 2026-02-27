## Roadmap

These are the next steps to transform the scraper into a Data Engineering project:

### Observability & Reliability (Goal)
- [ ] **Professional Logging:** Replace `print()` with **Loguru** to track script execution with timestamps and color-coded status (INFO, WARNING, ERROR).
- [ ] **Error Handling:** Implement a retry logic for when the website fails to respond.

### Data Scaling
- [ ] **Multi-Source Aggregator:** Expand the script to fetch news from TechCrunch and G1 Technology simultaneously using `asyncio.gather`.
- [ ] **Database Integration:** Move from CSV to **SQLite** storage using `aiosqlite` to prevent duplicate news and keep a historical record.

### Advanced Features
- [ ] **CLI Interface:** Use **Typer** to allow users to choose the output format (JSON/CSV) or the number of news via terminal commands.
- [ ] **Automated Tests:** Add **Pytest** to ensure the HTML parsing logic doesn't break when the website changes its layout.