import streamlit as st

fishing_data = {
    "大武崙": {
        "1月": ("偏冷，黑潮遠離", "花枝（少）、鯖魚、小白帶魚"),
        "4月": ("黑潮北推開始靠近", "花枝活性開始升高，夜釣可試"),
        "6月": ("黑潮最接近", "透抽旺季、可嘗試夜間Eging"),
        "10月": ("黑潮遠離", "白帶魚、秋刀魚"),
    },
    "鼻頭角": {
        "1月": ("黑潮遠離，偏冷水", "深場小透抽、白帶魚"),
        "4月": ("黑潮接近，水溫上升", "花枝活性強、Eging旺季"),
        "6月": ("黑潮最強，外礁水溫高", "透抽、鬼頭刀、小鮪魚"),
        "10月": ("黑潮轉弱", "竹筴魚、底棲魚穩定"),
    },
    "潮境公園": {
        "1月": ("黑潮影響低", "底棲魚類活動緩慢"),
        "4月": ("黑潮推進", "透抽、花枝活性提高"),
        "6月": ("黑潮旺季", "夜釣透抽、表層魚靠近"),
        "10月": ("黑潮轉弱", "秋刀魚、白帶魚夜咬"),
    }
}

st.title("🎣 黑潮釣況小助手")

location = st.selectbox("選擇釣點", list(fishing_data.keys()))
month = st.selectbox("選擇月份", ["1月", "4月", "6月", "10月"])

if location and month:
    condition, recommendation = fishing_data[location].get(month, ("無資料", "無建議"))
    st.subheader("🌊 黑潮狀況")
    st.write(condition)
    st.subheader("🐟 建議釣況 / 魚種")
    st.write(recommendation)
