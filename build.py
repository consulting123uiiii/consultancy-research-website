#!/usr/bin/env python3
"""
Static page generator for consultancyresearch.com.

Header/footer/head live here once; each page supplies title, description and body.
Run:  python3 build.py     (outputs .html files into the repo root)

index.html is hand-maintained and is NOT overwritten by this script.
"""
import pathlib

ROOT = pathlib.Path(__file__).parent

ARROW = ('<svg width="15" height="9" viewBox="0 0 15 9" fill="none">'
         '<path d="M0 4.5h13M9.5 1 13 4.5 9.5 8" stroke="currentColor" stroke-width="1.3"/></svg>')

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://consultancyresearch.com/{slug}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>

<header class="site-header is-solid">
  <div class="wrap header-inner">
    <a class="brand" href="index.html" aria-label="Consultancy Research International - home">
      <svg class="brand__mark" viewBox="0 0 40 40" fill="none" aria-hidden="true">
        <rect x="0.6" y="0.6" width="38.8" height="38.8" stroke="#0B1E30" stroke-width="1.2"/>
        <rect x="9" y="22" width="3.4" height="9" fill="#0B1E30"/>
        <rect x="15.6" y="17" width="3.4" height="14" fill="#0B1E30"/>
        <rect x="22.2" y="12" width="3.4" height="19" fill="#B4884A"/>
        <path d="M8 15.5 L16 11 L24 7.5 L32 9.5" stroke="#B4884A" stroke-width="1.2" stroke-linecap="square"/>
      </svg>
      <span class="brand__text">
        <span class="brand__name">Consultancy Research</span>
        <span class="brand__sub">International</span>
      </span>
    </a>
    <nav class="nav" aria-label="Primary">
      <a href="capabilities.html">Capabilities</a>
      <a href="sectors.html">Sectors</a>
      <a href="insights.html">Insights</a>
      <a href="about.html">About</a>
    </nav>
    <div class="header-cta">
      <a class="btn" href="contact.html">Start a project</a>
      <button class="burger" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>

<div class="mobile-nav" aria-label="Mobile">
  <a href="capabilities.html">Capabilities</a>
  <a href="sectors.html">Sectors</a>
  <a href="insights.html">Insights</a>
  <a href="about.html">About</a>
  <a href="contact.html">Contact</a>
  <a class="btn" href="contact.html">Start a project</a>
</div>

<main>
"""

FOOT = """</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <div class="brand">
          <svg class="brand__mark" viewBox="0 0 40 40" fill="none" aria-hidden="true">
            <rect x="0.6" y="0.6" width="38.8" height="38.8" stroke="#FFFFFF" stroke-width="1.2" opacity=".55"/>
            <rect x="9" y="22" width="3.4" height="9" fill="#FFFFFF" opacity=".8"/>
            <rect x="15.6" y="17" width="3.4" height="14" fill="#FFFFFF" opacity=".8"/>
            <rect x="22.2" y="12" width="3.4" height="19" fill="#D9C49B"/>
            <path d="M8 15.5 L16 11 L24 7.5 L32 9.5" stroke="#D9C49B" stroke-width="1.2" stroke-linecap="square"/>
          </svg>
          <span class="brand__text">
            <span class="brand__name">Consultancy Research</span>
            <span class="brand__sub">International</span>
          </span>
        </div>
        <p class="footer-about">Independent primary research and market intelligence for investors, consultancies and corporate strategy teams.</p>
      </div>
      <div class="footer-col">
        <h5>Firm</h5>
        <ul>
          <li><a href="about.html">About us</a></li>
          <li><a href="capabilities.html">Capabilities</a></li>
          <li><a href="sectors.html">Sectors</a></li>
          <li><a href="insights.html">Insights</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Engage</h5>
        <ul>
          <li><a href="contact.html">Commission research</a></li>
          <li><a href="insights.html">Research briefing</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Contact</h5>
        <ul>
          <li><a href="mailto:research@consultancyresearch.com">research@consultancyresearch.com</a></li>
          <li>78 York Street<br>London, United Kingdom</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> Consultancy Research International. All rights reserved.</span>
      <nav>
        <a href="privacy.html">Privacy</a>
        <a href="terms.html">Terms</a>
        <a href="contact.html">Contact</a>
      </nav>
    </div>
  </div>
</footer>

<script src="assets/js/site.js"></script>
</body>
</html>
"""


def page_hero(eyebrow, h1, lede):
    return f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow reveal">{eyebrow}</p>
    <h1 class="reveal">{h1}</h1>
    <p class="lede reveal">{lede}</p>
  </div>
</section>
"""


CTA = """<section class="cta">
  <div class="wrap cta__inner reveal">
    <h2>Tell us the decision. We will build the evidence.</h2>
    <p>Most engagements begin with a thirty-minute scoping conversation. There is no charge for it, and no obligation to proceed.</p>
    <div class="cta__actions">
      <a class="btn btn--light" href="contact.html">Start a project</a>
      <a class="btn btn--outline-light" href="about.html">About the firm</a>
    </div>
  </div>
</section>
"""

CTA_ABOUT = CTA.replace('<a class="btn btn--outline-light" href="about.html">About the firm</a>',
                        '<a class="btn btn--outline-light" href="capabilities.html">Our capabilities</a>')

PAGES = {}

# ------------------------------------------------------------------ CAPABILITIES
PAGES["capabilities.html"] = dict(
    title="Capabilities — Consultancy Research International",
    desc="Commercial due diligence, custom primary research, sector intelligence and strategy advisory from an independent market research firm.",
    body=page_hero(
        "Capabilities",
        "Research built for<br>decisions with consequences.",
        "We are commissioned when the cost of being wrong is high and the available information is thin, contested, or written by someone with an interest in the outcome."
    ) + """
<section class="section">
  <div class="wrap">
    <div class="grid grid--2">
      <article class="card reveal">
        <span class="card__num">01</span>
        <h3>Commercial &amp; market due diligence</h3>
        <p>An independent read on whether a market, an asset or a plan holds up. Built to transaction timetables and structured so it survives an investment committee that is looking for holes.</p>
        <ul class="card__list">
          <li>Bottom-up market sizing and segmentation</li>
          <li>Growth driver decomposition and forecast stress testing</li>
          <li>Customer retention, pricing power and switching economics</li>
          <li>Competitive positioning and share estimation</li>
          <li>Red-flag, confirmatory and vendor-side diligence</li>
        </ul>
      </article>
      <article class="card reveal">
        <span class="card__num">02</span>
        <h3>Custom primary research</h3>
        <p>Fieldwork designed around the question rather than pulled off a shelf. Quantitative and qualitative programmes run to a written specification, with the sample defined and agreed before any collection begins.</p>
        <ul class="card__list">
          <li>Quantitative survey programmes</li>
          <li>Qualitative depth interviews, moderated or unmoderated</li>
          <li>Focus groups and moderated discussions</li>
          <li>Longitudinal and tracking studies</li>
          <li>Channel and distribution checks</li>
        </ul>
      </article>
      <article class="card reveal">
        <span class="card__num">03</span>
        <h3>Sector &amp; competitive intelligence</h3>
        <p>Standing coverage for teams that need to see a category move before consensus does. We monitor the operational signals that lead reported results rather than following them.</p>
        <ul class="card__list">
          <li>Continuous sector monitoring programmes</li>
          <li>Competitor strategy, capability and capacity mapping</li>
          <li>Regulatory and policy impact assessment</li>
          <li>Supply chain, input cost and lead time tracking</li>
          <li>Demand signal and order book intelligence</li>
        </ul>
      </article>
      <article class="card reveal">
        <span class="card__num">04</span>
        <h3>Strategy &amp; growth advisory</h3>
        <p>When the evidence points somewhere, we help act on it. Small senior teams, no leverage pyramid, and recommendations that stay tied to the research that produced them.</p>
        <ul class="card__list">
          <li>Market entry and geographic expansion</li>
          <li>Pricing architecture and commercial model design</li>
          <li>Portfolio and adjacency prioritisation</li>
          <li>Post-acquisition value creation planning</li>
          <li>Board and investment committee support materials</li>
        </ul>
      </article>
    </div>
  </div>
</section>

<section class="section section--ink">
  <div class="wrap split split--rev">
    <div class="reveal">
      <p class="eyebrow">Method</p>
      <h2 style="margin-bottom:22px">Four stages. Every one auditable.</h2>
      <p class="lede">We do not ask clients to take our conclusions on trust. Each finding carries the evidence behind it, the confidence we attach to it, and what would have to be true for it to be wrong.</p>
    </div>
    <ol class="steps reveal">
      <li><h3>Frame the commercial question</h3><p>A broad request becomes a written research question with explicit decision thresholds. Scope, sample and deliverable are agreed before any fieldwork starts.</p></li>
      <li><h3>Design the research and define the sample</h3><p>Method, sample and instrument are specified and agreed before any collection begins, so the evidence base is built to answer the question rather than assembled from convenience.</p></li>
      <li><h3>Collect and triangulate</h3><p>Quantitative and qualitative work run in parallel and are cross-checked against the published record. Where sources conflict, we report the conflict.</p></li>
      <li><h3>Deliver with a clear line of sight</h3><p>Findings arrive as an argument, not a data dump: conclusion, confidence, evidence, and the conditions under which it would break.</p></li>
    </ol>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="reveal" style="max-width:620px;margin-bottom:48px">
      <p class="eyebrow">Deliverables</p>
      <h2>What arrives, and when.</h2>
    </div>
    <div class="grid grid--3">
      <article class="card reveal">
        <h3>Rolling insight</h3>
        <p>Findings released as they are confirmed, from the first completed fieldwork onward. Clients are not waiting on a report to start forming a view.</p>
      </article>
      <article class="card reveal">
        <h3>Structured evidence base</h3>
        <p>Survey outputs, interview records and source data delivered in a form the client's own team can interrogate, quote and re-use after the engagement closes.</p>
      </article>
      <article class="card reveal">
        <h3>Decision document</h3>
        <p>A written argument sized for the audience &mdash; typically twenty to forty pages, with the conclusion on the first page rather than the last.</p>
      </article>
    </div>
  </div>
</section>
""" + CTA,
)

# ------------------------------------------------------------------ SECTORS
SECTORS = [
    ("Industrials &amp; Manufacturing",
     "Capital equipment, factory automation, aftermarket and services attach, distribution structures, supply chain resilience and the real economics of reshoring.",
     ["Capital equipment demand cycles", "Aftermarket and service attach rates", "Automation payback periods", "Distributor margin structures"]),
    ("Healthcare &amp; Life Sciences",
     "Provider economics, payer and reimbursement dynamics, medtech adoption curves, pharma services outsourcing and the practical route a product takes to a patient.",
     ["Reimbursement and coverage risk", "Clinician adoption behaviour", "Provider consolidation effects", "Pharma services outsourcing demand"]),
    ("Technology &amp; Software",
     "Enterprise buying behaviour, retention and expansion economics, category consolidation, build-versus-buy decisions and where pricing power genuinely sits.",
     ["Enterprise buying committees", "Retention and expansion drivers", "Competitive displacement patterns", "Pricing and packaging shifts"]),
    ("Financial Services",
     "Distribution economics, regulatory change, market infrastructure providers, non-bank credit formation and the operational reality behind reported margins.",
     ["Distribution and adviser economics", "Regulatory change exposure", "Infrastructure vendor switching", "Non-bank credit dynamics"]),
    ("Consumer &amp; Retail",
     "Category demand, channel shift, private label pressure, brand equity durability and price elasticity under sustained input cost inflation.",
     ["Category demand and elasticity", "Channel and format shift", "Private label encroachment", "Retail buyer negotiation dynamics"]),
    ("Energy &amp; Transition",
     "Generation and grid economics, transition technology adoption, policy and subsidy exposure, offtake structures and project bankability.",
     ["Project economics and offtake", "Grid and interconnection constraints", "Policy and subsidy dependence", "Technology adoption curves"]),
    ("Business Services",
     "Outsourced service demand, compliance-driven spend, labour supply constraints, roll-up integration economics and contract renewal behaviour.",
     ["Contract renewal and churn", "Compliance-driven demand", "Labour supply and wage pressure", "Roll-up integration economics"]),
    ("Transport &amp; Logistics",
     "Freight rate formation, network and density economics, last-mile structures, warehouse automation and capacity cycle positioning.",
     ["Freight rate formation", "Network density economics", "Last-mile cost structures", "Capacity cycle positioning"]),
]

sector_cards = "\n".join(
    f"""      <article class="card reveal">
        <span class="card__num">{i:02d}</span>
        <h3>{name}</h3>
        <p>{desc}</p>
        <ul class="card__list">{''.join(f'<li>{t}</li>' for t in topics)}</ul>
      </article>"""
    for i, (name, desc, topics) in enumerate(SECTORS, start=1)
)

PAGES["sectors.html"] = dict(
    title="Sectors — Consultancy Research International",
    desc="Standing research coverage across industrials, healthcare, technology, financial services, consumer, energy, business services and logistics.",
    body=page_hero(
        "Sector coverage",
        "Eight sectors.<br>Continuous coverage.",
        "Our researchers work the same categories year after year. That accumulated context is why the second engagement in a sector is faster, sharper and cheaper than the first."
    ) + f"""
<section class="section">
  <div class="wrap">
    <div class="grid grid--2">
{sector_cards}
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap wrap-narrow" style="text-align:center">
    <div class="reveal">
      <p class="eyebrow center">Beyond our core sectors</p>
      <h2 style="margin-bottom:22px">If it is researchable, we will tell you honestly whether we can do it well.</h2>
      <p class="lede" style="margin:0 auto 32px">We regularly work outside standing coverage where the question is well framed and the right respondents can be reached. Where we are not the right firm, we say so at the scoping stage rather than after the invoice.</p>
      <a class="btn" href="contact.html">Put a question to us</a>
    </div>
  </div>
</section>
""" + CTA,
)

# ------------------------------------------------------------------ INSIGHTS
ARTICLES = [
    ("Methodology", "Why sample design beats sample size",
     "A sample drawn from the wrong population is not more reliable for being larger, only more confident. How we specify one that survives challenge.",
     "line"),
    ("Industrials", "Reshoring: the gap between intent and capital",
     "Boards keep announcing supply chain relocation. Order books for the equipment that would make it real tell a considerably slower story.",
     "bars"),
    ("Software", "Net revenue retention is not a growth signal",
     "What enterprise buyers actually renew on, and why the headline metric increasingly measures pricing action rather than product value.",
     "rings"),
    ("Healthcare", "Reimbursement risk is a commercial question",
     "Coverage decisions are treated as regulatory detail and priced as such. In most medtech diligence they are the single largest swing factor.",
     "line"),
    ("Consumer", "Elasticity after three years of price rises",
     "Category-level demand has held up better than modelled in some baskets and worse in others. The split is not where most forecasts placed it.",
     "bars"),
    ("Energy", "Interconnection queues as a leading indicator",
     "Grid connection timetables constrain more transition projects than capital availability does. They are also public, and largely unwatched.",
     "rings"),
    ("Financial services", "What advisers switch platforms for",
     "Platform economics assume adviser inertia. Interview evidence points to a narrower set of triggers that break it faster than incumbents assume.",
     "line"),
    ("Business services", "Roll-up margin, and where it leaks",
     "Integration synergy models rarely account for the operational cost of holding acquired customer relationships through a rebrand.",
     "bars"),
    ("Logistics", "Density beats scale in last mile",
     "National footprint is the metric operators report. Route density is the metric that determines whether the unit economics ever close.",
     "rings"),
]

VIS = {
    "line": """<svg viewBox="0 0 400 126" preserveAspectRatio="none" aria-hidden="true">
            <path d="M0 104 L57 96 L114 100 L171 74 L228 66 L285 44 L342 36 L400 14" stroke="#0B1E30" stroke-width="1.5" fill="none"/>
            <path d="M0 104 L57 96 L114 100 L171 74 L228 66 L285 44 L342 36 L400 14 L400 126 L0 126 Z" fill="#0B1E30" opacity=".06"/>
            <circle cx="400" cy="14" r="4" fill="#B4884A"/>
          </svg>""",
    "bars": """<svg viewBox="0 0 400 126" preserveAspectRatio="none" aria-hidden="true">
            <rect x="30" y="70" width="34" height="56" fill="#0B1E30" opacity=".18"/>
            <rect x="92" y="52" width="34" height="74" fill="#0B1E30" opacity=".26"/>
            <rect x="154" y="60" width="34" height="66" fill="#0B1E30" opacity=".22"/>
            <rect x="216" y="34" width="34" height="92" fill="#0B1E30" opacity=".34"/>
            <rect x="278" y="22" width="34" height="104" fill="#B4884A" opacity=".85"/>
            <rect x="340" y="46" width="34" height="80" fill="#0B1E30" opacity=".28"/>
          </svg>""",
    "rings": """<svg viewBox="0 0 400 126" preserveAspectRatio="none" aria-hidden="true">
            <circle cx="200" cy="63" r="46" stroke="#0B1E30" stroke-width="1.4" fill="none" opacity=".35"/>
            <circle cx="200" cy="63" r="28" stroke="#0B1E30" stroke-width="1.4" fill="none" opacity=".5"/>
            <circle cx="200" cy="63" r="10" fill="#B4884A"/>
            <line x1="0" y1="63" x2="146" y2="63" stroke="#0B1E30" stroke-width="1" opacity=".22"/>
            <line x1="254" y1="63" x2="400" y2="63" stroke="#0B1E30" stroke-width="1" opacity=".22"/>
          </svg>""",
}

insight_cards = "\n".join(
    f"""      <article class="insight reveal">
        <div class="insight__top" style="background:#F3F1EA">{VIS[vis]}</div>
        <div class="insight__body">
          <p class="insight__meta">{meta}</p>
          <h3>{title}</h3>
          <p>{blurb}</p>
          <a class="link-arrow" href="contact.html">Request the note {ARROW}</a>
        </div>
      </article>"""
    for meta, title, blurb, vis in ARTICLES
)

PAGES["insights.html"] = dict(
    title="Insights — Consultancy Research International",
    desc="Perspectives from our research programmes across industrials, healthcare, software, consumer, energy, financial services and logistics.",
    body=page_hero(
        "Insights",
        "What the evidence<br>keeps showing us.",
        "Short notes drawn from live research programmes. We publish where a finding is durable enough to be useful and general enough to share without compromising a client engagement."
    ) + f"""
<section class="section">
  <div class="wrap">
    <div class="insights">
{insight_cards}
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap wrap-narrow" style="text-align:center">
    <div class="reveal">
      <p class="eyebrow center">Research briefing</p>
      <h2 style="margin-bottom:20px">A monthly note, and nothing else.</h2>
      <p class="lede" style="margin:0 auto 30px">One email a month with the findings we think travel beyond the client that commissioned them. No promotion, no sequence, unsubscribe in one click.</p>
      <a class="btn" href="contact.html">Request the briefing</a>
    </div>
  </div>
</section>
""" + CTA,
)

# ------------------------------------------------------------------ ABOUT
PAGES["about.html"] = dict(
    title="About — Consultancy Research International",
    desc="An independent market research firm built around primary evidence, with no conflicting business lines.",
    body=page_hero(
        "About the firm",
        "Independent, by<br>construction.",
        "Consultancy Research International exists because the people making the largest commercial decisions are usually working from the thinnest evidence."
    ) + """
<section class="section">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Our position</p>
      <h2>We sell research. Nothing else.</h2>
    </div>
    <div class="reveal">
      <p style="color:var(--muted)">We do not run a fund. We do not sell software, data subscriptions or advertising. We hold no position, direct or indirect, in the markets we are asked to research. That structural simplicity is the point: it is what allows a client to read our conclusion without first working out what we stood to gain from it.</p>
      <p style="color:var(--muted)">The firm is deliberately small at the senior level and deliberately deep at the research level. Engagements are led by people who have covered their sector for years, supported by a research team whose work is designing and running the fieldwork behind each answer.</p>
      <p style="color:var(--muted)">We would rather turn down a mandate than deliver one badly. Where a question falls outside what we can evidence properly, we say so at the scoping call.</p>
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <div class="reveal" style="max-width:620px;margin-bottom:48px">
      <p class="eyebrow">Principles</p>
      <h2>Four rules we do not trade away.</h2>
    </div>
    <div class="grid grid--2">
      <article class="card reveal">
        <span class="card__num">01</span>
        <h3>Evidence over narrative</h3>
        <p>A well-told story is not a finding. Every conclusion we deliver is tied to a source record, and where the evidence is thin we mark it thin rather than dressing it up.</p>
      </article>
      <article class="card reveal">
        <span class="card__num">02</span>
        <h3>Disagreement is data</h3>
        <p>When credible sources contradict one another, that tension usually contains the insight. We report it rather than averaging it into a comfortable middle.</p>
      </article>
      <article class="card reveal">
        <span class="card__num">03</span>
        <h3>Sample quality decides answer quality</h3>
        <p>A sample is not more reliable for being larger, only more confident. We would rather extend a timeline by three days than fill it with responses that cannot speak to the question.</p>
      </article>
      <article class="card reveal">
        <span class="card__num">04</span>
        <h3>Say the uncomfortable thing</h3>
        <p>Clients are paying for judgement, not agreement. If the research undermines the thesis that commissioned it, that is the most valuable output we can deliver.</p>
      </article>
    </div>
  </div>
</section>

""" + CTA_ABOUT,
)

# ------------------------------------------------------------------ CONTACT
PAGES["contact.html"] = dict(
    title="Contact — Consultancy Research International",
    desc="Commission a research programme or put a question to Consultancy Research International.",
    body=page_hero(
        "Contact",
        "Start with the<br>decision you face.",
        "Tell us what you are trying to establish and by when. We will come back within one business day with a view on whether it is researchable, how, and at what cost."
    ) + """
<section class="section">
  <div class="wrap split split--rev">
    <div class="reveal">
      <h2 style="margin-bottom:14px">Send a brief</h2>
      <p class="lede" style="margin-bottom:32px">No obligation and no charge for scoping. If we are not the right firm for the question we will tell you at this stage.</p>

      <form class="form" data-mailto-form="research@consultancyresearch.com">
        <div class="form-row">
          <div class="field"><label for="n">Name</label><input id="n" name="Name" type="text" required></div>
          <div class="field"><label for="o">Organisation</label><input id="o" name="Organisation" type="text" required></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="e">Work email</label><input id="e" name="Email" type="email" required></div>
          <div class="field">
            <label for="t">Enquiry type</label>
            <select id="t" name="Enquiry type">
              <option>Commission a research programme</option>
              <option>Commercial due diligence</option>
              <option>Custom primary research</option>
              <option>Standing sector coverage</option>
              <option>Media or other</option>
            </select>
          </div>
        </div>
        <div class="field">
          <label for="m">What are you trying to establish?</label>
          <textarea id="m" name="Brief" placeholder="The decision, the question behind it, and the timetable you are working to." required></textarea>
        </div>
        <div class="form-status" role="status"></div>
        <div style="display:flex;align-items:center;gap:20px;flex-wrap:wrap">
          <button class="btn" type="submit">Send brief</button>
          <span class="form-note">We reply within one business day.</span>
        </div>
      </form>
    </div>

    <aside class="reveal">
      <p class="eyebrow">Direct</p>
      <div class="contact-block">
        <h4>Research enquiries</h4>
        <p><a href="mailto:research@consultancyresearch.com">research@consultancyresearch.com</a></p>
      </div>
      <div class="contact-block">
        <h4>Office</h4>
        <p>78 York Street<br>London, United Kingdom</p>
      </div>
      <div class="contact-block">
        <h4>Response time</h4>
        <p>One business day. Scoping calls typically within seventy-two hours.</p>
      </div>
      <div class="contact-block" style="border-bottom:1px solid var(--line)">
        <h4>Confidentiality</h4>
        <p>Briefs are treated as confidential from first contact. Mutual NDA available on request.</p>
      </div>
    </aside>
  </div>
</section>
""",
)

# ------------------------------------------------------------------ PRIVACY
PAGES["privacy.html"] = dict(
    title="Privacy Notice — Consultancy Research International",
    desc="How Consultancy Research International collects, uses and protects personal data.",
    body=page_hero("Legal", "Privacy notice", "How we collect, use, store and protect personal data.") + """
<section class="section">
  <div class="wrap wrap-narrow prose reveal">
    <p><strong>Last updated:</strong> <span data-year>2026</span></p>

    <h2>Who we are</h2>
    <p>Consultancy Research International ("we", "us") is an independent market research firm. This notice explains how we handle personal data in connection with our website, our research programmes and our fieldwork.</p>

    <h2>Data we collect</h2>
    <ul>
      <li><strong>Contact data</strong> you provide directly &mdash; name, organisation, work email address and the content of your enquiry.</li>
      <li><strong>Professional data</strong> where you take part in our research &mdash; employment history, areas of expertise and screening responses.</li>
      <li><strong>Business contact data</strong> obtained from public professional sources and licensed business-information providers, used to identify individuals who may be relevant to a research programme.</li>
      <li><strong>Technical data</strong> generated when you visit this website, limited to what is necessary to serve and secure the pages.</li>
    </ul>

    <h2>How we use it</h2>
    <ul>
      <li>To respond to enquiries and scope research engagements.</li>
      <li>To identify and engage research participants for client research programmes.</li>
      <li>To send research briefings where you have asked to receive them.</li>
      <li>To meet our legal, regulatory and contractual obligations.</li>
    </ul>

    <h2>Legal basis</h2>
    <p>Where the UK GDPR or EU GDPR applies, we rely on legitimate interests for business-to-business research and professional outreach, on contract performance where we are engaged with you, on consent where you have opted into a briefing, and on legal obligation where retention or disclosure is required of us.</p>

    <h2>Sharing</h2>
    <p>We share personal data with service providers who support our operations under written data processing terms, and with clients only in the form agreed in the engagement. We do not sell personal data.</p>

    <h2>Retention</h2>
    <p>We keep personal data only for as long as it is needed for the purpose it was collected for, or for as long as a legal or regulatory obligation requires. Records connected to a research programme are retained for the period required by our contractual and regulatory obligations.</p>

    <h2>International transfers</h2>
    <p>Where personal data is transferred outside the UK or EEA, we use appropriate safeguards including standard contractual clauses.</p>

    <h2>Your rights</h2>
    <p>Depending on where you are located, you may have the right to access, correct, delete, restrict or object to our processing of your personal data, to withdraw consent, and to complain to a supervisory authority. To exercise any of these rights, write to <a href="mailto:privacy@consultancyresearch.com">privacy@consultancyresearch.com</a>.</p>

    <h2>Opting out of contact</h2>
    <p>You can ask us to stop contacting you at any time by replying to any message from us or writing to <a href="mailto:privacy@consultancyresearch.com">privacy@consultancyresearch.com</a>. We action removal requests promptly and record them so that contact is not resumed.</p>

    <h2>Contact</h2>
    <p>Questions about this notice: <a href="mailto:privacy@consultancyresearch.com">privacy@consultancyresearch.com</a>.</p>
  </div>
</section>
""",
)

# ------------------------------------------------------------------ TERMS
PAGES["terms.html"] = dict(
    title="Terms of Use — Consultancy Research International",
    desc="Terms governing use of the Consultancy Research International website.",
    body=page_hero("Legal", "Terms of use", "The terms on which this website is made available.") + """
<section class="section">
  <div class="wrap wrap-narrow prose reveal">
    <p><strong>Last updated:</strong> <span data-year>2026</span></p>

    <h2>Acceptance</h2>
    <p>By accessing this website you agree to these terms. If you do not accept them, please do not use the site.</p>

    <h2>Nature of the content</h2>
    <p>Material published here is provided for general information about our services. It does not constitute investment advice, a recommendation, an offer or a solicitation to buy or sell any security or financial instrument, and it should not be relied on as the basis for any commercial or investment decision.</p>

    <h2>No client relationship</h2>
    <p>Use of this site, including submission of an enquiry, does not create a client relationship. Engagements are governed exclusively by a signed written agreement.</p>

    <h2>Intellectual property</h2>
    <p>All content on this site is owned by or licensed to Consultancy Research International and may not be reproduced, distributed or used commercially without prior written permission.</p>

    <h2>Third-party links</h2>
    <p>Where we link to third-party sites we do so for convenience only and accept no responsibility for their content or availability.</p>

    <h2>Limitation of liability</h2>
    <p>To the fullest extent permitted by law, we exclude liability for any loss arising from use of, or reliance on, material published on this site. Nothing in these terms limits liability that cannot lawfully be limited.</p>

    <h2>Changes</h2>
    <p>We may update these terms at any time. The version published here is the version in force.</p>

    <h2>Contact</h2>
    <p>Questions about these terms: <a href="mailto:research@consultancyresearch.com">research@consultancyresearch.com</a>.</p>
  </div>
</section>
""",
)

# ------------------------------------------------------------------ 404
PAGES["404.html"] = dict(
    title="Page not found — Consultancy Research International",
    desc="The page you are looking for could not be found.",
    body="""<section class="section" style="padding-top:190px;text-align:center">
  <div class="wrap wrap-narrow">
    <p class="eyebrow center">Error 404</p>
    <h1 style="margin-bottom:22px">This page could not be found.</h1>
    <p class="lede" style="margin:0 auto 34px">The link may be out of date, or the page may have moved.</p>
    <a class="btn" href="index.html">Return to the homepage</a>
  </div>
</section>
""",
)


def build():
    for slug, cfg in PAGES.items():
        html = HEAD.format(title=cfg["title"], desc=cfg["desc"], slug=slug) + cfg["body"] + FOOT
        (ROOT / slug).write_text(html, encoding="utf-8")
        print("built", slug)


if __name__ == "__main__":
    build()
