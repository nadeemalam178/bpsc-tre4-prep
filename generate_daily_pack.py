#!/usr/bin/env python3
"""
BPSC TRE 4.0 Daily Pack & Practice Generator
Automatically creates dated daily study modules and updates progress.
Usage:
    python generate_daily_pack.py                  # Generates today's or next sequential day
    python generate_daily_pack.py --date 2026-10-10 --day 2
"""

import os
import sys
import json
import argparse
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DAY_CURRICULUM = {
    1: {
        "title": "Day 01: Foundations & Core Concepts",
        "m_topics": "Rational Numbers, Divisibility Rules, Food Components & Light Reflection",
        "s_topics": "Real Numbers (Euclid's Algorithm & Irrationality), Polynomials (Zeroes & Coefficients)",
        "gs_topics": "1857 Revolt in Bihar (Veer Kunwar Singh, Pir Ali), Champaran Satyagraha 1917, Bihar Rivers & Geography",
        "lang_topics": "Hindi: संधि एवं समास, वर्तनी शुद्धि | English: Subject-Verb Agreement, Articles"
    },
    2: {
        "title": "Day 02: Linear Relations & Chemical Systems",
        "m_topics": "Fractions, Decimals, Laws of Exponents | Acids, Bases and Salts (pH scale, indicators)",
        "s_topics": "Pair of Linear Equations in Two Variables (Graphical, Substitution, Elimination, Cross-multiplication, Conditions for consistency)",
        "gs_topics": "1942 Quit India Movement in Bihar (Azad Dasta, Jayaprakash Narayan), Soils of Bihar (Bangar, Khadar)",
        "lang_topics": "Hindi: उपसर्ग एवं प्रत्यय, पर्यायवाची शब्द | English: Tenses, Conditional Clauses"
    },
    3: {
        "title": "Day 03: Quadratic Systems & Life Processes",
        "m_topics": "Algebraic Expressions & Standard Identities | Nutrition in Plants (Photosynthesis) & Animals",
        "s_topics": "Quadratic Equations (Factorisation, Completing square, Quadratic formula, Nature of roots discriminant D)",
        "gs_topics": "Non-Cooperation Movement in Bihar (1920-22, Sadakat Ashram, Bihar Vidyapeeth), Climate of Bihar (Norwesters/Kalbaisakhi)",
        "lang_topics": "Hindi: विलोम शब्द, प्रमुख मुहावरे एवं लोकोक्तियाँ | English: Prepositions & Phrasal Verbs"
    },
    4: {
        "title": "Day 04: Progressions & Organism Energy",
        "m_topics": "Linear Equations in One Variable | Respiration in Organisms (Aerobic vs Anaerobic, Breathing rate)",
        "s_topics": "Arithmetic Progressions (AP - nth term, Sum of first n terms Sn, Arithmetic Mean)",
        "gs_topics": "Civil Disobedience Movement & Salt Satyagraha in Bihar (Nakhas Pind Patna), Bihar Irrigation and Canals",
        "lang_topics": "Hindi: अनेकार्थी शब्द, वाक्य शुद्धि | English: Active & Passive Voice rules"
    },
    5: {
        "title": "Day 05: Geometry Foundations & Transport Systems",
        "m_topics": "Comparing Quantities (Percentage, Profit & Loss, Discount) | Transportation in Animals & Plants (Xylem/Phloem, Human Circulatory)",
        "s_topics": "Triangles (Similarity criteria AAA, SAS, SSS, Basic Proportionality Theorem Thales & its converse)",
        "gs_topics": "Bihar Kisan Sabha (Swami Sahajanand Saraswati 1929, Bakasht movement), Major Agro-Climatic Zones of Bihar",
        "lang_topics": "Hindi: तत्सम-तद्भव, कारक एवं विभक्ति | English: Direct & Indirect Speech rules"
    }
}

def get_next_day_info():
    # Scan existing date folders
    existing_dirs = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d)) and len(d) == 10 and d.count('-') == 2]
    existing_dirs.sort()
    
    if not existing_dirs:
        today_str = datetime.now().strftime("%Y-%m-%d")
        return today_str, 1
    
    latest_dir = existing_dirs[-1]
    latest_date = datetime.strptime(latest_dir, "%Y-%m-%d")
    next_date = latest_date + timedelta(days=1)
    next_day_num = len(existing_dirs) + 1
    return next_date.strftime("%Y-%m-%d"), next_day_num

def create_pack(target_date, day_num):
    target_folder = os.path.join(BASE_DIR, target_date)
    os.makedirs(target_folder, exist_ok=True)
    
    curr = DAY_CURRICULUM.get(day_num, {
        "title": f"Day {day_num:02d}: Comprehensive Syllabus Drill",
        "m_topics": "Middle Stage Mathematics & Science Core Revision",
        "s_topics": "Secondary School Mathematics Targeted Topics",
        "gs_topics": "Modern Bihar History, Indian National Movement & General Science",
        "lang_topics": "Language Qualifying (Hindi Grammar & English Essentials)"
    })
    
    overview_path = os.path.join(target_folder, "DAY_OVERVIEW.md")
    with open(overview_path, "w", encoding="utf-8") as f:
        f.write(f"""# 📅 BPSC TRE 4.0 — Daily Study Module: Day {day_num:02d} ({target_date})
**Focus:** Middle (6–8 Maths & Science) + Secondary (9–10 Maths) + General Studies & Language

---

## 🎯 Today's Curriculum Focus
- **Part I: Language Qualifying:** {curr['lang_topics']}
- **Part II: General Studies:** {curr['gs_topics']}
- **Part III: Class 6–8 Maths & Science:** {curr['m_topics']}
- **Part IV: Class 9–10 Secondary Maths:** {curr['s_topics']}

---

## ⚡ Daily Action Plan
1. Review study notes and master all formulas.
2. Solve the daily 30-MCQ practice set.
3. Open `index.html` in the parent directory to log your progress and take interactive quizzes.
""")
        
    print(f"✅ Created daily study folder for Day {day_num:02d}: {target_folder}")
    print(f"   Created {overview_path}")
    return target_folder

def main():
    parser = argparse.ArgumentParser(description="Generate daily BPSC TRE 4.0 study pack.")
    parser.add_argument("--date", help="Target date in YYYY-MM-DD format")
    parser.add_argument("--day", type=int, help="Day number (e.g. 1, 2, 3...)")
    args = parser.parse_args()
    
    auto_date, auto_day = get_next_day_info()
    target_date = args.date or auto_date
    day_num = args.day or auto_day
    
    create_pack(target_date, day_num)

if __name__ == "__main__":
    main()
