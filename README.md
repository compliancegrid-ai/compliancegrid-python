# ComplianceGrid Python SDK

Official Python SDK for the [ComplianceGrid API](https://www.compliancegrid.ai) — export compliance, sanctions screening, HS codes, and 12+ regulatory domains.

## Installation

```bash
pip install compliancegrid
```

## Quick Start

```python
from compliancegrid import ComplianceGrid

cg = ComplianceGrid(api_key="cg_sk_your_sandbox_key_here")

# Screen a party against all federal watchlists
result = cg.compliance.screen_parties([
    {"name": "Acme Trading Co", "country": "CN", "type": "CONSIGNEE"}
])
print(result["data"]["summary"])

# Classify an HS code
hs = cg.hs.classify(description="stainless steel kitchen knives")
print(hs["data"]["classifications"])

# Search FFL holders in Texas
ffls = cg.firearms.search_ffl(state="TX", city="Houston", limit=10)
print(ffls["data"]["results"])
```

## Authentication

ComplianceGrid uses API keys for authentication:

| Key Prefix | Environment | Endpoint |
|-----------|-------------|----------|
| `cg_sk_…` | Sandbox (mock data) | `sandbox.api.compliancegrid.ai` |
| `cg_pk_…` | Production (real data) | `api.compliancegrid.ai` |

The SDK **automatically routes** requests to the correct endpoint based on your key prefix.

Get your keys at [compliancegrid.ai/dashboard/developer](https://www.compliancegrid.ai/dashboard/developer).

## Available APIs

| Module | Description |
|--------|-------------|
| `cg.compliance` | Restricted party screening, prohibited goods, export license, HS classification |
| `cg.aes` | AES filing validation, preparation, and submission |
| `cg.hs` | HTS code search, AI classification, lookup, reference data |
| `cg.firearms` | ATF FFL search, verification, parsing, reference data |
| `cg.pharma` | DEA registration lookup, FDA drug search, shortages, recalls |
| `cg.financial` | SEC EDGAR, FDIC BankFind, FINRA BrokerCheck |
| `cg.aviation` | FAA aircraft registry, FMCSA carrier safety |
| `cg.maritime` | Vessel search, C-TPAT partner lookup |
| `cg.business` | SAM.gov entity search |
| `cg.legal` | OIG LEIE exclusion search |
| `cg.fcc` | FCC ULS license search |
| `cg.ai` | AI compliance assistant (powered by Claude) |

## Examples

### Restricted Party Screening

```python
result = cg.compliance.screen_parties([
    {"name": "Huawei Technologies", "type": "OTHER"},
    {"name": "Acme Corp", "country": "DE", "type": "CONSIGNEE"},
])

for r in result["data"]["results"]:
    print(f"{r['party']['name']}: {r['status']} ({r['matchCount']} matches)")
```

### HS Code Search

```python
result = cg.hs.search("laptop computer")
for item in result["data"]["results"]:
    print(f"{item['htsNumber']} — {item['description']} (Duty: {item['general']})")
```

### DEA Registration Lookup

```python
dea = cg.pharma.lookup_dea("BJ1234563")
print(dea["data"]["name"], dea["data"]["schedules"])
```

### SEC EDGAR Search

```python
sec = cg.financial.search_sec("Apple Inc")
print(sec["data"]["results"][0]["cik"], sec["data"]["results"][0]["ticker"])
```

### AI Compliance Assistant

```python
chat = cg.ai.chat([
    {"role": "user", "content": "What HS code applies to stainless steel kitchen knives from China?"}
])
print(chat["data"]["reply"])
print("Tools used:", [t["name"] for t in chat["data"]["toolsUsed"]])
```

### FAA Aircraft Search

```python
aircraft = cg.aviation.search_aircraft(manufacturer="cessna", state="WI")
print(aircraft["data"]["results"])
```

### Vessel Search

```python
vessels = cg.maritime.search_vessels(name="Ever Given")
print(vessels["data"]["results"])
```

## Error Handling

```python
from compliancegrid import ComplianceGrid, ApiError

cg = ComplianceGrid(api_key="cg_sk_your_key")

try:
    cg.compliance.screen_parties([{"name": "Test"}])
except ApiError as e:
    print(f"API Error {e.status_code}: [{e.code}] {e}")
```

## Context Manager

```python
with ComplianceGrid(api_key="cg_sk_your_key") as cg:
    result = cg.compliance.screen_parties([{"name": "Test Corp"}])
    print(result)
# HTTP client automatically closed
```

## Configuration

```python
cg = ComplianceGrid(
    api_key="cg_pk_your_production_key",
    base_url="https://api.compliancegrid.ai",  # optional override
    timeout=60.0,                                # optional, default 30s
)
```

## Requirements

- Python 3.9+
- [httpx](https://www.python-httpx.org/) (installed automatically)

## License

MIT — [ComplianceGrid](https://www.compliancegrid.ai)
