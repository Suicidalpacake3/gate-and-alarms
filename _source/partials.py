"""Shared header, footer and icons for the Gate & Alarms site."""

PHONE_DISPLAY = "081 718 2920"
PHONE_TEL = "+27817182920"
WHATSAPP = "https://wa.me/27817182920"
EMAIL = "brian@gateandalarms.co.za"

ICON = {
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 3.5h3.2l1.6 4.2-2.1 1.3a11 11 0 0 0 7.3 7.3l1.3-2.1 4.2 1.6V19a1.6 1.6 0 0 1-1.7 1.6A16.6 16.6 0 0 1 3.4 5.2 1.6 1.6 0 0 1 5 3.5z"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 11.6a8.4 8.4 0 0 1-12.4 7.4L3.5 20.5l1.6-4.4A8.4 8.4 0 1 1 20.5 11.6z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5.5" width="18" height="13" rx="1.5"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>',
}

NAV = [("index.html", "Home"), ("about.html", "About"), ("services.html", "Services"), ("contact.html", "Contact")]


def head(title, description, page):
    return f"""<!doctype html>
<html lang="en-ZA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#11161a">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/img/hero-house-night.jpg">
<link rel="icon" href="assets/brand/favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/brand/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="assets/brand/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&amp;family=Source+Sans+3:wght@400;500;600&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css?v=5">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Gate and Alarms Security",
  "description": "Gate automation, alarm systems, CCTV and steelwork for homes and businesses in Pretoria.",
  "telephone": "{PHONE_TEL}",
  "email": "{EMAIL}",
  "url": "https://gateandalarms.co.za/",
  "areaServed": ["Waverley", "Pretoria Moot", "Pretoria"],
  "logo": "https://gateandalarms.co.za/assets/brand/icon-512.png"
}}
</script>
</head>
<body data-page="{page}">
"""


def brand():
    return """<a class="brand" href="index.html" aria-label="Gate and Alarms, home">
      <img src="assets/brand/mark.svg" alt="" width="44" height="44">
      <span class="brand-text">
        <span class="brand-name">Gate <em>&amp;</em> Alarms</span>
        <span class="brand-sub">Security &amp; Steelworks</span>
      </span>
    </a>"""


def header(page):
    links = "\n".join(
        f'          <a href="{href}"{" aria-current=\"page\"" if href == page else ""}>{label}</a>'
        for href, label in NAV
    )
    return f"""<header class="site-header">
  <div class="wrap">
    {brand()}
    <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="site-nav"><span></span></button>
    <nav class="nav" id="site-nav" aria-label="Main">
      <div class="nav-links">
{links}
      </div>
      <a class="btn btn-signal" href="tel:{PHONE_TEL}">{ICON['phone']}Call Brian</a>
    </nav>
    <div class="nav-scrim"></div>
  </div>
</header>
"""


def footer():
    brand_light = brand().replace("assets/brand/mark.svg", "assets/brand/mark-light.svg")
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-about">
        {brand_light}
        <p>A small, well established Pretoria company installing and maintaining gates, gate motors, alarm systems and CCTV for homes, businesses and industrial sites since the early 2000s.</p>
      </div>
      <div>
        <h4>Main services</h4>
        <ul>
          <li><a href="services.html#sliding-gates">Sliding gates</a></li>
          <li><a href="services.html#swing-gates">Swing gates</a></li>
          <li><a href="services.html#gate-motors">Gate motors</a></li>
          <li><a href="services.html#alarm-systems">Alarm systems</a></li>
          <li><a href="services.html#cctv">CCTV cameras</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">About us</a></li>
          <li><a href="services.html#security">Security and steel</a></li>
          <li><a href="services.html#additional">Additional services</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Speak to Brian</h4>
        <a class="footer-phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
        <ul>
          <li><a href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp us</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Waverley, the Moot and greater Pretoria</li>
        </ul>
        <h4 style="margin-top:28px">Office hours</h4>
        <ul>
          <li>Monday to Friday, 08:00 to 17:00</li>
          <li>Saturday, 08:00 to 13:00</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="footer-base">
    <div class="wrap">
      <span>&copy; <span data-year>2026</span> Gate and Alarms Security. All rights reserved.</span>
      <span>On site service only. We come to you.</span>
    </div>
  </div>
</footer>
<div class="float-call">
  <a class="btn btn-signal" href="tel:{PHONE_TEL}">{ICON['phone']}Call</a>
  <a class="btn btn-ink" href="{WHATSAPP}" target="_blank" rel="noopener">{ICON['chat']}WhatsApp</a>
</div>
<script src="assets/js/site.js?v=5"></script>
</body>
</html>
"""
