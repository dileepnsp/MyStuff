import requests

ALL_KEY_FIELDS = [
    # Identifiers
    "ValorNumber", "ValorSymbol", "ISIN", "NSIN",
    # Names
    "ShortName", "SecDescriptionFull", "IssuerNameShort", "IssuerNameFull",
    # Industry/Sector
    "ICBIndustry", "ICBIndustryDesc", "ICBSupersector", "ICBSupersectorDesc",
    "IndustrySectorCode", "IndustrySectorDesc",
    "RBSSEconomicSector", "RBSSEconomicSectorDesc",
    "RBSSIndustry", "RBSSIndustryDesc",
    # Classification
    "SecurityType", "SecTypeDesc", "InstrumentTypeCode",
    "ProductLine", "ProductLineDesc", "PortalSegment",
    "ListingSegment", "ListingSegmentDesc",
    # Geography
    "GeographicalAreaCode", "GeographicalAreaDesc",
    # Currency
    "TradingBaseCurrency", "NominalCurrency",
    # Share data
    "NumberInIssue", "TotalShares", "FreeFloatShares", "FreeFloatFraction",
    "NominalValue",
    # Prices
    "ClosingPrice", "PreviousClosingPrice", "ClosingDelta",
    "YearlyHighPrice", "YearlyLowPrice",
    # Dates
    "FirstTradingDate", "LastTradingDate",
    # Dividends
    "DividendEntitlementFlag", "ExDividendDate",
    # Market cap
    "TotalMarketCap", "TotalMarketCapCHF",
    # Ratios
    "APENORM", "AROEPCT", "ADIVSHR", "AEPSNORM",
    # External IDs
    "BloombergLocalSymbol", "ReutersLocalRIC",
    "TradingState",
]

def get_full_profile(valoren: str) -> dict:
    resp = requests.get(
        "https://www.six-group.com/fqs/ref.json",
        params={
            "select": ",".join(ALL_KEY_FIELDS),
            "where": f"valoren={valoren}"
        },
        timeout=15
    )
    resp.raise_for_status()
    data = resp.json()
    return data[0] if data else {}

# Example: Nestle
profile = get_full_profile("3886355")
for k, v in profile.items():
    if v:
        print(f"{k:35s} = {v}")
