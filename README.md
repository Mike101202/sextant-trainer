# Sextant Trainer

A free, fully offline sextant trainer for celestial navigation practice. Works in any modern browser, installs to the home screen as a PWA, and functions with no internet connection once loaded.

**[Try it live →](https://YOUR-USERNAME.github.io/sextant-trainer/)**

*(Replace the URL above with your actual GitHub Pages URL after enabling Pages.)*

## Features

- **Auto mode** — the app computes everything from your Hs.
- **Tables mode** — you look up Hc, d and Zn from your printed Pub. 229, and the app does the corrections, d-ΔDec multiplication, and intercept.
- **Full manual mode** — enter fully corrected Ho, Hc and Zn; the app plots the fix.
- **Running fix** — combine two or more sightings of the same body across time, with dead-reckoning advance.
- **Midday zenith-distance fit** — fits z² vs time across morning and afternoon Sun sightings to give noon time (→ longitude) and latitude.
- **Direct fix** — two-circle intersection solution (Van Allen), independent of the intercept method.
- **Pub. 229 second-difference** — optional, for high-accuracy Hc above ~60°.
- **Practice almanac** — hourly GHA/Dec for Sun, Moon, planets, Aries and stars; printable daily pages.
- **Works completely offline** — PWA with a service worker; nothing is fetched after first load.
- **No accounts, no tracking, no data collection.** Everything stays on your device.

## Using the app

The Help panel (tap **A** in the header) contains a labelled sextant diagram, a link to the official Pub. 229 PDFs and the full Nautical Almanac, and a glossary of 34 navigation terms.

For paper-based practice:
1. Set up an assumed position in Setup.
2. Go to Sights, choose Tables mode, and enter Hc, d, Zn from your Pub. 229 book.
3. The app computes Ho from your Hs, applies d × ΔDec, and shows the intercept.
4. Repeat for another body, tick them in the Sights list, and go to Fix to see the combined position.

## Tables and almanac

The app uses the official *Pub. 229 — Sight Reduction Tables for Marine Navigation* (also known as HO 229 in the US and NP 401 in the UK). These are **US Government publications and are in the public domain**. A well-maintained archive of the official PDFs, along with the Nautical Almanac and other free resources, is at:

**https://thenauticalalmanac.com/**

The Help panel in the app links directly to it.

## F-Droid

An F-Droid release is planned. Once the listing is live it will appear here.

To build the Android APK yourself, this app can be wrapped with [Capacitor](https://capacitorjs.com/):

```bash
npm install
npx cap add android
npx cap sync
cd android && ./gradlew assembleRelease




Accuracy

The app's ephemeris is coarser than the printed Nautical Almanac. The Sun is good to about ±0.6′, stars to ±0.3′, the Moon to ±0.3′, and planets to ±1–2′ (or worse for Jupiter and Saturn). When the app and the printed almanac disagree, trust the printed almanac. The app is a practice tool, not a navigation reference standard.

Expected fix accuracy for celestial positions derived with this app:
Condition	Typical
2 sights of different bodies, good geometry	2–5 nm
3+ sights, bodies ~90° apart	1–3 nm
Running fix, Sun morning + afternoon	3–6 nm
Midday zenith-distance fit (good span)	±0.5–2 nm
Noon latitude from a single sight	±0.5–1 nm
Accuracy of the almanac itself

The built-in almanac is computed from the same ephemeris as the app — Meeus, Astronomical Algorithms, with the ELP-2000 series for the Moon and JPL approximate elements for the planets. It is suitable for practice and for cross-checking, not for primary navigation.
Contributing

Bug reports and suggestions welcome — please open an issue on GitHub.
Credits

    Sextant diagram: Joaquim Alves Gaspar, Wikimedia Commons, Marine sextant.svg, CC BY-SA 3.0.

    Moon position: ELP-2000/82 truncated series, from Meeus, Astronomical Algorithms.

    Sun position: Meeus low-precision solar coordinates.

    Planet positions: JPL approximate Keplerian elements (Standish), with light-time, aberration and precession applied.

    Star catalogue: J2000 positions with proper motion and IAU 1976 precession.
