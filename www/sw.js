// Sextant Trainer — offline-first service worker
// Bump CACHE whenever index.html / assets change so returning users get the new build.
const CACHE = 'sextant-v1.0.1';
const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './Marine_sextant.svg',
  './icon-192.png',
  './icon-512.png'
];

self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE);
    // Add each asset independently so a single 404 doesn't abort the install.
    await Promise.all(ASSETS.map(async url => {
      try { await cache.add(new Request(url, { cache: 'reload' })); }
      catch (err) { console.warn('SW cache miss:', url, err); }
    }));
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  event.respondWith((async () => {
    const cached = await caches.match(event.request);
    if (cached) return cached;
    try {
      const res = await fetch(event.request);
      if (res.ok && res.type === 'basic') {
        const copy = res.clone();
        caches.open(CACHE).then(c => c.put(event.request, copy));
      }
      return res;
    } catch (err) {
      if (event.request.mode === 'navigate') {
        return caches.match('./index.html');
      }
      throw err;
    }
  })());
});