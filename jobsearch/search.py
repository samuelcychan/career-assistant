"""Build job-search links for a keyword across configured sources.

Usage:
    python -m jobsearch.search aosp
    python -m jobsearch.search aosp --region asia --country TW JP
    python -m jobsearch.search aosp --location Taipei --json
"""
import argparse
import json
from urllib.parse import quote_plus

from .sources import SOURCES, Source


def build_links(keyword, location="", region=None, countries=None, sources=SOURCES):
    q, loc = quote_plus(keyword), quote_plus(location)
    wanted = {c.upper() for c in countries} if countries else None
    out = []
    for s in sources:
        if region and s.region != region:
            continue
        if wanted and s.country != "*" and s.country not in wanted:
            continue
        out.append({"source": s.name, "region": s.region, "country": s.country,
                    "url": s.url.format(q=q, loc=loc)})
    return out


def main(argv=None):
    p = argparse.ArgumentParser(description="Generate job-search links.")
    p.add_argument("keyword")
    p.add_argument("--location", default="")
    p.add_argument("--region", choices=["global", "asia"])
    p.add_argument("--country", nargs="+", help="e.g. TW JP KR HK SG MY TH IN")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    links = build_links(a.keyword, a.location, a.region, a.country)
    if a.json:
        print(json.dumps(links, ensure_ascii=False, indent=2))
    else:
        for l in links:
            print(f"[{l['region']}/{l['country']}] {l['source']}: {l['url']}")


if __name__ == "__main__":
    main()
