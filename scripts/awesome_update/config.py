"""Configuration for awesome list auto-update agent."""
import os

# GitHub API Configuration
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO_OWNER = "vivy-yi"
REPO_NAME = "awesome-openclaw"

# Search Keywords
SEARCH_KEYWORDS = [
    "openclaw",
    "moltbot",
    "clawdbot",
    "ai-agent",
    "claude-agent",
    "llm-agent",
    "autonomous-agent",
]

# Categories to scan on GitHub
TRENDING_CATEGORIES = [
    "ai",
    "agent",
    "bot",
    "llm",
]

# Quality thresholds
MIN_STARS = 10
MAX_AGE_DAYS = 180  # Skip repos with no commits in 6 months

# Output
REPORT_TEMPLATE = "daily_update_report.md"
