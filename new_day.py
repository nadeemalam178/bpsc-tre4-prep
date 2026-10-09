#!/usr/bin/env python3
"""
BPSC TRE 4.0 - Clean Daily Study Pack Generator
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
        "lang_title": "संधि, समास, वर्तनी शुद्धि एवं Subject-Verb Agreement",
        "lang_body": "• स्वर व व्यंजन संधि (उज्ज्वल = उत् + ज्वल)\n• 6 समास (यथाशक्ति = अव्ययीभाव समास)\n• वर्तनी: कवयित्री, उज्ज्वल, आशीर्वाद\n• English: Rule of Proximity with Neither...nor (closest subject)",
        "gs_title": "1857 क्रांति (बिहार) एवं 1917 चंपारण सत्याग्रह",
        "gs_body": "• पटना में पीर अली का विद्रोह (3 जुलाई 1857, डॉ. लॉयल)\n• जगदीशपुर में बाबू वीर कुंवर सिंह व अमर सिंह\n• चंपारण (1917): राजकुमार शुक्ल का निमंत्रण, 3/20 तिनकठिया, 25% अवैध वसूली वापसी\n• गंगा नदी बिहार में चौसा (बक्सर) से प्रवेश करती है (445 किमी, 12 जिले)\n• कोसी नदी: बिहार का शोक, कुरसेला (कटिहार) में गंगा से मिलन",
        "middle_title": "परिमेय संख्याएँ, विभाज्यता, पोषक तत्व एवं गोलीय दर्पण",
        "middle_body": "• परिमेय संख्याएँ: (योज्य प्रतिलोम) × (गुणात्मक प्रतिलोम) = -1\n• 9 से विभाज्यता: अंकों का योग 9 से कटना चाहिए\n• प्रकाश: 60° पर झुके दर्पण में बनने वाले प्रतिबिंब = (360/60) - 1 = 5\n• भोजन: स्टार्च (आयोडीन -> नीला-काला), प्रोटीन (CuSO4 + NaOH -> बैंगनी)\n• विटामिन C (एस्कॉर्बिक एसिड) की कमी से स्कर्वी",
        "sec_title": "वास्तविक संख्याएँ एवं बहुपद (NCERT Exemplar & PYQs)",
        "sec_body": "• यूक्लिड प्रमेयिका: a = bq + r (0 ≤ r < b)\n• सांत दशमलव: q = 2^n · 5^m होने पर max(n, m) स्थानों के बाद सांत\n• बहुपद: 1/α + 1/β = -b/c\n• x² + 99x + 127: सभी गुणांक धनात्मक होने पर दोनों शून्यक सदैव ऋणात्मक\n• त्रिघात: एक शून्यक 0 होने पर अन्य दो का गुणन = c/a"
    },
    2: {
        "title": "Day 02: Linear Equations & Chemical Systems",
        "lang_title": "उपसर्ग, प्रत्यय, पर्यायवाची, विलोम एवं Tenses",
        "lang_body": "• उपसर्ग एवं प्रत्यय के भेद व BPSC में पूछे गए शब्द\n• प्रमुख पर्यायवाची व विलोम शब्द संग्रह\n• English: Conditionals (If clause rules: If + Past Perfect -> Would have + V3)",
        "gs_title": "1942 भारत छोड़ो आंदोलन (बिहार) एवं बिहार की मृदा",
        "gs_body": "• 1942 अगस्त क्रांति: पटना सचिवालय गोलीकांड (11 अगस्त 1942, 7 शहीद छात्र, डीएम आर्चर)\n• जयप्रकाश नारायण एवं आजाद दस्ता (नेपाल की तराई, हजारीबाग जेल से पलायन)\n• बिहार की मृदा: पुरानी जलोढ़ (बांगर) एवं नवीन जलोढ़ (खादर - बाढ़ क्षेत्र)\n• बिहार का कृषि-जलवायु क्षेत्र (Zone I, II, IIIA, IIIB)",
        "middle_title": "भिन्न, दशमलव, घातांक एवं अम्ल-क्षार-लवण",
        "middle_body": "• भिन्नों का ल.स.प. व म.स.प. सूत्र\n• अम्ल, क्षार व लवण: लिटमस, हल्दी, फेनोल्फथलीन सूचक रंग परिवर्तन\n• pH पैमाना (सोरेनसन): रक्त का pH 7.4, आमाशय का HCl pH 1.5-2.0\n• उदासीनीकरण अभिक्रिया (Neutralization) एवं लवण निर्माण",
        "sec_title": "दो चरों वाले रैखिक समीकरण युग्म (Linear Equations in 2 Variables)",
        "sec_body": "• संगत व असंगत की शर्तें:\n  1. a1/a2 ≠ b1/b2 -> अद्वितीय हल (प्रतिच्छेदी रेखाएँ, संगत)\n  2. a1/a2 = b1/b2 = c1/c2 -> अनंत अनेक हल (संपाती रेखाएँ, आश्रित/संगत)\n  3. a1/a2 = b1/b2 ≠ c1/c2 -> कोई हल नहीं (समांतर रेखाएँ, असंगत)\n• धारा के अनुकूल (Downstream: u + v) व प्रतिकूल (Upstream: u - v) वाले प्रश्न\n• विलोपन एवं वज्र-गुणन विधियों के त्वरित नियम"
    },
    3: {
        "title": "Day 03: Quadratic Systems & Life Processes",
        "lang_title": "मुहावरे, लोकोक्तियाँ, अनेक शब्दों के एक शब्द एवं Prepositions",
        "lang_body": "• मुहावरे एवं लोकोक्तियाँ: BPSC में पूछे गए प्रमुख मुहावरे\n• Prepositions of Place and Time (In, At, On, Between, Among)\n• अनेक शब्दों के लिए एक शब्द संकलन",
        "gs_title": "असहयोग आंदोलन (बिहार) एवं बिहार की जलवायु",
        "gs_body": "• 1920-22 असहयोग आंदोलन: सदाकत आश्रम (मजहरुल हक), बिहार विद्यापीठ स्थापना\n• बिहार की जलवायु: उपोष्ण मानसूनी (Cwg वर्गीकरण)\n• कालवैशाखी (Nor'westers) एवं आम्र वर्षा (Mango showers)",
        "middle_title": "बीजीय व्यंजक, पादप पोषण एवं प्रकाश संश्लेषण",
        "middle_body": "• मानक सर्वसमिकाएँ: (a+b)², (a-b)², a²-b² अनुप्रयोग\n• पौधों में पोषण: प्रकाश संश्लेषण समीकरण (6CO2 + 12H2O -> C6H12O6 + 6O2 + 6H2O)\n• क्लोरोफिल में मैग्नीशियम (Mg) धातु की उपस्थिति",
        "sec_title": "द्विघात समीकरण (Quadratic Equations & Discriminant D)",
        "sec_body": "• विविक्तकर: D = b² - 4ac\n  1. D > 0: दो भिन्न वास्तविक मूल\n  2. D = 0: दो बराबर वास्तविक मूल (-b/2a)\n  3. D < 0: कोई वास्तविक मूल नहीं (काल्पनिक मूल)\n• द्विघात सूत्र: x = (-b ± √D) / 2a\n• मूलों के व्युत्क्रम का योग = -b/c"
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
        f.write(f"""# BPSC TRE 4.0 — दैनिक अध्ययन: Day {day_num:02d} ({target_date})
पाठ्यक्रम: माध्यमिक (9–10 गणित) एवं मध्य विद्यालय (6–8 गणित-विज्ञान)

## आज के विषय
- भाग I (भाषा अहर्ता): {c['lang_title']}
- भाग II (सामान्य अध्ययन): {c['gs_title']}
- भाग III (6–8 गणित-विज्ञान): {c['middle_title']}
- भाग IV (9–10 माध्यमिक गणित): {c['sec_title']}

## अध्ययन सामग्री
1. PART_1_LANGUAGE_QUALIFYING.md
2. PART_2_GENERAL_STUDIES.md
3. PART_3_CLASS_6_TO_8_MATHS_SCIENCE.md
4. PART_4_CLASS_9_TO_10_MATHS.md
5. PRACTICE_SET_30_MCQS.md
6. daily_quiz_data.json
""")

    # 2. PART_1_LANGUAGE_QUALIFYING.md
    with open(os.path.join(target_folder, "PART_1_LANGUAGE_QUALIFYING.md"), "w", encoding="utf-8") as f:
        f.write(f"""# BPSC TRE 4.0 — भाग I: भाषा अहर्ता (Day {day_num:02d})
विषय: {c['lang_title']}

{c['lang_body']}
""")

    # 3. PART_2_GENERAL_STUDIES.md
    with open(os.path.join(target_folder, "PART_2_GENERAL_STUDIES.md"), "w", encoding="utf-8") as f:
        f.write(f"""# BPSC TRE 4.0 — भाग II: सामान्य अध्ययन (Day {day_num:02d})
विषय: {c['gs_title']}

{c['gs_body']}
""")

    # 4. PART_3_CLASS_6_TO_8_MATHS_SCIENCE.md
    with open(os.path.join(target_folder, "PART_3_CLASS_6_TO_8_MATHS_SCIENCE.md"), "w", encoding="utf-8") as f:
        f.write(f"""# BPSC TRE 4.0 — भाग III: 6–8 गणित एवं विज्ञान (Day {day_num:02d})
विषय: {c['middle_title']}

{c['middle_body']}
""")

    # 5. PART_4_CLASS_9_TO_10_MATHS.md
    with open(os.path.join(target_folder, "PART_4_CLASS_9_TO_10_MATHS.md"), "w", encoding="utf-8") as f:
        f.write(f"""# BPSC TRE 4.0 — भाग IV: 9–10 माध्यमिक गणित (Day {day_num:02d})
विषय: {c['sec_title']}

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
    print(f"Day {day_num:02d} ({target_date}) study pack ready in folder: {target_folder}")
    print("------------------------------------------------------------")

if __name__ == "__main__":
    generate_pack()
