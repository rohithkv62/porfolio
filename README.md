# Build 3D Scroll-Animated Websites — Antigravity Skill Pack

Hey — you commented **"AI"** on the reel, so here's the full setup.

This pack contains the exact Antigravity skill I used to build the 3D scroll-animated site from the video, plus the 7 deep-dive guides on the stack, the scroll-animation math, the design system, and every pattern I layered in.

By the end of this README you'll have:

1. The skill installed for Antigravity
2. A new Next.js project scaffolded with the full stack
3. A working canvas frame-sequence scroll animation playing in your browser

Expected time: **~1 hour**, same as the reel.

---

## What's in this pack

```
skill-pack/
├── README.md                           ← you are here
└── 3d-scroll-website/
    ├── SKILL.md                        ← the skill (install this)
    └── references/
        ├── 01-tech-stack.md            ← every library + exact version
        ├── 02-animation-techniques.md  ← Framer Motion, CSS 3D, SVG paths, typewriter
        ├── 03-scroll-animation-deep-dive.md  ← the frame-sequence math
        ├── 04-design-patterns.md       ← neumorphic shadows, palette, typography
        ├── 05-component-architecture.md  ← file layout + SSR rules
        ├── 06-performance-optimization.md  ← RAF, direct DOM, preloading
        └── 07-antigravity-guide.md     ← prompting tips + workflow
```

---

---

## Step 1 — Install the skill

Antigravity can be configured to use skills or instructions from a specific directory. You can save this skill folder in your workspace or Antigravity's settings directory:

**macOS / Linux:**

```bash
mkdir -p ~/.gemini/antigravity-ide/skills
cp -r 3d-scroll-website ~/.gemini/antigravity-ide/skills/
```

**Windows (PowerShell):**

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.gemini\antigravity-ide\skills"
Copy-Item -Recurse 3d-scroll-website "$HOME\.gemini\antigravity-ide\skills\"
```

That's it. The next time you work with Antigravity, it will have access to these instructions.

### Verify the install

Start Antigravity in your workspace and ask:

> what skills or context documents do you have available?

You should see `3d-scroll-website` in its awareness. If you don't, you can explicitly ask Antigravity to read the `SKILL.md` file to load its instructions.

---

## Step 2 — Build your site

Open a terminal in an empty folder where you want the new project, open Antigravity, and provide a prompt like:

> Build me a premium 3D scroll-animated landing page for a design agency called "Northlight." Use the 3d-scroll-website skill guidelines. The hero should have a canvas frame-sequence animation, then a projects showcase section, a bento features grid, testimonials, an FAQ, and a final call-to-action.

Or keep it simple:

> Scaffold a new 3D scroll-animated site based on the 3d-scroll-website skill. I'll tell you what I want section by section.

Antigravity will read the skill, scaffold the Next.js project, install dependencies, wire up Lenis smooth scroll, and start building sections.

---

## Step 3 — Add your frame sequence

The hero canvas animation needs **pre-rendered frames** (100–120 JPG images exported from Blender, Cinema 4D, or After Effects). The skill handles all the code; you supply the frames.

Three ways to get frames:

1. **Render your own** — animate a 4-second shot in Blender at 24–30 fps, export as JPG sequence.
2. **Commission an artist** — any 3D freelancer can deliver a frame sequence in a day or two.
3. **Use a stock sequence** — some stock sites sell product-animation sequences ready to drop in.

Place the frames in `public/frames/` named `frame_0001.jpg`, `frame_0002.jpg`, etc. The skill file explains the exact naming convention under "Asset pipeline."

If you don't have frames yet, ask Antigravity to build the site with placeholder frames and swap them in later — everything will still work.

---

## Troubleshooting

**"The skill isn't being recognized by Antigravity."**
Make sure the path is correct or simply attach the `SKILL.md` file as context directly into your Antigravity chat session.

**"The scroll animation is janky."**
Check the performance rules in `references/06-performance-optimization.md`. Nine times out of ten it's one of: scroll handler updating React state on every tick, canvas missing DPR scaling, or frames not finishing preload before scrolling starts.

**"Next.js errors about App Router / RSC."**
The skill pins Next.js 16, which has breaking changes from earlier versions. If Antigravity is writing code that looks like Next 13/14 patterns, tell it to read `node_modules/next/dist/docs/` for the current API.

**"Something feels off on Safari / iOS."**
Lenis needs Safari-specific config (higher `lerp`, `syncTouch: false`). The skill covers this under "Smooth scroll (Lenis)" but if Antigravity skipped it, ask explicitly for the Safari-safe Lenis config.

---

## Want help going further?

Book a 30-min session and I'll walk through your project live:
[**calendly.com/abhishek-devini/30min**](https://calendly.com/abhishek-devini/30min)

— Abhishek / Devini
