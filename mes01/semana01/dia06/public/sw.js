// Service Worker para Calculadora Científica
const CACHE_NAME = 'calculadora-cientifica-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/src/main.tsx',
  '/src/index.css',
  '/calculator-icon.svg',
  '/manifest.json'
];

// Instalar Service Worker
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Cache aberto');
        return cache.addAll(urlsToCache);
      })
  );
});

// Buscar recursos do cache
self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        // Cache hit - retorna resposta
        if (response) {
          return response;
        }

        return fetch(event.request).then(
          function(response) {
            // Verifica se recebemos uma resposta válida
            if(!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }

            // IMPORTANTE: Clona a resposta. Uma resposta é um stream
            // e como queremos tanto o browser quanto o cache para consumir a resposta
            // precisamos cloná-la para ter duas streams.
            var responseToCache = response.clone();

            caches.open(CACHE_NAME)
              .then(function(cache) {
                cache.put(event.request, responseToCache);
              });

            return response;
          }
        );
      })
    );
});

// Atualizar Service Worker
self.addEventListener('activate', function(event) {
  var cacheWhitelist = [CACHE_NAME];

  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames.map(function(cacheName) {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});