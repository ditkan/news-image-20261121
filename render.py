#!/usr/bin/env python3
"""Render the Horizon Post front page for Saturday 21 November 2026.

Draws a complete newspaper front page -- masthead, two lead stories, a
dotted world map with the day's datelines, seven regional sections and a
markets ticker -- onto a 1024x1024 canvas and saves it as entry.png.
Runs locally with Pillow; the shipped main.py only copies the result.
"""

import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W = H = 1024
MARGIN = 26
CW = W - 2 * MARGIN  # content width

PAPER = (247, 243, 233)
INK = (18, 16, 12)
RED = (138, 28, 28)
GREY = (110, 102, 88)
HAIR = (168, 158, 138)
DARK = (24, 22, 18)

FONT_DIR = "/usr/share/fonts/truetype/noto"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_SERIF_BLACK = font("NotoSerifDisplay-Black.ttf", 57)
F_SERIF_BOLD = font("NotoSerif-Bold.ttf", 21)
F_SERIF_BOLD_S = font("NotoSerif-Bold.ttf", 17)
F_SANS_BOLD = font("NotoSans-Bold.ttf", 12)
F_SANS_BOLD_S = font("NotoSans-Bold.ttf", 10)
F_SANS = font("NotoSans-Regular.ttf", 10)
F_BODY = font("NotoSans-Regular.ttf", 10)
F_HEAD = font("NotoSans-Bold.ttf", 12)
F_SEC = font("NotoSans-Bold.ttf", 13)
F_KICK = font("NotoSans-Bold.ttf", 10)
F_BAND = font("NotoSans-Bold.ttf", 20)
F_BAND_S = font("NotoSans-Bold.ttf", 11)
F_TICK = font("NotoSans-Bold.ttf", 11)


def wrap_px(draw, text, fnt, width):
    """Greedy word wrap measured in pixels."""
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- stories
LEADS = [
    {
        "kicker": "LEAD · ANTALYA, TURKIYE",
        "head": "COP31 Talks Run Into Overtime as Fossil Fuels Vanish From the Draft",
        "body": (
            "The UN climate summit missed its Friday deadline and worked on "
            "into Saturday, split over how fast the world should quit coal, "
            "oil and gas after a draft deal dropped any mention of fossil "
            "fuels at all."
        ),
    },
    {
        "kicker": "LEAD · NEW YORK",
        "head": "Anthropic's $81 Billion Debut Is the Biggest IPO in History",
        "body": (
            "The AI company raised $81.3 billion and opened near a $2 "
            "trillion market value on Wall Street, a record first day -- in "
            "the middle of an AI sell-off that turned into tech's worst "
            "week since 2020."
        ),
    },
]

SECTIONS = [
    ("EUROPE", [
        ("MISSILE HITS ZELENSKY'S HOMETOWN",
         "A Russian ballistic missile struck central Kryvyi Rih, killing "
         "two people and wounding 60. Kyiv says Russia launched 3 missiles "
         "and 148 drones overnight; 117 drones were downed."),
        ("KYIV BRIDGES, POWER HIT",
         "Russian strikes on the capital killed three people, injured "
         "nine and damaged bridges and transport links, cutting power."),
        ("CRIMEA BRIDGE HIT A THIRD TIME IN FOUR DAYS",
         "Ukraine struck the Kerch bridge to Crimea again, its latest "
         "blow against the supply line Russia uses to feed the peninsula."),
        ("DENMARK RATIFIES GREENLAND DEAL 109-0",
         "Parliament in Copenhagen voted unanimously for a security pact "
         "that gives the United States two new bases in Greenland."),
        ("FRENCH POLICE SENTENCED IN ZECLER CASE",
         "A Paris court sentenced the officers filmed in the racist "
         "beating of music producer Michel Zecler, six years on."),
    ]),
    ("MIDDLE EAST", [
        ("SAUDI AIR DEFENCE DROPS 3 MISSILES OVER RIYADH",
         "Defences destroyed three Houthi ballistic missiles fired at "
         "the capital before dawn on Saturday -- the second attack on "
         "Riyadh in days."),
        ("IRAN READIES A TANKER CONVOY",
         "Tehran is preparing more than 14 oil tankers to sail through "
         "the US naval blockade, officials said."),
        ("TWO TANKERS ATTACKED OFF OMAN",
         "Britain's UKMTO reporting centre logged attacks on two "
         "tankers near Khasab, at the mouth of the Gulf."),
        ("SIX KILLED IN ISRAELI STRIKES ON GAZA",
         "Medics in Gaza said Israeli strikes killed six people, as "
         "the future of the ceasefire stayed in doubt."),
        ("TURKIYE TAKES CONTROL OF OPPOSITION TV",
         "Authorities in Istanbul took control of Sozcu TV, the "
         "opposition broadcaster, in a widening media crackdown."),
    ]),
    ("ASIA", [
        ("THREE RIVALS SIGN SHENZHEN DECLARATION",
         "Trump, Xi and Putin met in Shenzhen and signed a four-point "
         "peace declaration at their first summit together. It said "
         "nothing about Ukraine."),
        ("WORLD COURT: MYANMAR COMMITTED GENOCIDE",
         "The ICJ at The Hague found Myanmar responsible for genocide "
         "against the Rohingya, the first such ruling against a state."),
        ("NORTH KOREA EXPANDS YONGBYON PLANT",
         "The UN nuclear watchdog says Pyongyang is enlarging its "
         "uranium enrichment plant at Yongbyon."),
        ("VIOLENCE FLARES BEFORE HASINA'S RETURN",
         "Clashes spread in Bangladesh as exiled former prime "
         "minister Sheikh Hasina planned her return to Dhaka."),
        ("KOREA EXPORTS TOP $1 TRILLION",
         "Exports topped $1 trillion in a year for the first time, "
         "powered by chip demand."),
    ]),
    ("NORTH AMERICA", [
        ("S&P 500 SLIDES 3.7% IN AI SELL-OFF",
         "Wall Street's plunge led a global rout: Japan's Nikkei fell "
         "5.06% and London's FTSE 100 lost 1.02% as investors doubted "
         "AI spending will ever pay off."),
        ("TRUMP CURBS CONTRACTORS' WORD TO CONGRESS",
         "An executive order tells federal contractors to notify the "
         "White House before sharing information with Congress."),
        ("FBI CRIMINAL DATABASE HACKED",
         "Intruders breached the FBI's criminal information database, "
         "CNN reported; the bureau says it is investigating."),
        ("BUFFETT QUADRUPLES THANKSGIVING GIFTS",
         "Warren Buffett sharply raised his traditional holiday "
         "giving to the foundations run by his children."),
    ]),
    ("LATIN AMERICA", [
        ("PERU QUAKE: MAGNITUDE 6.7 IN THE ANDES",
         "A deep quake near Junin, at 00:09 GMT and 108 km down, shook "
         "buildings in Lima and sent residents into the streets. No "
         "deaths and only minor damage were reported."),
        ("MEXICO CAPTURES 'EL CHAPO ISIDRO'",
         "Federal forces seized Fausto Isidro Meza Flores, an FBI "
         "most-wanted cartel boss, in Guasave, Sinaloa. Violence "
         "followed the arrest."),
        ("MOSQUITOES CUT DENGUE BY 69% IN BRAZIL",
         "Releasing Wolbachia-carrying mosquitoes cut dengue cases "
         "by 69% in the trial cities, researchers reported."),
        ("US SIGNS MILITARY DEAL WITH VENEZUELA",
         "Washington's new pact with Caracas comes ten months after "
         "US forces removed Nicolas Maduro from power."),
    ]),
    ("AFRICA", [
        ("700,000 DISPLACED IN SOUTHERN ETHIOPIA",
         "Fighting has driven some 700,000 people from their homes "
         "in Ethiopia's south, aid agencies said."),
        ("SOMALIA EXPELS THE UAE AMBASSADOR",
         "Mogadishu ordered out the Emirates' envoy as the row over "
         "UAE bases and influence in the country deepened."),
        ("KENYA ORDERS POLICE HEADCOUNT",
         "Nairobi ordered a nationwide police headcount amid concern "
         "about Russian military recruitment of Kenyans."),
        ("SOUTH AFRICA HOLDS RATES AT 7.25%",
         "The Reserve Bank kept its key rate unchanged while the "
         "global sell-off battered emerging markets."),
        ("WHO WARNS ON EBOLA CHILD DEATHS IN CONGO",
         "The WHO warned child deaths are running high in Congo's "
         "Ebola outbreak as teams race to contain it."),
    ]),
    ("OCEANIA · SCIENCE · SPORT", [
        ("BEPICOLOMBO REACHES MERCURY AT LAST",
         "After an eight-year cruise, the European-Japanese probe "
         "slipped into orbit around Mercury."),
        ("AIR NIUGINI JET LANDS SAFELY",
         "An Air Niugini flight made an emergency landing in Papua "
         "New Guinea; everyone on board was safe."),
        ("ENGLAND'S RECORD WIN OVER THE ALL BLACKS",
         "England beat New Zealand by a record margin. Captain Maro "
         "Itoje warned the win 'must not be our ceiling'."),
        ("MOROCCO AND MALI SHINE AT U17 WORLD CUP",
         "Both African sides won big in the latest round of the "
         "Under-17 World Cup."),
        ("AI WEAPONS TALKS END WITHOUT A DEAL",
         "UN talks in Geneva agreed only to keep working on rules "
         "for autonomous weapons. No binding limits were set."),
    ]),
    ("THE DAY IN NUMBERS", [
        ("$81.3 BILLION",
         "raised by Anthropic in the largest stock-market debut "
         "ever recorded, ahead of its first day of trading."),
        ("148 DRONES, 3 MISSILES",
         "launched by Russia at Ukraine overnight, Kyiv says; air "
         "defences brought down 117 of the drones."),
        ("6.7 MAGNITUDE, 108 KM DEEP",
         "the Junin earthquake in Peru's Andes, felt in Lima, with "
         "no deaths reported by Saturday night."),
        ("3 MISSILES OVER RIYADH",
         "Houthi ballistic missiles intercepted over the Saudi "
         "capital before dawn, the second attack in days."),
        ("69 PER CENT",
         "the fall in dengue cases in Brazilian cities that "
         "released Wolbachia mosquitoes, researchers found."),
    ]),
]

TICKER = ("MARKETS   S&P 500 6,910  -3.70%   ·   NIKKEI -5.06%   ·   "
          "FTSE 100 10,346  -1.02%   ·   BRENT $89.95  +0.57%   ·   "
          "BITCOIN AT A TWO-YEAR LOW   ·   GAS $3.75  +1.82%")

# Dotted world map on a 96x24 grid (columns ~ longitude, rows ~
# latitude). Each row lists the land spans as (first, last) columns.
MAP_SPANS = {
    1: [(10, 26), (30, 34), (58, 66), (74, 88)],
    2: [(6, 28), (31, 36), (44, 52), (55, 92)],
    3: [(5, 27), (32, 35), (43, 54), (55, 90)],
    4: [(6, 25), (44, 53), (54, 88), (84, 87)],
    5: [(7, 24), (45, 52), (53, 86), (85, 87)],
    6: [(8, 23), (46, 50), (53, 84)],
    7: [(10, 21), (47, 49), (56, 80), (62, 67)],
    8: [(13, 19), (44, 56), (58, 78), (63, 66)],
    9: [(15, 18), (44, 58), (60, 76), (64, 66), (70, 74)],
    10: [(45, 58), (64, 74)],
    11: [(20, 26), (46, 57), (68, 75)],
    12: [(21, 28), (47, 56), (70, 74)],
    13: [(22, 29), (47, 55), (68, 72), (75, 80)],
    14: [(22, 28), (48, 54)],
    15: [(21, 27), (48, 53), (78, 89)],
    16: [(21, 26), (49, 52), (77, 90)],
    17: [(20, 25), (49, 51), (78, 89)],
    18: [(20, 24), (80, 87)],
    19: [(19, 23)],
    20: [(19, 22), (90, 92)],
}
MAP_COLS = 96
MAP_NROWS = 24

# dateline rings on the map grid: (col, row)
MAP_DOTS = [
    (56, 7),    # Antalya, Turkiye -- COP31
    (56, 5),    # Ukraine -- Kryvyi Rih / Kyiv
    (60, 9),    # Riyadh, Saudi Arabia
    (78, 10),   # Shenzhen, China
    (28, 16),   # Junin, Peru
    (19, 9),    # Guasave, Mexico
    (58, 13),   # southern Ethiopia
    (87, 15),   # Papua New Guinea
]
MAP_CAPTION = ("WHERE THE DAY HAPPENED:  1 Antalya COP31  ·  2 Ukraine strikes  ·  "
               "3 Riyadh missiles  ·  4 Shenzhen summit  ·  5 Peru quake  ·  "
               "6 Sinaloa capture  ·  7 Ethiopia displacement  ·  8 Air Niugini landing")


def draw_map(draw, x, y, w, h):
    cell_w = w / MAP_COLS
    cell_h = h / MAP_NROWS
    r = max(1.0, min(cell_w, cell_h) * 0.30)
    for ri, spans in MAP_SPANS.items():
        for first, last in spans:
            for ci in range(first, last + 1):
                cx = x + (ci + 0.5) * cell_w
                cy = y + (ri + 0.5) * cell_h
                draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(96, 90, 78))
    for ci, ri in MAP_DOTS:
        cx = x + (ci + 0.5) * cell_w
        cy = y + (ri + 0.5) * cell_h
        draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], outline=RED, width=2)
        draw.ellipse([cx - 1.6, cy - 1.6, cx + 1.6, cy + 1.6], fill=RED)


def draw_lead(draw, x, y, w, lead):
    draw.text((x, y), lead["kicker"], font=F_KICK, fill=RED)
    y += 15
    for line in wrap_px(draw, lead["head"], F_SERIF_BOLD, w):
        draw.text((x, y), line, font=F_SERIF_BOLD, fill=INK)
        y += 25
    y += 3
    for line in wrap_px(draw, lead["body"], F_BODY, w):
        draw.text((x, y), line, font=F_BODY, fill=(52, 48, 40))
        y += 13
    return y


def draw_section(draw, x, y, w, title, stories):
    draw.text((x, y), title, font=F_SEC, fill=RED)
    draw.line([x, y + 19, x + w, y + 19], fill=INK, width=2)
    y += 25
    for head, body in stories:
        for line in wrap_px(draw, head, F_HEAD, w):
            draw.text((x, y), line, font=F_HEAD, fill=INK)
            y += 13
        for line in wrap_px(draw, body, F_BODY, w):
            draw.text((x, y), line, font=F_BODY, fill=(52, 48, 40))
            y += 11
        y += 5
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # --- masthead ------------------------------------------------------
    kicker = "T H E   W O R L D   I N   O N E   P A G E"
    kw = draw.textlength(kicker, font=F_SANS_BOLD_S)
    draw.text(((W - kw) / 2, 12), kicker, font=F_SANS_BOLD_S, fill=GREY)
    draw.line([MARGIN, 30, W - MARGIN, 30], fill=INK, width=3)

    name = "The Horizon Post"
    nw = draw.textlength(name, font=F_SERIF_BLACK)
    draw.text(((W - nw) / 2, 36), name, font=F_SERIF_BLACK, fill=INK)
    draw.line([MARGIN, 104, W - MARGIN, 104], fill=INK, width=1)

    # --- date band ------------------------------------------------------
    draw.rectangle([MARGIN, 110, W - MARGIN, 142], fill=DARK)
    date = "SATURDAY, 21 NOVEMBER 2026"
    dw = draw.textlength(date, font=F_BAND)
    draw.text(((W - dw) / 2, 116), date, font=F_BAND, fill=(250, 247, 238))
    draw.text((MARGIN + 10, 121), "35 STORIES", font=F_BAND_S, fill=(206, 198, 178))
    r_txt = "7 REGIONS"
    draw.text((W - MARGIN - 10 - draw.textlength(r_txt, font=F_BAND_S), 121),
              r_txt, font=F_BAND_S, fill=(206, 198, 178))

    # --- leads + map row -------------------------------------------------
    top = 154
    lead_w = 300
    draw_lead(draw, MARGIN, top, lead_w, LEADS[0])
    map_x = MARGIN + lead_w + 18
    map_w = CW - 2 * lead_w - 36
    draw.text((map_x, top), "THE WORLD ON SATURDAY", font=F_KICK, fill=RED)
    draw_map(draw, map_x, top + 15, map_w, 106)
    cap_lines = wrap_px(draw, MAP_CAPTION, F_SANS_BOLD_S, map_w)
    cy = top + 126
    for line in cap_lines:
        draw.text((map_x, cy), line, font=F_SANS_BOLD_S, fill=GREY)
        cy += 12
    draw_lead(draw, MARGIN + CW - lead_w, top, lead_w, LEADS[1])
    draw.line([MARGIN + lead_w + 9, top, MARGIN + lead_w + 9, top + 160],
              fill=HAIR, width=1)
    draw.line([MARGIN + CW - lead_w - 9, top, MARGIN + CW - lead_w - 9, top + 160],
              fill=HAIR, width=1)
    grid_top = top + 168
    draw.line([MARGIN, grid_top - 6, W - MARGIN, grid_top - 6], fill=INK, width=2)

    # --- regional grid: 4 columns x 2 rows -------------------------------
    col_w = (CW - 3 * 14) / 4
    row_h = (H - grid_top - 36) / 2
    ends = []
    for i, (title, stories) in enumerate(SECTIONS):
        cx = MARGIN + (i % 4) * (col_w + 14)
        cyy = grid_top + (i // 4) * row_h
        if i % 4:
            draw.line([cx - 7, cyy, cx - 7, cyy + row_h - 12], fill=HAIR, width=1)
        if i // 4:
            draw.line([cx, cyy - 5, cx + col_w, cyy - 5], fill=HAIR, width=1)
        ends.append(draw_section(draw, cx, cyy, col_w, title, stories))
    print("section bottoms:", [round(e) for e in ends], "limit:", H - 40)

    # --- ticker -----------------------------------------------------------
    ty = H - 34
    draw.line([MARGIN, ty - 6, W - MARGIN, ty - 6], fill=INK, width=2)
    tw = draw.textlength(TICKER, font=F_TICK)
    draw.text(((W - tw) / 2 if tw <= CW else MARGIN, ty), TICKER,
              font=F_TICK, fill=INK)

    img.save(OUT, optimize=True)
    print("saved", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
