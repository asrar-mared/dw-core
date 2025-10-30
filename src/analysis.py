# 🧠 وحدة تحليل رمزية داخل DW-CORE

def analyze_signature(text):
    if "لا تُشاهَد غيره في جنت" in text:
        return "✅ توقيع رمزي مُعتمد"
    return "⚠️ توقيع غير معروف"

if __name__ == "__main__":
    sample = "هذا الملف يحمل توقيع: لا تُشاهَد غيره في جنت"
    print(analyze_signature(sample))
