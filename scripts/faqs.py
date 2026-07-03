"""Collect and render FAQs for the site."""

FAQ_PAGE_SLUGS = {"en": "safety", "hr": "sigurnost"}


def collect_all_faqs(pages: list[dict]) -> list[dict]:
    """Gather unique FAQs from every landing page, preserving first-seen order."""
    seen: set[str] = set()
    collected: list[dict] = []
    for page in pages:
        for faq in page.get("faqs", []):
            question = faq["q"].strip()
            if question in seen:
                continue
            seen.add(question)
            collected.append(faq)
    return collected
