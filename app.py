# -*- coding: utf-8 -*-
import streamlit as st
import numpy as np

# ---------------------- 模型系数 ----------------------
intercept = -5.0
coefs = {
    "age": np.log(1.04),    # 年龄
    "esr": np.log(1.24),    # 红细胞沉降率
    "hb": np.log(1.03),     # 血红蛋白
    "plt": np.log(0.99),    # 血小板
    "glo": np.log(0.91),    # 球蛋白
    "sii": np.log(1.01),    # SII 指数
    "sri": np.log(1.66)     # 双侧RI总分
}

# ---------------------- 页面标题 ----------------------
st.title("🧬 疾病风险预测工具")
st.markdown("---")

# ---------------------- 输入控件 ----------------------
age = st.slider("年龄", 0, 100, 40)
esr = st.number_input("ESR (mm/h)", value=10.0)
hb = st.number_input("Hb (g/L)", value=140.0)
plt = st.number_input("PLT (10^9/L)", value=250.0)
glo = st.number_input("GLO (g/L)", value=30.0)
sii = st.number_input("SII 指数", value=400.0)
sri = st.number_input("双侧RI总分", value=5.0)

# ---------------------- 计算风险 ----------------------
z = intercept +\
    coefs["age"] * age +\
    coefs["esr"] * esr +\
    coefs["hb"] * hb +\
    coefs["plt"] * plt +\
    coefs["glo"] * glo +\
    coefs["sii"] * sii +\
    coefs["sri"] * sri

probability = 1 / (1 + np.exp(-z))

# ---------------------- 结果显示 ----------------------
st.markdown("---")
st.subheader("📊 预测结果")

prob_percent = f"{probability:.2%}"

if probability > 0.5:
    st.error(f"🔴 预测患病概率：{prob_percent}")
    st.warning("高风险，建议尽快复查！")
else:
    st.success(f"🟢 预测患病概率：{prob_percent}")
    st.info("目前处于低风险状态，继续保持！")
