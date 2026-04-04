import ipywidgets as widgets
from IPython.display import display
import numpy as np

# ====================== 1. 模型系数配置 ======================
intercept = -5.0 
coefs = {
    "age": np.log(1.04),   # 年龄
    "esr": np.log(1.24),   # 红细胞沉降率 (ESR)
    "hb": np.log(1.03),    # 血红蛋白 (Hb)
    "plt": np.log(0.99),   # 血小板 (PLT)
    "glo": np.log(0.91),   # 球蛋白 (GLO)
    "sii": np.log(1.01),   # SII 指数
    "sri": np.log(1.66)    # 双侧RI总分
}

# ====================== 2. 预测函数 ======================
def on_predict_clicked(b):
    # 计算线性组合
    z = intercept + \
        coefs["age"] * w_age.value + \
        coefs["esr"] * w_esr.value + \
        coefs["hb"] * w_hb.value + \
        coefs["plt"] * w_plt.value + \
        coefs["glo"] * w_glo.value + \
        coefs["sii"] * w_sii.value + \
        coefs["sri"] * w_sri.value
    
    # 逻辑回归概率
    probability = 1 / (1 + np.exp(-z))
    
    # 显示结果（4位小数 + 百分比）
    result_text.value = f"预测概率：{probability:.4f}   ≈ {probability:.2%}"

# ====================== 3. 创建输入控件 ======================
def create_styled_input(label_name):
    label = widgets.Label(value=f"{label_name}:", layout=widgets.Layout(margin='8px 0 0 0'))
    text_box = widgets.FloatText(value=0, layout=widgets.Layout(width='98%'))
    return widgets.VBox([label, text_box])

# 生成输入框
w_age_box = create_styled_input("年龄")
w_age = w_age_box.children[1]

w_esr_box = create_styled_input("红细胞沉降率 (ESR)")
w_esr = w_esr_box.children[1]

w_hb_box = create_styled_input("血红蛋白 (Hb)")
w_hb = w_hb_box.children[1]

w_plt_box = create_styled_input("血小板 (PLT)")
w_plt = w_plt_box.children[1]

w_glo_box = create_styled_input("球蛋白 (GLO)")
w_glo = w_glo_box.children[1]

w_sii_box = create_styled_input("SII 指数")
w_sii = w_sii_box.children[1]

w_sri_box = create_styled_input("双侧RI总分")
w_sri = w_sri_box.children[1]

# ====================== 4. 按钮与结果 ======================
predict_btn = widgets.Button(
    description="开始预测",
    button_style="success",  # 绿色按钮
    layout=widgets.Layout(margin='20px 0', width='120px')
)
predict_btn.on_click(on_predict_clicked)

# 结果显示
result_text = widgets.Label(
    value="预测概率：0",
    layout=widgets.Layout(margin='10px 0', font_size="14px")
)

# ====================== 5. 界面布局（已修复） ======================
title = widgets.HTML("<h3>疾病风险预测模型</h3>")  # 这里是关键修复

input_row1 = widgets.HBox([w_age_box, w_esr_box, w_hb_box, w_plt_box], 
                          layout=widgets.Layout(gap='10px', margin='10px 0'))
input_row2 = widgets.HBox([w_glo_box, w_sii_box, w_sri_box], 
                          layout=widgets.Layout(gap='10px', margin='10px 0'))

# 整体界面
ui = widgets.VBox([
    title,
    input_row1,
    input_row2,
    predict_btn,
    result_text
], layout=widgets.Layout(padding='15px'))

# 显示界面
display(ui)