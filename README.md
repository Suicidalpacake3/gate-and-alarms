# Gate and Alarms Security website

Static site, four pages: `index.html`, `about.html`, `services.html`, `contact.html`.
No server code needed. Upload the root folder (without `_source` if you like) to any host.

## Editing

The finished `.html` files are generated. Edit the sources, then rebuild:

```
python _source/build.py
```

- `_source/pages/*.html`: the content of each page
- `_source/partials.py`: header, footer, phone number, WhatsApp link and email (change them once here)
- `assets/css/site.css`: all styling
- `assets/js/site.js`: mobile menu, service accordions, contact form

The build stops with an error if any page contains an en or em dash.

## Logo

- `assets/brand/mark.svg`: logo mark (dark), `mark-light.svg` for dark backgrounds
- `assets/brand/favicon.svg`, `favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, `icon-512.png`

## Contact form

There is no backend. The form builds a message and opens it in WhatsApp (to 081 718 2920) or the visitor's email app (to brian@gateandalarms.co.za).

## Photos

All photos are free stock images from Pexels (free for commercial use, no attribution required), saved in `assets/img`. Pexels photo IDs: 31737859, 13165402, 4540992, 18143352, 8365306, 430208, 36004813, 16423104, 13007861, 29386088, 11758312, 38524262, 17965455, 4626268.

One exception: `centurion-d5-evo.jpg` is by Felix Chidanyika on Wikimedia Commons under CC BY-SA 4.0, which requires the credit shown on the services page. Keep that caption if you keep the photo.
