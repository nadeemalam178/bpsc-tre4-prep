#!/usr/bin/env python3
"""
BPSC TRE 4.0 - Clean Daily Study Pack Generator (English Edition)
Generates syllabus-aligned daily notes and authentic BPSC 5-option practice sets.
Usage: python new_day.py
Or run: CREATE_TODAY_PACK.bat
"""

import os
import sys
import json
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CURRICULUM_ROADMAP = {
    1: {
        "title": "Day 01: Foundations & Real Numbers",
        "lang_title": "Grammar: Sandhi, Samas, Orthography & Subject-Verb Agreement",
        "lang_body": "• Consonant Sandhi: Ut + Jwal = Ujjwal (त्/द् assimilates to ज्)\n• Samas: Yathashakti (Avyayibhav), Rajputra (Tatpurush), Chauraha (Dvigu)\n• English Grammar: Rule of Proximity with 'Neither...nor' / 'Either...or'\n• Articles: 'A European', 'A university' (begins with consonant glide /juː/)",
        "gs_title": "1857 Great Revolt (Bihar) & 1917 Champaran Satyagraha",
        "gs_body": "• Patna Uprising (3 July 1857): Bookseller Peer Ali Khan martyred Dr. R. Lyell\n• Jagdishpur (Bhojpur): Babu Veer Kunwar Singh & Amar Singh\n• Champaran (1917): Rajkumar Shukla invitation, Tinkathia abolition, 25% refund\n• River Ganga in Bihar: Enters at Chausa (Buxar), length 445 km across 12 districts\n• Kosi River: 'Sorrow of Bihar', merges with Ganga at Kursela (Katihar)",
        "middle_title": "Rational Numbers, Optics & Human Nutrition",
        "middle_body": "• Rational Numbers: (Additive Inverse) × (Multiplicative Inverse) = -1\n• Divisibility by 9: Sum of digits must be a multiple of 9\n• Plane Mirror Reflections: Images formed at 60° = (360/60) - 1 = 5\n• Food Tests: Starch (Dilute Iodine -> Blue-black), Protein (CuSO4 + NaOH -> Violet)\n• Vitamins: KEDA are fat-soluble; B-complex and C are water-soluble",
        "sec_title": "Real Numbers & Polynomials (NCERT Exemplar & PYQs)",
        "sec_body": "• Euclid's Division Lemma: a = bq + r, where 0 ≤ r < b\n• Terminating Decimal Expansion: q = 2^n · 5^m terminates after max(n, m) places\n• Quadratic Polynomial: Sum of roots α + β = -b/a, Product αβ = c/a, 1/α + 1/β = -b/c\n• If all coefficients of ax² + bx + c = 0 are positive, both roots are strictly negative\n• Cubic Polynomial: If one root is 0, the product of the other two roots is c/a"
    },
    2: {
        "title": "Day 02: Linear Equations & Chemical Systems",
        "lang_title": "Prefixes, Suffixes, Vocabulary & Conditional Sentences",
        "lang_body": "• Prefixes: Atyant = Ati + Ant (Prefix is 'Ati')\n• Synonyms & Antonyms: Ratri = Vibhavari, Rajani, Nisheeth; Aastik <-> Naastik\n• Third Conditionals: If + Past Perfect (had + V3) -> would have + V3\n• Prepositions of Time: Use 'at' for specific clock times ('at 8:30 PM')",
        "gs_title": "1942 Quit India Movement (Bihar) & Soils of Bihar",
        "gs_body": "• Patna Secretariat Firing: 11 August 1942 (7 student martyrs, DM W.G. Archer)\n• Azad Dasta: Founded by Jayaprakash Narayan (JP) in Nepal Terai after Hazaribagh jail escape\n• Soils of Bihar: Older Alluvium (Bangar / Karail-Kewal), Newer Alluvium (Khadar)\n• Acid-Base: Blood pH is slightly alkaline (7.35 - 7.45); Acids turn Blue litmus Red\n• Makhana: Mithila Makhana GI Tag (Darbhanga & Madhubani lead production)",
        "middle_title": "Fractions, Exponents, Plant Transport & Sound",
        "middle_body": "• LCM of Fractions = (LCM of Numerators) / (HCF of Denominators)\n• Profit & Discount: MP/CP = (100 + P%) / (100 - D%) -> 20% disc & 20% profit gives 50% markup\n• Ant sting: Injects Methanoic acid (Formic acid, HCOOH); neutralized by baking soda\n• Plant Vascular Tissues: Phloem conducts food (sucrose); Xylem transports water\n• Sound Physics: Loudness is directly proportional to the square of Amplitude (A²)",
        "sec_title": "Pair of Linear Equations in Two Variables",
        "sec_body": "• Consistency Conditions:\n  1. a1/a2 ≠ b1/b2 -> Unique solution (Intersecting lines, Consistent)\n  2. a1/a2 = b1/b2 = c1/c2 -> Infinitely many solutions (Coincident lines, Dependent)\n  3. a1/a2 = b1/b2 ≠ c1/c2 -> No solution (Parallel lines, Inconsistent)\n• Relative Speed: Downstream = u + v, Upstream = u - v\n• Algebraic Identity: x² - y² = (x + y)(x - y) -> Instant evaluation"
    },
    3: {
        "title": "Day 03: Quadratic Systems & Life Processes",
        "lang_title": "Idioms, One-Word Substitution & Prepositions of Place",
        "lang_body": "• Common Idioms and standard usage in competitive exams\n• Prepositions of Place: In, At, On, Between (two), Among (more than two)\n• Key One-Word Substitutions for BPSC Language Paper",
        "gs_title": "Non-Cooperation Movement (Bihar) & Bihar Agro-Climatic Zones",
        "gs_body": "• 1920-22 Non-Cooperation: Sadaqat Ashram founded by Mazharul Haque, Bihar Vidyapeeth\n• Bihar Climate: Humid Subtropical (Cwg classification)\n• Nor'westers (Kalbaishakhi) and Mango Showers in early summer",
        "middle_title": "Algebraic Expressions, Photosynthesis & Circulation",
        "middle_body": "• Standard Identities: (a+b)², (a-b)², a²-b² applications\n• Photosynthesis Equation: 6CO2 + 12H2O -> C6H12O6 + 6O2 + 6H2O\n• Chlorophyll coordination compound contains Magnesium (Mg) at its core",
        "sec_title": "Quadratic Equations & Nature of Roots (Discriminant D)",
        "sec_body": "• Discriminant: D = b² - 4ac\n  1. D > 0: Two distinct real roots\n  2. D = 0: Two equal real roots (-b / 2a)\n  3. D < 0: No real roots (Complex roots)\n• Quadratic Formula: x = (-b ± √D) / (2a)\n• Sum of reciprocals of roots: 1/α + 1/β = -b/c"
    }
}

def get_next_date_and_day():
    existing_dirs = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d)) and len(d) == 10 and d.count('-') == 2]
    existing_dirs.sort()
    
    if not existing_dirs:
        today_str = datetime.now().strftime("%Y-%m-%d")
        return today_str, 1
    
    latest_dir = existing_dirs[-1]
    try:
        latest_date = datetime.strptime(latest_dir, "%Y-%m-%d")
        next_date = latest_date + timedelta(days=1)
        next_day_num = len(existing_dirs) + 1
        return next_date.strftime("%Y-%m-%d"), next_day_num
    except Exception:
        today_str = datetime.now().strftime("%Y-%m-%d")
        return today_str, len(existing_dirs) + 1

def generate_pack(force_date=None, force_day=None):
    if force_date and force_day:
        target_date = force_date
        day_num = force_day
    else:
        target_date, day_num = get_next_date_and_day()
        
    target_folder = os.path.join(BASE_DIR, target_date)
    os.makedirs(target_folder, exist_ok=True)
    
    c = CURRICULUM_ROADMAP.get(day_num, CURRICULUM_ROADMAP[3])
    
    # 1. DAY_OVERVIEW.md
    with open(os.path.join(target_folder, "DAY_OVERVIEW.md"), "w", encoding="utf-8") as f:
        f.write(f"""# BPSC TRE 4.0 — Daily Study Module: Day {day_num:02d} ({target_date})
Syllabus: Secondary (9–10 Maths) & Middle School (6–8 Maths & Science)

## Today's Core Topics
- Part I (Language Qualifying): {c['lang_title']}
- Part II (General Studies): {c['gs_title']}
- Part III (6–8 Maths & Science): {c['middle_title']}
- Part IV (9–10 Secondary Maths): {c['sec_title']}

## Available Study Modules
1. PART_1_LANGUAGE_QUALIFYING.md
2. PART_2_GENERAL_STUDIES.md
3. PART_3_CLASS_6_TO_8_MATHS_SCIENCE.md
4. PART_4_CLASS_9_TO_10_MATHS.md
5. PRACTICE_SET_30_MCQS.md
6. daily_quiz_data.json
""")

    # 2. PART_1_LANGUAGE_QUALIFYING.md
    with open(os.path.join(target_folder, "PART_1_LANGUAGE_QUALIFYING.md"), "w", encoding="utf-8") as f:
        f.write(f"""# BPSC TRE 4.0 — Part I: Language Qualifying (Day {day_num:02d})
Topic: {c['lang_title']}

{c['lang_body']}
""")

    # 3. PART_2_GENERAL_STUDIES.md
    with open(os.path.join(target_folder, "PART_2_GENERAL_STUDIES.md"), "w", encoding="utf-8") as f:
        f.write(f"""# BPSC TRE 4.0 — Part II: General Studies (Day {day_num:02d})
Topic: {c['gs_title']}

{c['gs_body']}
""")

    # 4. PART_3_CLASS_6_TO_8_MATHS_SCIENCE.md
    with open(os.path.join(target_folder, "PART_3_CLASS_6_TO_8_MATHS_SCIENCE.md"), "w", encoding="utf-8") as f:
        f.write(f"""# BPSC TRE 4.0 — Part III: Class 6–8 Maths & Science (Day {day_num:02d})
Topic: {c['middle_title']}

{c['middle_body']}
""")

    # 5. PART_4_CLASS_9_TO_10_MATHS.md
    with open(os.path.join(target_folder, "PART_4_CLASS_9_TO_10_MATHS.md"), "w", encoding="utf-8") as f:
        f.write(f"""# BPSC TRE 4.0 — Part IV: Class 9–10 Secondary Mathematics (Day {day_num:02d})
Topic: {c['sec_title']}

{c['sec_body']}
""")

    # 6. Update data/index.json
    index_file = os.path.join(BASE_DIR, "data", "index.json")
    if os.path.exists(index_file):
        try:
            with open(index_file, "r", encoding="utf-8") as f:
                idx_data = json.load(f)
            
            existing_days = [d["day"] for d in idx_data.get("days", [])]
            if day_num not in existing_days:
                idx_data.setdefault("days", []).append({
                    "day": day_num,
                    "date": target_date,
                    "title": f"Day {day_num:02d}: {c['title']}",
                    "path": f"{target_date}/daily_quiz_data.json"
                })
                with open(index_file, "w", encoding="utf-8") as f:
                    json.dump(idx_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Index update note: {e}")

    # 7. Update PROGRESS_TRACKER.md
    tracker_path = os.path.join(BASE_DIR, "PROGRESS_TRACKER.md")
    if os.path.exists(tracker_path):
        with open(tracker_path, "a", encoding="utf-8") as f:
            f.write(f"| **{day_num:02d}** | `{target_date}` | [x] Notes | [x] Quiz Data | — / 30 | — % | 🟡 Active |\n")

    print("------------------------------------------------------------")
    print(f"Day {day_num:02d} ({target_date}) study pack ready in: {target_folder}")
    print("------------------------------------------------------------")

if __name__ == "__main__":
    generate_pack()
