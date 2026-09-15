import sys

html_file = r"c:\porfolio-website\index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace CSS
css_to_replace_start = "    /* Minimal Loader */"
css_to_replace_end = "    .letter24 { animation-delay: calc(3.5s / 24 * (24 - 24) * -1); }"

new_css = """    /* Minimal Loader */
    .loader-overlay {
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      z-index: 9999;
      background: #02060d;
      transition: opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.6s;
    }
    .loader-overlay.hidden {
      opacity: 0; visibility: hidden; pointer-events: none;
    }

.loader {
    width: 100%; height: 100%; position: relative; display: flex;
    justify-content: center; align-items: center; overflow: hidden;
    background: radial-gradient(circle at center, rgba(0, 220, 255, 0.08), transparent 38%), #02060d;
    font-family: Arial, Helvetica, sans-serif; color: white;
}
.loader::before {
    content: ""; position: absolute; inset: 0;
    background: linear-gradient(rgba(0, 220, 255, 0.025) 1px, transparent 1px), linear-gradient(90deg, rgba(0, 220, 255, 0.025) 1px, transparent 1px);
    background-size: 50px 50px; animation: gridMove 8s linear infinite;
}
@keyframes gridMove { from { transform: translateY(0); } to { transform: translateY(50px); } }
.particles { position: absolute; inset: 0; overflow: hidden; }
.particle { position: absolute; width: 3px; height: 3px; background: #00eaff; border-radius: 50%; box-shadow: 0 0 8px #00eaff, 0 0 18px #00eaff; opacity: 0; animation: particleMove linear infinite, particleBlink ease-in-out infinite; }
.particle:nth-child(1) { left: 8%; top: 80%; animation-duration: 7s, 1.5s; }
.particle:nth-child(2) { left: 18%; top: 20%; animation-duration: 9s, 2s; }
.particle:nth-child(3) { left: 30%; top: 70%; animation-duration: 6s, 1.2s; }
.particle:nth-child(4) { left: 42%; top: 15%; animation-duration: 8s, 2.5s; }
.particle:nth-child(5) { left: 55%; top: 80%; animation-duration: 10s, 1.8s; }
.particle:nth-child(6) { left: 67%; top: 30%; animation-duration: 7s, 2s; }
.particle:nth-child(7) { left: 78%; top: 65%; animation-duration: 8s, 1.5s; }
.particle:nth-child(8) { left: 90%; top: 25%; animation-duration: 6s, 2.2s; }
@keyframes particleMove { 0% { transform: translateY(100px) translateX(0); } 50% { transform: translateY(-100px) translateX(30px); } 100% { transform: translateY(-300px) translateX(-20px); } }
@keyframes particleBlink { 0%, 100% { opacity: 0; } 50% { opacity: 1; } }
.hud { width: min(1100px, 90vw); height: 650px; position: relative; display: flex; flex-direction: column; justify-content: center; align-items: center; z-index: 5; }
.hud-circle { position: absolute; width: 650px; height: 650px; border: 2px solid rgba(0, 234, 255, 0.8); border-radius: 50%; box-shadow: 0 0 15px rgba(0, 234, 255, 0.35), inset 0 0 40px rgba(0, 234, 255, 0.03); animation: circleRotate 18s linear infinite, circlePulse 3s ease-in-out infinite; }
.hud-circle::before { content: ""; position: absolute; inset: 18px; border: 1px dashed rgba(0, 234, 255, 0.15); border-radius: 50%; animation: circleRotateReverse 12s linear infinite; }
.hud-circle::after { content: ""; position: absolute; inset: -5px; border-radius: 50%; border-top: 2px solid transparent; border-right: 2px solid #00eaff; border-bottom: 2px solid transparent; border-left: 2px solid transparent; animation: circleRotate 4s linear infinite; }
@keyframes circleRotate { to { transform: rotate(360deg); } }
@keyframes circleRotateReverse { to { transform: rotate(-360deg); } }
@keyframes circlePulse { 0%, 100% { opacity: 0.65; transform: scale(1); } 50% { opacity: 1; transform: scale(1.015); } }
.music { position: relative; z-index: 10; height: 70px; display: flex; align-items: center; gap: 22px; margin-bottom: 20px; }
.music-icon { font-size: 45px; color: #00eaff; filter: drop-shadow(0 0 8px #00eaff) drop-shadow(0 0 20px rgba(0, 234, 255, 0.5)); animation: musicBounce 0.9s ease-in-out infinite; }
@keyframes musicBounce { 0%, 100% { transform: translateY(0) rotate(-4deg); } 50% { transform: translateY(-10px) rotate(4deg); } }
.equalizer { height: 50px; display: flex; align-items: center; gap: 8px; }
.bar { width: 4px; height: 20px; background: #00eaff; box-shadow: 0 0 8px #00eaff, 0 0 16px rgba(0, 234, 255, 0.7); animation: equalizer 0.8s ease-in-out infinite alternate; }
.bar:nth-child(1) { animation-delay: 0.1s; } .bar:nth-child(2) { animation-delay: 0.3s; } .bar:nth-child(3) { animation-delay: 0.05s; } .bar:nth-child(4) { animation-delay: 0.4s; } .bar:nth-child(5) { animation-delay: 0.2s; } .bar:nth-child(6) { animation-delay: 0.5s; } .bar:nth-child(7) { animation-delay: 0.15s; } .bar:nth-child(8) { animation-delay: 0.35s; } .bar:nth-child(9) { animation-delay: 0.25s; } .bar:nth-child(10) { animation-delay: 0.45s; }
@keyframes equalizer { from { height: 8px; } to { height: 45px; } }
.title-wrapper { position: relative; z-index: 20; margin-bottom: 45px; animation: titleEntrance 1.2s ease-out; }
.title { position: relative; font-size: clamp(38px, 6vw, 78px); font-weight: 900; font-style: italic; letter-spacing: -2px; white-space: nowrap; color: #00eaff; text-shadow: 0 0 8px rgba(0, 234, 255, 0.9), 0 0 25px rgba(0, 234, 255, 0.4); animation: titleGlow 2s ease-in-out infinite; }
.title::before, .title::after { content: attr(data-text); position: absolute; left: 0; top: 0; width: 100%; overflow: hidden; pointer-events: none; }
.title::before { color: #ff0055; transform: translate(-2px, 0); clip-path: inset(0 0 65% 0); animation: glitchRed 2.5s infinite; }
.title::after { color: #00ffff; transform: translate(2px, 0); clip-path: inset(65% 0 0 0); animation: glitchBlue 1.8s infinite; }
@keyframes glitchRed { 0%, 90%, 100% { transform: translate(0); } 92% { transform: translate(-5px, -2px); } 94% { transform: translate(4px, 2px); } 96% { transform: translate(-2px, 1px); } }
@keyframes glitchBlue { 0%, 88%, 100% { transform: translate(0); } 90% { transform: translate(5px, 1px); } 93% { transform: translate(-4px, -2px); } 95% { transform: translate(2px, 2px); } }
@keyframes titleGlow { 0%, 100% { filter: brightness(1); } 50% { filter: brightness(1.3); } }
@keyframes titleEntrance { from { opacity: 0; transform: scale(0.8); filter: blur(15px); } to { opacity: 1; transform: scale(1); filter: blur(0); } }
.scanline { position: absolute; left: 0; right: 0; height: 2px; background: linear-gradient(90deg, transparent, #00eaff, transparent); box-shadow: 0 0 12px #00eaff; opacity: 0.5; animation: scan 3s linear infinite; }
.scanline:nth-child(2) { animation-delay: 1.5s; }
@keyframes scan { 0% { top: 10%; opacity: 0; } 20% { opacity: 0.7; } 50% { opacity: 0.2; } 100% { top: 90%; opacity: 0; } }
.progress-container { position: relative; z-index: 20; width: min(850px, 80vw); }
.progress-frame { position: relative; height: 80px; padding: 10px 18px; border: 2px solid #00eaff; clip-path: polygon(3% 0, 97% 0, 100% 50%, 97% 100%, 3% 100%, 0 50%); background: rgba(0, 234, 255, 0.025); box-shadow: 0 0 12px rgba(0, 234, 255, 0.6), inset 0 0 20px rgba(0, 234, 255, 0.05); overflow: hidden; }
.progress-track { width: 100%; height: 100%; position: relative; background: rgba(0, 234, 255, 0.03); overflow: hidden; clip-path: polygon(2% 0, 98% 0, 100% 50%, 98% 100%, 2% 100%, 0 50%); }
.progress-fill { height: 100%; width: 0%; position: relative; background: repeating-linear-gradient(135deg, #00eaff 0px, #00eaff 15px, #8fffff 15px, #8fffff 20px); box-shadow: 0 0 15px #00eaff, 0 0 35px rgba(0, 234, 255, 0.7); animation: progressMove 1s linear infinite, progressGlow 1.5s ease-in-out infinite; }
@keyframes progressMove { from { background-position: 0 0; } to { background-position: 40px 0; } }
@keyframes progressGlow { 0%, 100% { filter: brightness(1); } 50% { filter: brightness(1.5); } }
.progress-fill::after { content: ""; position: absolute; top: 0; left: -100px; width: 100px; height: 100%; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.8), transparent); animation: shine 1.8s linear infinite; }
@keyframes shine { from { left: -100px; } to { left: 100%; } }
.percentage { position: absolute; right: 30px; top: 50%; transform: translateY(-50%); font-size: 25px; font-weight: bold; color: #00eaff; text-shadow: 0 0 8px #00eaff, 0 0 20px #00eaff; z-index: 5; }
.loading-text { margin-top: 35px; font-size: 21px; font-weight: 600; letter-spacing: 12px; color: #00eaff; text-shadow: 0 0 8px #00eaff, 0 0 20px rgba(0, 234, 255, 0.5); animation: loadingGlow 1.2s ease-in-out infinite; }
@keyframes loadingGlow { 0%, 100% { opacity: 0.45; letter-spacing: 10px; } 50% { opacity: 1; letter-spacing: 15px; } }
.dots { display: flex; align-items: center; gap: 12px; margin-top: 25px; }
.dot { width: 8px; height: 8px; border-radius: 50%; background: #00eaff; box-shadow: 0 0 8px #00eaff, 0 0 18px #00eaff; opacity: 0.2; animation: dotPulse 1.4s infinite; }
.dot:nth-child(1) { animation-delay: 0s; } .dot:nth-child(2) { animation-delay: .15s; } .dot:nth-child(3) { animation-delay: .30s; } .dot:nth-child(4) { animation-delay: .45s; } .dot:nth-child(5) { animation-delay: .60s; } .dot:nth-child(6) { animation-delay: .75s; } .dot:nth-child(7) { animation-delay: .90s; } .dot:nth-child(8) { animation-delay: 1.05s; } .dot:nth-child(9) { animation-delay: 1.20s; }
@keyframes dotPulse { 0%, 100% { opacity: 0.15; transform: scale(0.8); } 50% { opacity: 1; transform: scale(1.7); } }
.corner { position: absolute; width: 100px; height: 100px; border-color: rgba(0, 234, 255, 0.5); border-style: solid; animation: cornerPulse 2s ease-in-out infinite; pointer-events: none; }
.corner.top-left { top: 30px; left: 30px; border-width: 2px 0 0 2px; }
.corner.top-right { top: 30px; right: 30px; border-width: 2px 2px 0 0; }
.corner.bottom-left { bottom: 30px; left: 30px; border-width: 0 0 2px 2px; }
.corner.bottom-right { bottom: 30px; right: 30px; border-width: 0 2px 2px 0; }
@keyframes cornerPulse { 0%, 100% { opacity: 0.3; } 50% { opacity: 1; } }
@media (max-width: 700px) { .hud-circle { width: 500px; height: 500px; } .title { font-size: 32px; } .progress-container { width: 85vw; } .loading-text { font-size: 15px; letter-spacing: 7px; } .music { transform: scale(0.8); } }"""

start_idx = content.find(css_to_replace_start)
end_idx = content.find(css_to_replace_end) + len(css_to_replace_end)
content = content[:start_idx] + new_css + content[end_idx:]


# 2. Replace HTML
html_to_replace_start = '  <div class="loader-overlay" id="loader">'
html_to_replace_end = '      <div class="letter letter24">&nbsp;</div>\n    </div>\n  </div>'

new_html = """  <div class="loader-overlay" id="loader">
    <div class="loader">
        <div class="particles"><span class="particle"></span><span class="particle"></span><span class="particle"></span><span class="particle"></span><span class="particle"></span><span class="particle"></span><span class="particle"></span><span class="particle"></span></div>
        <div class="scanline"></div><div class="scanline"></div>
        <div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div>
        <div class="hud">
            <div class="hud-circle"></div>
            <div class="music"><div class="music-icon">♪</div><div class="equalizer"><span class="bar"></span><span class="bar"></span><span class="bar"></span><span class="bar"></span><span class="bar"></span><span class="bar"></span><span class="bar"></span><span class="bar"></span><span class="bar"></span><span class="bar"></span></div></div>
            <div class="title-wrapper"><div class="title" data-text="NEVER GONNA GIVE YOU UP">NEVER GONNA GIVE YOU UP</div></div>
            <div class="progress-container"><div class="progress-frame"><div class="progress-track"><div class="progress-fill" id="progressFill"></div></div><div class="percentage" id="percentage">0%</div></div></div>
            <div class="loading-text">LOADING...</div>
            <div class="dots"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
        </div>
    </div>
  </div>"""

start_idx2 = content.find(html_to_replace_start)
end_idx2 = content.find(html_to_replace_end) + len(html_to_replace_end)
content = content[:start_idx2] + new_html + content[end_idx2:]


# 3. Replace JS
js_to_replace_start = "      const loader = document.getElementById('loader');"
js_to_replace_end = "      }, 3500);"

new_js = """      const loader = document.getElementById('loader');
      const progressFill = document.getElementById("progressFill");
      const percentage = document.getElementById("percentage");
      const title = document.querySelector(".title");
      const hudCircle = document.querySelector(".hud-circle");

      let progress = 0;
      let loadInterval;
      
      if(progressFill && percentage) {
        loadInterval = setInterval(() => {
            progress += Math.random() * 2.5 + 0.5;
            if (progress >= 100) {
                progress = 100;
                clearInterval(loadInterval);
                setTimeout(() => {
                    loader.classList.add('hidden');
                }, 800);
            }
            progressFill.style.width = progress + "%";
            percentage.textContent = Math.floor(progress) + "%";
        }, 60);

        setInterval(() => {
            if (title && Math.random() > 0.65) {
                title.style.transform = `translateX(${Math.random() * 6 - 3}px)`;
                title.style.filter = "brightness(1.8)";
                setTimeout(() => {
                    title.style.transform = "translateX(0)";
                    title.style.filter = "brightness(1)";
                }, 100);
            }
        }, 900);

        setInterval(() => {
            if (hudCircle && Math.random() > 0.7) {
                hudCircle.style.filter = "brightness(1.8)";
                setTimeout(() => {
                    hudCircle.style.filter = "brightness(1)";
                }, 120);
            }
        }, 1200);
      } else {
        setTimeout(() => loader.classList.add('hidden'), 3500);
      }"""

start_idx3 = content.find(js_to_replace_start)
end_idx3 = content.find(js_to_replace_end) + len(js_to_replace_end)
content = content[:start_idx3] + new_js + content[end_idx3:]

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
