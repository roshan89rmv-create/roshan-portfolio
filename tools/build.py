"""Builds the portfolio: index.html plus one page per case file in case/.

To add a case file, add an entry to CASES below and run:
    python3 tools/build.py
The order of CASES sets the order on the home page and the "Next case file" links.
"""
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINKEDIN = "https://www.linkedin.com/in/roshanmaryvarghese"
EMAIL = "roshan89.rmv@gmail.com"
INSTAGRAM = "https://instagram.com/nearlyroshan"

CASES = [
    {
        "slug": "claim-denial-decoder",
        "title": "Claim Denial Decoder",
        "year": "2026",
        "type": "Side project",
        "impact": "Turns cryptic health insurance rejection codes into plain-English next steps for patients and clinic staff.",
        "live": "https://claude.ai/artifact/KUER2xqjB1SmEMi6YyPpWi",
        "img": "claim-denial-decoder.webp",
        "img_alt": "Claim Denial Decoder explaining rejection code NCOV-003: what it means, why it happens and what to do next",
        "stack": "HTML, CSS, JavaScript, public payer adjudication guidelines, Claude",
        "for_whom": "Patients and clinic billing teams",
        "problem": [
            "Rejected claims come back with short codes such as MNEC-004 that most patients, and many clinic staff, can't read. People are left confused, chase the wrong person, or pay bills they may not owe.",
            "I handled these rejections for six years in GCC health insurance. The rules behind each code are public, but they're written for adjudicators, not for the person holding the bill.",
        ],
        "built_intro": "A one-page tool. Paste a rejection code or message, or tap a common reason, and it explains the rejection in three parts.",
        "built": [
            "What the rejection means, in one or two plain sentences.",
            "Why it usually happens, so people know whether it's a paperwork problem or a coverage problem.",
            "What to do next, plus a folded note with the technical fix for clinic billing teams.",
        ],
        "approach": [
            ("User", "Patients come first and billing teams second. The plain-language answer leads, and the coding fix sits in a fold labelled for clinic billing teams so it never crowds the patient view."),
            ("Constraints", "Rejection codes differ by market. I based the codes on UAE-style codes from Daman's public adjudication guidelines, and added free-text matching so someone outside the UAE can type the reason in their own words."),
            ("Trade-offs", "I covered the 12 most common rejection reasons well rather than every code thinly. When it matches from words rather than a code, it says it's a best guess and shows each likely reason."),
        ],
        "shows": "I can turn insider claims knowledge into a product a non-expert can use without help.",
    },
    {
        "slug": "gulf-chronic-disease-watch",
        "title": "Gulf Chronic Disease Watch",
        "year": "2026",
        "type": "Data project",
        "impact": "Separates real chronic disease trends in the Gulf from noise, using the WHO's own uncertainty ranges.",
        "live": "https://claude.ai/artifact/Adyt7ckMZNwcC1VpwRYuEr",
        "img": "gulf-chronic-disease-watch.webp",
        "img_alt": "Line chart of adult obesity in six Gulf states and India from 2000 to 2024, with WHO uncertainty bars",
        "stack": "WHO Global Health Observatory API, Python, Chart.js, HTML, CSS, Claude",
        "for_whom": "Population health and payer teams",
        "problem": [
            "Health headlines about the Gulf quote diabetes and obesity rates without the error bars behind them. Some of the changes people cite fall inside the WHO's own uncertainty range, so the data can't confirm them.",
            "Population health teams and insurers who plan around those numbers risk acting on changes that may not be real.",
        ],
        "built_intro": "An interactive dashboard covering five indicators across the six GCC states and India, from 2000 to the latest WHO estimate.",
        "built": [
            "A \"what moved\" grid that marks each change as a clear rise, a clear fall, or within uncertainty.",
            "A trend explorer with uncertainty bars, a pandemic anomaly check, and a payer view of diabetes treatment coverage.",
            "Seven data quirks, written up in plain language, that change how the numbers should be read.",
        ],
        "approach": [
            ("User", "People who need to know which shifts are real before they act. So the first thing on the page is a verdict for each country and indicator, not a chart to decode."),
            ("Constraints", "WHO figures are model estimates with wide ranges. A change only counts as clear when the 2000 and latest ranges don't overlap, and I checked all 35 data series against the raw API."),
            ("Trade-offs", "I used a z-score anomaly test only for premature deaths. On the smooth, modelled series it would flag almost every year, so I documented that limit instead of showing misleading flags."),
        ],
        "shows": "I question data before I trust it, and I explain its limits as clearly as its findings.",
    },
    {
        "slug": "dubai-health-money-radar",
        "title": "Dubai Health Money Radar",
        "year": "2026",
        "type": "Live tracker, updated weekly",
        "impact": "A weekly, plain-English record of who pays for healthcare in Dubai and what just changed.",
        "live": "https://claude.ai/artifact/7PYZqPuVy4tv63mTWiH6Y8",
        "img": "dubai-health-money-radar.webp",
        "img_alt": "Dubai Health Money Radar: a header, three start-here cards and a radar chart of updates by topic and age",
        "stack": "HTML, CSS, JavaScript, SVG, a scheduled weekly research task, Claude",
        "for_whom": "Residents and the health industry",
        "problem": [
            "Changes to health insurance rules, public budgets and new health bodies in Dubai are spread across laws, press releases and news sites.",
            "Residents can't easily tell what affects their cover. People building health products miss shifts that change their market.",
        ],
        "built_intro": "A tracker that refreshes itself every Monday and explains each change in one place.",
        "built": [
            "A radar chart that plots every update by topic and age, next to a spotlight on the newest change.",
            "A feed where each update has one line for residents and one for the industry, with its source linked.",
            "Reference views: a money map, a diagram of who pays whom, the rules in force today, and a comparison with the US system.",
        ],
        "approach": [
            ("User", "Two audiences with different questions. Rather than two products, each update carries a \"for residents\" line and a \"for the industry\" line, and a filter shows what matters to each reader."),
            ("Constraints", "Only confirmed changes go in, each with a source. Every item is labelled as in force or announced, because announced reforms often change before they land."),
            ("Trade-offs", "It updates weekly, not daily. Fewer, verified items are more useful than a noisy feed, and I review each week's changes."),
        ],
        "shows": "I can design for two audiences at once and keep a product honest about what's confirmed.",
    },
    {
        "slug": "biopharma-deal-radar",
        "title": "Biopharma Deal Radar",
        "year": "2026",
        "type": "Live tracker, updated weekly",
        "impact": "Explains who is buying whom in medicine across the USA, India and the Gulf, for people outside the industry.",
        "live": "https://claude.ai/artifact/CHbfJAABRZAxzf44hTQ5EE",
        "img": "biopharma-deal-radar.webp",
        "img_alt": "Biopharma Deal Radar: a big-picture summary, headline numbers and region cards for the USA, India and the UAE and Gulf",
        "stack": "HTML, CSS, JavaScript, embedded JSON data, a scheduled weekly research task, Claude",
        "for_whom": "Non-specialists and career switchers",
        "problem": [
            "Pharma deal news is written for investors, with terms such as \"up to $7B\", ADCs and in vivo CAR-T.",
            "People moving into health tech, life sciences or payer roles can't easily see the patterns: who is buying, what they want, and why it matters for patients and costs.",
        ],
        "built_intro": "A filterable board of 80+ pharma and biotech deals that adds new deals every Monday.",
        "built": [
            "Deal cards that say who did what, what the company makes and why it matters, filterable by region, type and health area.",
            "Charts of the biggest deals and busiest buyers, plus a plain-English table of who competes with whom.",
            "A quiz, talking points and a word list, so readers can use what they learn in a conversation.",
        ],
        "approach": [
            ("User", "Non-specialists preparing for interviews and conversations. That's why it has talking points and a quiz, not just a data table."),
            ("Constraints", "Headline deal values often include future \"up to\" payments that may never be paid. The page says so, and the word list explains upfront versus \"up to\"."),
            ("Trade-offs", "I narrowed it to three regions, the USA, India and the UAE and Gulf, and removed Europe, so each region stays deep enough to be useful."),
        ],
        "shows": "I can translate a technical market into plain language without losing accuracy.",
    },
]

MARK = ('<svg width="30" height="30" viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="14" fill="#0D3B42"/>'
        '<path d="M14 64V34a18 18 0 0 1 36 0v30" fill="#8ED1CB"/><circle cx="46" cy="18" r="7" fill="#EFA53A"/></svg>')
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230D3B42'/%3E"
           "%3Cpath d='M14 64V34a18 18 0 0 1 36 0v30' fill='%238ED1CB'/%3E%3Ccircle cx='46' cy='18' r='7' fill='%23EFA53A'/%3E%3C/svg%3E")
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700;12..96,800'
         '&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap" rel="stylesheet">')


def head(title, desc, prefix, og_img):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{prefix}img/{og_img}">
<link rel="icon" href="{FAVICON}">
{FONTS}
<link rel="stylesheet" href="{prefix}site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>"""


def bar(prefix, nav):
    links = "".join(f'<a href="{href}">{e(label)}</a>' for label, href in nav)
    return f"""
<header class="bar" id="bar">
  <div class="wrap">
    <a class="mark" href="{prefix}index.html" aria-label="Roshan Mary Varghese, home">{MARK}<span class="full">Roshan Mary Varghese</span></a>
    <nav aria-label="Sections">{links}</nav>
  </div>
</header>"""


def case_page(i, c):
    nxt = CASES[(i + 1) % len(CASES)]
    n, total = i + 1, len(CASES)
    problem = "".join(f"<p>{e(p)}</p>" for p in c["problem"])
    built = "".join(f"<li>{e(b)}</li>" for b in c["built"])
    approach = "".join(f'<li class="card"><b>{e(k)}</b><span>{e(v)}</span></li>' for k, v in c["approach"])
    return head(f'{c["title"]}: case file | Roshan Mary Varghese', c["impact"], "../", c["img"]) + bar("../", [
        ("All work", "../index.html#work"), ("Timeline", "../index.html#timeline"), ("Contact", "../index.html#contact")]) + f"""
<main id="main">
  <div class="case-head">
    <div class="wrap">
      <div class="crumbs"><a href="../index.html#work">All work</a><span>Case file {n} of {total}</span></div>
      <h1>{e(c["title"])}</h1>
      <p class="impact">{e(c["impact"])}</p>
      <dl class="facts">
        <div><dt>Year</dt><dd>{e(c["year"])}</dd></div>
        <div><dt>Type</dt><dd>{e(c["type"])}</dd></div>
        <div><dt>Built for</dt><dd>{e(c["for_whom"])}</dd></div>
        <div><dt>Live</dt><dd><a href="{c["live"]}" target="_blank" rel="noopener">Open the live page</a></dd></div>
      </dl>
    </div>
  </div>

  <div class="wrap">
    <figure class="case-shot">
      <a href="{c["live"]}" target="_blank" rel="noopener" aria-label="Open {e(c["title"])}, live">
        <div class="chrome" aria-hidden="true"><i></i><i></i><i></i><span>{e(c["title"])}</span></div>
        <img src="../img/{c["img"]}" alt="{e(c["img_alt"])}" width="1600" height="1000">
      </a>
      <figcaption>Tap the screenshot to open the live page.</figcaption>
    </figure>

    <div class="case-body">
      <section aria-labelledby="problem" style="padding:0">
        <h2 id="problem">The problem</h2>
        {problem}
      </section>

      <section aria-labelledby="built" style="padding:0">
        <h2 id="built">What I built</h2>
        <p>{e(c["built_intro"])}</p>
        <ul class="built">{built}</ul>
        <p class="stack" style="margin-top:16px"><b>Built with:</b> {e(c["stack"])}</p>
        <div class="links"><a class="btn dark" href="{c["live"]}" target="_blank" rel="noopener">Open {e(c["title"])}</a></div>
      </section>

      <section aria-labelledby="approach" style="padding:0">
        <h2 id="approach">How I approached it</h2>
        <ul class="approach">{approach}</ul>
      </section>

      <section class="shows" aria-labelledby="shows">
        <h2 id="shows">What it shows about me</h2>
        <p>{e(c["shows"])}</p>
      </section>

      <a class="next card" href="{nxt["slug"]}.html">
        <div><span class="kicker">Next case file</span><h3>{e(nxt["title"])}</h3><p>{e(nxt["impact"])}</p></div>
        <span class="go">Read next</span>
      </a>
    </div>
  </div>
</main>

<footer class="case-foot">
  <div class="wrap">
    <span>Roshan Mary Varghese</span>
    <span><a href="mailto:{EMAIL}">{EMAIL}</a></span>
    <span><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></span>
  </div>
</footer>
</body>
</html>
"""


def work_card(c):
    return f"""
      <article class="work card">
        <a class="thumb" href="case/{c["slug"]}.html" aria-label="Read the {e(c["title"])} case file">
          <img src="img/{c["img"]}" alt="{e(c["img_alt"])}" loading="lazy" width="1600" height="1000">
        </a>
        <div class="body">
          <div class="meta"><span class="type">{e(c["type"])}</span><span>{e(c["year"])}</span></div>
          <h3>{e(c["title"])}</h3>
          <p class="impact">{e(c["impact"])}</p>
          <p class="stack"><b>Built with:</b> {e(c["stack"])}</p>
          <div class="links">
            <a class="btn dark" href="case/{c["slug"]}.html">Read the case file</a>
            <a class="btn" href="{c["live"]}" target="_blank" rel="noopener">Open live</a>
          </div>
        </div>
      </article>"""


def index_page():
    body = (ROOT / "tools" / "index.body.html").read_text()
    body = body.replace("<!--WORK-->", "".join(work_card(c) for c in CASES))
    body = body.replace("{LINKEDIN}", LINKEDIN).replace("{EMAIL}", EMAIL).replace("{INSTAGRAM}", INSTAGRAM)
    return head("Roshan Mary Varghese | Health tech product and client engagement",
                "Dentist, six years in health insurance claims and account management, MPH with Distinction. "
                "I build plain-English health tech tools and write up how I made each one.",
                "", "dubai-health-money-radar.webp") + bar("", [
        ("Work", "#work"), ("Timeline", "#timeline"), ("Credentials", "#credentials"), ("Contact", "#contact")]) + body


def main():
    (ROOT / "case").mkdir(exist_ok=True)
    for i, c in enumerate(CASES):
        (ROOT / "case" / f'{c["slug"]}.html').write_text(case_page(i, c))
    (ROOT / "index.html").write_text(index_page())
    print(f"Built index.html and {len(CASES)} case files")


if __name__ == "__main__":
    main()
