"""
DocAura voice generator — run this on YOUR computer (it needs normal internet).
Uses Microsoft's free natural Indian-English neural voices:
  Priya (girl) -> en-IN-NeerjaNeural
  Doci  (boy)  -> en-IN-PrabhatNeural

Steps:
  1. Install Python (python.org) if you don't have it.
  2. Open a terminal / Command Prompt and run:   pip install edge-tts
  3. Run:   python make_docaura_voices.py
  4. Upload the created file  docaura_voices.zip  back to Claude.
"""
import asyncio
import os
import zipfile

import edge_tts

GIRL = "en-IN-NeerjaNeural"
BOY = "en-IN-PrabhatNeural"

# (file key, speaker, line)   P = Priya, D = Doci, B = both together
LINES = [
    ("p1", "P", "Arey yaar! Interview is tomorrow, and I don't have a resume!"),
    ("d1", "D", "Relax, Priya. Why so much tension?"),
    ("p2", "P", "Every site says login first, then pay four ninety-nine to download! Daylight robbery!"),
    ("d2", "D", "Chill, madam. Just use..."),
    ("d3", "D", "Doc Aura!"),
    ("p3", "P", "Wait, wait, wait. No login?"),
    ("d4", "D", "No login. No sign-up. Hundred percent free. Promise!"),
    ("p4", "P", "But I'm applying for a Data Analyst job only."),
    ("d5", "D", "Simple! Pick your job role, and get a resume made for it."),
    ("p5", "P", "Superb! And my certificate PDF has a spelling mistake, yaar."),
    ("d6", "D", "Same site only! Edit, merge, compress your PDF. Done!"),
    ("p6", "P", "Resume done in two minutes? I'm getting so much aura!"),
    ("c0", "B", "Say it with us!"),
    ("c1", "B", "Doc!"),
    ("c2", "B", "Aura!"),
    ("c3", "B", "Doc Aura!"),
    ("d8", "D", "Doc Aura dot github dot io. Go, go, go!"),
]

# small tweaks so they sound lively, not flat
STYLE = {
    "P": dict(voice=GIRL, rate="+8%", pitch="+6Hz"),
    "D": dict(voice=BOY, rate="+8%", pitch="+0Hz"),
}

OUT = "voices"


async def main():
    os.makedirs(OUT, exist_ok=True)
    for key, who, text in LINES:
        speakers = ["P", "D"] if who == "B" else [who]
        for sp in speakers:
            st = STYLE[sp]
            path = os.path.join(OUT, f"{key}_{sp}.mp3")
            await edge_tts.Communicate(text, st["voice"], rate=st["rate"], pitch=st["pitch"]).save(path)
            print("saved", path)


asyncio.run(main())
