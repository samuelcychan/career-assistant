from jobsearch.search import build_links


def test_keyword_encoded_and_all_sources():
    links = build_links("aosp engineer")
    assert links and all("aosp+engineer" in l["url"] or "aosp%20engineer" in l["url"] for l in links)


def test_asia_filter_and_country():
    links = build_links("aosp", region="asia", countries=["tw"])
    assert links and {l["country"] for l in links} == {"TW"}
    assert any("104.com.tw" in l["url"] for l in links)
