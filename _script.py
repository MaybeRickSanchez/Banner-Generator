from PIL import Image
import os

alphabet_path = "Alphabets"
background_path = "backgrounds"
output_path = "UniCodes"

os.makedirs(output_path, exist_ok=True)

widths = {
    "A":6,"B":5,"C":4,"D":5,"E":4,"F":4,"G":5,"H":5,"I":2,"J":5,"K":6,"L":5,"M":7,"N":6,"O":5,"P":5,"Q":6,"R":5,"S":4,"T":6,
    "U":5,"V":5,"W":7,"X":7,"Y":6,"Z":6,
    "_":3," ":3
}

ranks = []

alphabets = {}
for f in os.listdir(alphabet_path):
    if f.lower().endswith(".png"):
        alphabets[f.split(".")[0]] = Image.open(os.path.join(alphabet_path, f)).convert("RGBA")

backgrounds = []
for i in range(1,15):
    p = os.path.join(background_path, f"BG{i}.png")
    if os.path.exists(p):
        backgrounds.append(Image.open(p).convert("RGBA"))

def build(rank, bg):
    chars = []
    total_w = 3
    for c in rank:
        if c == "-":
            total_w += 2
            continue
        w = widths.get(c,5)
        chars.append((c,w))
        total_w += w + 1
    total_w += 2

    h = bg.height
    w = total_w
    img = Image.new("RGBA", (w, h), (0,0,0,0))
    img.paste(bg.resize((w,h)), (0,0))

    x = 3
    for c,w in chars:
        if c == " ":
            x+=3
            continue
        if c == "-":
            x+=2
            continue
        if c in alphabets:
            glyph = alphabets[c]
            img.paste(glyph, (x,2), glyph)
        x += w + 1

    return img

for idx, rank in enumerate(ranks, start=1):
    bg = backgrounds[(idx-1) % len(backgrounds)]
    out = build(rank, bg)
    out.save(os.path.join(output_path, f"{rank.replace(' ','_')}.png"))
