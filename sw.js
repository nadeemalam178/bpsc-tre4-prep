// Service Worker for BPSC TRE 4.0 PWA
// Cache v4: Network-First for HTML navigation and JSON data, Cache-First for static assets
const CACHE_NAME = 'bpsc-tre4-v4';
const STATIC_ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './icon-192.svg',
  './icon-512.svg',
  './data/index.json',
  './2026-10-09/daily_quiz_data.json',
  './2026-10-10/daily_quiz_data.json'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(STATIC_ASSETS);
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  
  // 1. Navigation / HTML pages: Always try network first so bug fixes load immediately
  if (req.mode === 'navigate' || req.destination === 'document') {
    event.respondWith(
      fetch(req)
        .then((networkResp) => {
          if (networkResp && networkResp.status === 200) {
            const copy = networkResp.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(req, copy));
          }
          return networkResp;
        })
        .catch(() => caches.match('./index.html'))
    );
    return;
  }

  // 2. Dynamic JSON data (quizzes, index): Network first to get latest syllabus updates
  if (req.url.endsWith('.json')) {
    event.respondWith(
      fetch(req)
        .then((networkResp) => {
          if (networkResp && networkResp.status === 200) {
            const copy = networkResp.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(req, copy));
          }
          return networkResp;
        })
        .catch(() => caches.match(req))
    );
    return;
  }

  // 3. Static assets (images, icons, fonts): Cache first with network fallback
  event.respondWith(
    caches.match(req).then((cachedResp) => {
      if (cachedResp) return cachedResp;
      return fetch(req).then((networkResp) => {
        if (networkResp && networkResp.status === 200) {
          const copy = networkResp.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(req, copy));
        }
        return networkResp;
      });
    })
  );
});
