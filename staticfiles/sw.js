const CACHE = 'tezsot-v1';

self.addEventListener('install', e => {
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(clients.claim());
});

self.addEventListener('push', e => {
  let data = { title: 'TezSot', body: 'Yangi xabar', icon: '/static/img/iconlogo.png', url: '/' };
  try {
    if (e.data) data = { ...data, ...e.data.json() };
  } catch (_) { data.body = e.data.text(); }
  e.waitUntil(self.registration.showNotification(data.title, {
    body: data.body, icon: data.icon, badge: '/static/img/iconlogo.png',
    vibrate: [200, 100, 200], data: { url: data.url },
    tag: 'tezsot-' + Date.now(), renotify: true
  }));
});

self.addEventListener('notificationclick', e => {
  e.notification.close();
  const url = e.notification.data?.url || '/';
  e.waitUntil(clients.matchAll({ type: 'window', includeUncontrolled: true }).then(cls => {
    for (const c of cls) if (c.url === url && 'focus' in c) return c.focus();
    return clients.openWindow(url);
  }));
});
