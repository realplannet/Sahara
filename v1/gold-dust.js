/* Sahara Balinese — ambient scroll-scrubbed gold dust (shared, all pages) */
(function () {
  if (window.__goldDust || document.getElementById('goldCanvas')) return;
  window.__goldDust = true;
  var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function init() {
    if (!document.body) { setTimeout(init, 60); return; }
    var cvs = document.createElement('canvas');
    cvs.id = 'goldDustAmbient';
    cvs.style.cssText = 'position:fixed;inset:0;width:100vw;height:100vh;z-index:3;pointer-events:none;';
    document.body.appendChild(cvs);
    var ctx = cvs.getContext('2d');
    var W = 0, H = 0, DPR = 1;
    function fit() {
      DPR = Math.min(window.devicePixelRatio || 1, 2);
      W = window.innerWidth; H = window.innerHeight;
      cvs.width = W * DPR; cvs.height = H * DPR;
    }
    fit();
    window.addEventListener('resize', fit);

    // particle count scales with viewport; lighter on mobile
    var N = Math.round(Math.max(80, Math.min(220, W * H / 5000)));
    if (W < 840) N = Math.min(N, 110);
    var dust = [];
    for (var i = 0; i < N; i++) dust.push({
      x: Math.random(), y: Math.random(),
      z: 0.25 + Math.random() * 0.75,
      r: 0.4 + Math.random() * 1.2,
      ph: Math.random() * 6.283,
      sp: 0.15 + Math.random() * 0.6
    });
    // a few drifting petal glints
    var petals = [];
    for (var k = 0; k < (W < 840 ? 4 : 7); k++) petals.push({
      x: Math.random(), y: Math.random(),
      z: 0.35 + Math.random() * 0.65,
      a: Math.random() * 6.283,
      spin: (Math.random() - 0.5) * 0.6,
      sz: 5 + Math.random() * 7,
      sp: 0.08 + Math.random() * 0.2
    });

    var scroll = 0, raf = 0, running = true;
    function draw(t) {
      ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
      ctx.clearRect(0, 0, W, H);
      var i, d, px, py, tw;
      for (i = 0; i < dust.length; i++) {
        d = dust[i];
        d.y -= 0.00014 * d.sp;
        if (d.y < -0.02) { d.y = 1.02; d.x = Math.random(); }
        tw = 0.10 + 0.42 * Math.abs(Math.sin(t * d.sp + d.ph));
        px = d.x * W + Math.sin(t * 0.3 * d.sp + d.ph) * 12 * d.z;
        py = (d.y * H + scroll * H * 0.45 * (1 - d.z) + H) % (H * 1.04) - H * 0.02;
        ctx.fillStyle = 'rgba(240,203,106,' + (tw * d.z * 0.55).toFixed(3) + ')';
        ctx.beginPath();
        ctx.arc(px, py, d.r * d.z, 0, 6.283);
        ctx.fill();
      }
      for (i = 0; i < petals.length; i++) {
        var p = petals[i];
        p.y -= 0.00008 * p.sp * 10;
        if (p.y < -0.05) { p.y = 1.05; p.x = Math.random(); }
        px = p.x * W + Math.sin(t * 0.2 + p.a) * 22 * p.z;
        py = (p.y * H + scroll * H * 0.6 * (1 - p.z) + H) % (H * 1.1) - H * 0.05;
        ctx.save();
        ctx.translate(px, py);
        ctx.rotate(p.a + t * p.spin + scroll * 2.4);
        ctx.fillStyle = 'rgba(219,168,60,' + (0.10 + 0.10 * p.z).toFixed(3) + ')';
        ctx.strokeStyle = 'rgba(246,214,132,' + (0.14 + 0.12 * p.z).toFixed(3) + ')';
        ctx.lineWidth = 0.8;
        ctx.beginPath();
        ctx.ellipse(0, 0, p.sz * p.z, p.sz * 0.38 * p.z, 0, 0, 6.283);
        ctx.fill();
        ctx.stroke();
        ctx.restore();
      }
    }
    function loop(tms) {
      if (!running) return;
      var t = tms / 1000;
      var max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
      var target = Math.min(1, Math.max(0, window.scrollY / max));
      scroll += (target - scroll) * 0.07;
      draw(t);
      raf = requestAnimationFrame(loop);
    }
    if (reduced) { scroll = 0; draw(1); return; }
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) { running = false; cancelAnimationFrame(raf); }
      else if (!running) { running = true; raf = requestAnimationFrame(loop); }
    });
    raf = requestAnimationFrame(loop);
  }
  init();
})();
