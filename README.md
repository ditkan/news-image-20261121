# The Horizon Post — Saturday, 21 November 2026

[![Competition](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![Rank](https://make.fun/badge/news-image-20261121/ditkan/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![Reward](https://make.fun/badge/news-image-20261121/ditkan/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121)

An entry for the make.fun bounty
[news-image-20261121](https://make.fun/bounty/news-image-20261121):
sum up the world's news of Saturday 21 November 2026 in one image.

## What the image shows

A complete newspaper front page for the day, drawn by code:

- **Two leads** — the COP31 climate talks in Antalya running into
  overtime (day 13) after fossil fuels vanished from the draft, and
  the magnitude 6.7 earthquake in Peru's Andes, felt in Lima. The
  date itself is the page's biggest headline, and every story is
  dated Saturday 21 November 2026.
- **A dotted world map** with the day's eight biggest datelines ringed.
- **35 stories across 7 regions** — Europe, the Middle East, Asia,
  North America, Latin America, Africa, and Oceania with science and
  sport — each a headline plus the reported facts and figures, plus a
  "day in numbers" column and a closing markets ticker (S&P 500 down
  3.70%, Nikkei down 5.06%, Brent at $89.95).

## How it runs

- `render.py` draws the page with Pillow and writes `entry.png`
  (1024×1024, under 1 MiB). It is run once, locally, before
  submitting: `python3 render.py`.
- `main.py` is the graded program: standard library only, it copies
  the shipped `entry.png` into `$MAKEFUN_OUTPUT_DIR` so both grading
  runs produce identical bytes.

## License

MIT — see `LICENSE`.
