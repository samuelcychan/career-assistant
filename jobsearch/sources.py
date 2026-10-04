"""Job-search sources: URL templates keyed by region.

`{q}` is the URL-encoded keyword, `{loc}` the URL-encoded location.
Sources are search-page links (no scraping, no API keys needed).
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Source:
    name: str
    region: str  # "global" | "asia"
    country: str  # ISO-ish code or "*"
    url: str


SOURCES = [
    # --- Global / US ---
    Source("LinkedIn", "global", "*", "https://www.linkedin.com/jobs/search/?keywords={q}&location={loc}"),
    Source("Indeed US", "global", "US", "https://www.indeed.com/jobs?q={q}&l={loc}"),
    Source("Glassdoor", "global", "*", "https://www.glassdoor.com/Job/jobs.htm?sc.keyword={q}"),
    Source("ZipRecruiter", "global", "US", "https://www.ziprecruiter.com/jobs-search?search={q}&location={loc}"),
    Source("SimplyHired", "global", "US", "https://www.simplyhired.com/search?q={q}&l={loc}"),
    Source("Dice", "global", "US", "https://www.dice.com/jobs?q={q}&location={loc}"),
    Source("DevJobsScanner", "global", "*", "https://www.devjobsscanner.com/search/?q={q}"),
    # --- Asia ---
    Source("104 人力銀行", "asia", "TW", "https://www.104.com.tw/jobs/search/?keyword={q}"),
    Source("1111 人力銀行", "asia", "TW", "https://www.1111.com.tw/search/job?ks={q}"),
    Source("Cake (CakeResume)", "asia", "TW", "https://www.cake.me/jobs/{q}"),
    Source("Indeed TW", "asia", "TW", "https://tw.indeed.com/jobs?q={q}&l={loc}"),
    Source("Indeed JP", "asia", "JP", "https://jp.indeed.com/jobs?q={q}&l={loc}"),
    Source("Green (Japan)", "asia", "JP", "https://www.green-japan.com/search_key?keyword={q}"),
    Source("Indeed KR", "asia", "KR", "https://kr.indeed.com/jobs?q={q}&l={loc}"),
    Source("Saramin", "asia", "KR", "https://www.saramin.co.kr/zf_user/search?searchword={q}"),
    Source("JobKorea", "asia", "KR", "https://www.jobkorea.co.kr/Search/?stext={q}"),
    Source("Indeed HK", "asia", "HK", "https://hk.indeed.com/jobs?q={q}&l={loc}"),
    Source("JobsDB HK", "asia", "HK", "https://hk.jobsdb.com/{q}-jobs"),
    Source("Indeed SG", "asia", "SG", "https://sg.indeed.com/jobs?q={q}&l={loc}"),
    Source("JobStreet SG", "asia", "SG", "https://sg.jobstreet.com/{q}-jobs"),
    Source("JobStreet MY", "asia", "MY", "https://my.jobstreet.com/{q}-jobs"),
    Source("JobsDB TH", "asia", "TH", "https://th.jobsdb.com/{q}-jobs"),
    Source("Indeed IN", "asia", "IN", "https://in.indeed.com/jobs?q={q}&l={loc}"),
    Source("Naukri", "asia", "IN", "https://www.naukri.com/{q}-jobs"),
]
