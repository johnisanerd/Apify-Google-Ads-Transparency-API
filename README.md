# 📢 Google Ads Transparency API: a competitor's ad library as clean JSON

> The most efficient, reliable, and developer-friendly way to use the Google Ads Transparency API.

**Actor page:** [apify.com/johnvc/google-ads-transparency-api](https://apify.com/johnvc/google-ads-transparency-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/google-ads-transparency-api/input-schema](https://apify.com/johnvc/google-ads-transparency-api/input-schema?fpr=9n7kx3)

List any advertiser's ads from the Google Ads Transparency Center as structured JSON. Give the API an advertiser ID and get the ads they are running, each with its format, the dates it was first and last shown, the total days it has run, and a preview link. It is a competitor ad library for growth teams, agencies, and AI marketing agents, pay-as-you-go.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Google-Ads-Transparency-API.git
   cd Apify-Google-Ads-Transparency-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run an example**
   ```bash
   # Single example:
   uv run python google-ads-transparency-api-example.py

   # Batch example (pulls several advertisers' ad libraries in one run):
   uv run python google-ads-transparency-api-batch-example.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python google-ads-transparency-api-example.py
```

## Why Use This Google Ads Transparency API?

Build a competitor ad library. One advertiser ID returns the ads a rival is running, with how long each has been live.

Clean, structured output. Every ad is one row, ready to load into a dataframe, a database, or an AI pipeline.

Spot the winners. Long run times signal ads that are working; the format mix shows where a competitor invests.

MCP-ready. AI agents can call it as a tool through the hosted Apify MCP server to analyze a competitor's creative strategy.

## Features

### Core Capabilities
- An advertiser's full ad library from one ID
- Ad format (text, image, video) and run dates
- Total days each ad has run
- Batch several advertisers in one run

### Data Quality
- One clean row per ad, with a preview link
- Stable JSON shape, easy to load anywhere

## Usage Examples

### Basic Example
```json
{
  "advertiserId": "AR01614014350098432001"
}
```

### Advanced Example
```json
{
  "advertiserIds": ["AR01614014350098432001", "AR13614460755715375105"],
  "maxResultsPerAdvertiser": 100
}
```

For a runnable batch script, see `google-ads-transparency-api-batch-example.py` in this repo.

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `advertiserId` | `str` | one of | - | A single advertiser ID, the AR... code in a Google Ads Transparency Center URL. |
| `advertiserIds` | `list[str]` | one of | - | A batch of advertiser IDs. Merged with `advertiserId` and de-duplicated. |
| `region` | `str` | no | - | Optional region filter. Leave blank for ads shown anywhere. |
| `maxResultsPerAdvertiser` | `int` | no | `50` | Ads per advertiser (maximum 500). |

To get an advertiser ID, open the advertiser on the Google Ads Transparency Center; the AR... code is in the URL.

## Output Format

Each item in the dataset is one ad:

```json
{
  "result_type": "ad",
  "advertiser_id": "AR01614014350098432001",
  "position": 1,
  "ad_creative_id": "CR08181256642625536001",
  "advertiser": "lululemon athletica canada inc.",
  "format": "video",
  "first_shown": 1731000000,
  "last_shown": 1748700000,
  "total_days_shown": 204,
  "link": "https://displayads-formats.googleusercontent.com/ads/preview/...",
  "details_link": "https://adstransparency.google.com/advertiser/AR01614014350098432001/creative/CR08181256642625536001"
}
```

---

<!-- The five install sections below are the canonical MCP install copy. -->
## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Google Ads Transparency API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/google-ads-transparency-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Google Ads Transparency API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

---

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/google-ads-transparency-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/google-ads-transparency-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Google Ads Transparency API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

---

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/google-ads-transparency-api`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/google-ads-transparency-api`, using OAuth when prompted.
5. Ask Claude to run the Google Ads Transparency API.

Open Claude on the web: https://claude.ai

---

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/google-ads-transparency-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/google-ads-transparency-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Google Ads Transparency API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

---

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/google-ads-transparency-api`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Google Ads Transparency API to build competitor ad libraries in your product or AI agent.*

Last Updated: 2026.06.21
